import requests

class TronaldDump():
  def __init__(self):
    self.api_url = "https://api.tronalddump.io/random/quote"
    self.quote = "Not yet found"
    self.quote_list = ["Not","yet","found"]

  def get(self):
    r = requests.get(self.api_url)
    self.quote = r.json()
    buf = ""
    for char in self.quote['value']:
      if char.isalnum() or char == " ":
        buf += char
    self.quote = buf
    self.quote_list = self.quote.split(" ")
    
    return self.quote_list

  def __str__(self):
    return f"Random Donald Trump Quote: {self.quote}"

  