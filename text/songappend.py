import os
from pathlib import Path
from tqdm import tqdm
path=Path('G:\Dataset\opencpop\split')

processed=[]

for in_path in tqdm(list(path.rglob(f"*wav"))):
    songpath='DUMMY3/trainsong/split/'+in_path.name
    encodepath='DUMMY3/trainsongencode/split/'+in_path.name[:-4]+'.npy'
    result='|'.join([songpath,str(174),encodepath])+'\n'
    processed+=[result]
with open('aishell3_sid_encode_train.txt.cleaned','a',encoding='utf-8') as data:
    data.writelines(processed)