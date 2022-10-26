import argparse
# import logging
import numpy as np
from pathlib import Path
from tqdm import tqdm
import librosa
# import pyworld as pw
import torch
import soundfile as sf

def encode_dataset(args):
    print(f"Loading hubert checkpoint")
    hubert = torch.hub.load("bshall/hubert:main", f"hubert_{args.model}")#.cuda()

    print(f"Encoding dataset at {args.in_dir}")
    for in_path in tqdm(list(args.in_dir.rglob(f"*{args.extension}"))):
        wav, sr = librosa.load(in_path,sr=None)

        assert(sr>15999)
        if len(wav.shape) > 1:
            wav = librosa.to_mono(wav)

        
        wav22 = librosa.resample(wav, sr, 22050)

        out_path = args.out_dir / in_path.relative_to(args.in_dir)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        sf.write(out_path.with_suffix(".wav"), wav22,22050, 'PCM_16')
        # np.save(out_path.with_suffix(".npy"), output.squeeze().cpu().numpy())


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
