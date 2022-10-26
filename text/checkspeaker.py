import os
prepath='G:/Dataset/AISHELL-3/'
test='test/wav'
train='train/wav'
spktest=os.listdir(prepath+test)
spktrain=os.listdir(prepath+train)
# print(spktest)
# print(spktrain)
spkelse=[]
spkall=[]
for spk in spktest:
    if not (spk in spktrain):
        spkelse.append(spk)
    else:
        spkall.append(spk)
for spk in spktrain:
    if not (spk in spktest):
        print(spk)
print(len(spktest))
print(len(spktrain))
print(len(spkelse))
print(len(spkall))
print(spkelse)
# traindict=dict((value,key) for key,value in enumerate(spktrain))
# print(traindict)