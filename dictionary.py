import requests

class Phonetic():
  def __init__(self, word = ""):
    self.api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    self.word = word
    self.phon = "Not yet found"

  def get(self):
    r = requests.get(self.api_url)
    self.phon = " "
    if not self.word == '':
      self.phon = r.json()
      if not 'title' in self.phon:
        if 'phonetic' in self.phon[0] and self.phon[0]['phonetic']:
          self.phon = self.phon[0]['phonetic']
        elif 'phonetics' in self.phon[0] and self.phon[0]['phonetics']:
          if 'text' in self.phon[0]['phonetics']:
            self.phon = self.phon[0]['phonetics'][1]['text']
          else:
            self.phon = self.word
        else:
          self.phon = self.word
      else:
        self.phon = self.word
      buf = ""
      for char in self.phon:
        if not char == "/":
          buf += char
      self.phon = buf
    return self.phon

  def __str__(self):
    return self.phon