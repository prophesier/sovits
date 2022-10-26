""" from https://github.com/keithito/tacotron """
from text import cleaners
from text.symbols import symbols,phoneme_to_id,pinyin_to_phoneme,id_to_phoneme


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}


def text_to_sequence(text, cleaner_names,chinese=True):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = []
  if chinese:
    clean_text = _clean_text(text, cleaner_names)
    add_space=(' æ '.join(clean_text.split(' '))).split(' ')
    phoneme=[]
    for pinyin in add_space:
      try:
        phone=pinyin_to_phoneme[pinyin]
      except:
        phone=[pinyin]
      phoneme+=phone
    for phone in phoneme:
      code=[]
      try:
        code=[int(phoneme_to_id[phone])]
      except:
        if phone!='':
          code=[int(phoneme_to_id['<unk>'])]
      sequence+=code
  else:
    clean_text = _clean_text(text, cleaner_names)
    for symbol in clean_text:
      symbol_id = _symbol_to_id[symbol]
      sequence += [symbol_id]
  return sequence


def cleaned_text_to_sequence(cleaned_text,chinese=True):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence=[]
  if chinese:
    add_space=(' æ '.join(cleaned_text.split(' '))).split(' ')
    phoneme=[]
    for pinyin in add_space:
      try:
        phone=pinyin_to_phoneme[pinyin]
      except:
        phone=[pinyin]
      phoneme+=phone
    for phone in phoneme:
      code=[]
      try:
        code=[int(phoneme_to_id[phone])]
      except:
        if phone!='':
          code=[int(phoneme_to_id['<unk>'])]
      sequence+=code
  else:
    sequence = [_symbol_to_id[symbol] for symbol in cleaned_text]
  return sequence


def sequence_to_text(sequence,chinese=True):
  '''Converts a sequence of IDs back to a string'''
  result = ''
  if chinese:
    for symbol_id in sequence:
      s = id_to_phoneme[str(symbol_id)]
      result += s
  else:
    for symbol_id in sequence:
      s = _id_to_symbol[symbol_id]
      result += s
  return result


def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    cleaner = getattr(cleaners, name)
    if not cleaner:
      raise Exception('Unknown cleaner: %s' % name)
    text = cleaner(text)
  return text

