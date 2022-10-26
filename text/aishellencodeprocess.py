processed=[]
traindict={'SSB0005': 0, 'SSB0009': 1, 'SSB0011': 2, 'SSB0012': 3, 'SSB0016': 4, 'SSB0018': 5, 'SSB0033': 6, 'SSB0038': 7, 'SSB0043': 8, 'SSB0057': 9, 'SSB0073': 10, 'SSB0080': 11, 'SSB0112': 12, 'SSB0122': 13, 'SSB0133': 14, 'SSB0139': 15, 'SSB0145': 16, 'SSB0149': 17, 'SSB0193': 18, 'SSB0197': 19, 'SSB0200': 20, 'SSB0241': 21, 'SSB0246': 22, 'SSB0261': 23, 'SSB0267': 24, 'SSB0273': 25, 'SSB0287': 26, 'SSB0288': 27, 'SSB0299': 28, 'SSB0307': 29, 'SSB0309': 30, 'SSB0315': 31, 'SSB0316': 32, 'SSB0323': 33, 'SSB0338': 34, 'SSB0339': 35, 'SSB0341': 36, 'SSB0342': 37, 'SSB0354': 38, 'SSB0366': 39, 'SSB0375': 40, 'SSB0379': 41, 'SSB0380': 42, 'SSB0382': 43, 'SSB0385': 44, 'SSB0393': 45, 'SSB0394': 46, 'SSB0395': 47, 'SSB0407': 48, 'SSB0415': 49, 'SSB0426': 50, 'SSB0427': 51, 'SSB0434': 52, 'SSB0435': 53, 'SSB0470': 54, 'SSB0482': 55, 'SSB0502': 56, 'SSB0534': 57, 'SSB0535': 58, 'SSB0539': 59, 'SSB0544': 60, 'SSB0565': 61, 'SSB0570': 62, 'SSB0578': 63, 'SSB0588': 64, 'SSB0590': 65, 'SSB0594': 66, 'SSB0599': 67, 'SSB0601': 68, 'SSB0603': 69, 'SSB0606': 70, 'SSB0607': 71, 'SSB0609': 72, 'SSB0614': 73, 'SSB0623': 74, 'SSB0629': 75, 'SSB0631': 76, 'SSB0632': 77, 'SSB0666': 78, 'SSB0668': 79, 'SSB0671': 80, 'SSB0686': 81, 'SSB0700': 82, 'SSB0710': 83, 'SSB0720': 84, 'SSB0723': 85, 'SSB0737': 86, 'SSB0746': 87, 'SSB0748': 88, 'SSB0751': 89, 'SSB0758': 90, 'SSB0760': 91, 'SSB0762': 92, 'SSB0778': 93, 'SSB0780': 94, 'SSB0784': 95, 'SSB0786': 96, 'SSB0794': 97, 'SSB0817': 98, 'SSB0851': 99, 'SSB0863': 100, 'SSB0871': 101, 'SSB0887': 102, 'SSB0913': 103, 'SSB0915': 104, 'SSB0919': 105, 'SSB0935': 106, 'SSB0966': 107, 'SSB0987': 108, 'SSB1008': 109, 'SSB1020': 110, 'SSB1024': 111, 'SSB1050': 112, 'SSB1055': 113, 'SSB1056': 114, 'SSB1064': 115, 'SSB1072': 116, 'SSB1091': 117, 'SSB1096': 118, 'SSB1100': 119, 'SSB1108': 120, 'SSB1115': 121, 'SSB1125': 122, 'SSB1131': 123, 'SSB1136': 124, 'SSB1138': 125, 'SSB1161': 126, 'SSB1203': 127, 'SSB1204': 128, 'SSB1218': 129, 'SSB1221': 130, 'SSB1253': 131, 'SSB1320': 132, 'SSB1341': 133, 'SSB1366': 134, 'SSB1377': 135, 'SSB1383': 136, 'SSB1385': 137, 'SSB1392': 138, 'SSB1393': 139, 'SSB1408': 140, 'SSB1431': 141, 'SSB1437': 142, 'SSB1448': 143, 'SSB1555': 144, 'SSB1563': 145, 'SSB1567': 146, 'SSB1575': 147, 'SSB1585': 148, 'SSB1593': 149, 'SSB1607': 150, 'SSB1624': 151, 'SSB1625': 152, 'SSB1630': 153, 'SSB1650': 154, 'SSB1670': 155, 'SSB1684': 156, 'SSB1686': 157, 'SSB1699': 158, 'SSB1711': 159, 'SSB1759': 160, 'SSB1806': 161, 'SSB1828': 162, 'SSB1831': 163, 'SSB1832': 164, 'SSB1837': 165, 'SSB1846': 166, 'SSB1863': 167, 'SSB1878': 168, 'SSB1891': 169, 'SSB1918': 170, 'SSB1935': 171, 'SSB1939': 172, 'SSB1956': 173}
with open('content.txt','r',encoding='utf-8') as content:
    raw=[line.rstrip() for line in content.readlines()]
    for item in raw:
        sp=item.split('	')
        filename=sp[0]
        filepath=sp[0][:7]
        try:
            speaker=traindict[filepath]
        except:
            continue
        path='DUMMY3/train/wav/'+filepath+'/'+filename
        encodepath='DUMMY3/trainencode/wav/'+filepath+'/'+filename[:11]+'.npy'
        result='|'.join([path,str(speaker),encodepath])+'\n'
        processed+=[result]

with open('aishell3_sid_encode_train.txt.cleaned','w',encoding='utf-8') as data:
    data.writelines(processed)
