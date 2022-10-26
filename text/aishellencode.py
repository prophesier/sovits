import argparse
# import logging
import numpy as np
from pathlib import Path
from tqdm import tqdm
import librosa
import pyworld as pw
import torch
# import torchaudio
# from torchaudio.functional import resample
def resize2d(source, target_len):
    source[source<0.001] = np.nan
    target = np.interp(np.linspace(0, len(source)-1, num=target_len,endpoint=True), np.arange(0, len(source)), source)
    return np.nan_to_num(target)
def _calculate_f0(input: np.ndarray,sr,length,f0min,f0max,
                      use_continuous_f0: bool=True,
                      use_log_f0: bool=True) -> np.ndarray:
        input = input.astype(float)
        frame_period = len(input)/sr/(length)*1000
        f0, timeaxis = pw.dio(
            input,
            fs=sr,
            f0_floor=f0min,
            f0_ceil=f0max,
            frame_period=frame_period)
        f0 = pw.stonemask(input, f0, timeaxis, sr)
        # if use_continuous_f0:
        #     f0 = self._convert_to_continuous_f0(f0)
        if use_log_f0:
            nonzero_idxs = np.where(f0 != 0)[0]
            f0[nonzero_idxs] = np.log(f0[nonzero_idxs])
        return f0.reshape(-1)


def encode_dataset(args):
    print(f"Loading hubert checkpoint")
    hubert = torch.hub.load("bshall/hubert:main", f"hubert_{args.model}")#.cuda()

    print(f"Encoding dataset at {args.in_dir}")
    for in_path in tqdm(list(args.in_dir.rglob(f"*{args.extension}"))):
        wav, sr = librosa.load(in_path,sr=None)

        assert(sr>15999)
        if len(wav.shape) > 1:
            wav = librosa.to_mono(wav)

        
        wav16 = librosa.resample(wav, sr, 16000)
        # wav = wav.unsqueeze(0)#.cuda()
        # print(wav.shape)
        
        source = torch.FloatTensor(wav16).unsqueeze(0).unsqueeze(0)
        with torch.inference_mode():
            units = hubert.units(source)

        
        f0=_calculate_f0(wav,sr,units.shape[1],
                f0min=librosa.note_to_hz('C2'),
                f0max=librosa.note_to_hz('C7'))
        f0=resize2d(f0,units.shape[1])

        f0 = torch.FloatTensor(f0).unsqueeze(-1).unsqueeze(0)

        output=torch.cat([units,f0,f0],dim=2)

        out_path = args.out_dir / in_path.relative_to(args.in_dir)
        out_path.parent.mkdir(parents=True, exist_ok=True)

        np.save(out_path.with_suffix(".npy"), output.squeeze().cpu().numpy())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode an audio dataset.")
    parser.add_argument(
        "model",
        help="available models (HuBERT-Soft or HuBERT-Discrete)",
        choices=["soft", "discrete"],
    )
    parser.add_argument(
        "in_dir",
        metavar="in-dir",
        help="path to the dataset directory.",
        type=Path,
    )
    parser.add_argument(
        "out_dir",
        metavar="out-dir",
        help="path to the output directory.",
        type=Path,
    )
    parser.add_argument(
        "--extension",
        help="extension of the audio files (defaults to .wav).",
        default='.wav',#".flac",
        type=str,
    )
    args = parser.parse_args()
    encode_dataset(args)
