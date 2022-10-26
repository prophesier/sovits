""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")

pinyin_to_phoneme={}
phoneme_to_id={}
id_to_phoneme={}
with open('text/pinyin.dict','r',encoding='utf-8') as pydict:
    pinyin_to_phoneme=dict((line.rstrip().split(' ')[0],line.rstrip().split(' ')[1:]) for line in pydict.readlines())

with open('text/phone_id_map.txt','r',encoding='utf-8') as iddict:
    phoneme_to_id=dict((line.rstrip().split(' ')[0],line.rstrip().split(' ')[1]) for line in iddict.readlines())
    id_to_phoneme=dict((line.rstrip().split(' ')[1],line.rstrip().split(' ')[0]) for line in iddict.readlines())
# print(pinyin_to_phoneme)
#print(len(phoneme_to_id))
# print(id_to_phoneme)
