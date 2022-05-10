import tronald
import dictionary

def main():
  t = tronald.TronaldDump()
  quote = t.get()
  q = phoneticQuote(quote)

  print("Donald Trump Quote:\n",t.quote,"\n")
  print("Phonetic Pronunciation of Donald Trump quote:\n",q)

def phoneticQuote(quote_list = []):
  buf = ""
  for word in quote_list:
    q = dictionary.Phonetic(word)
    q = q.get()
    buf += q
    buf += " "
  return buf
    
main()