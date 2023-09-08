def madlib():
  words = []
  article = input("Article: ")
  fadjective = input("Adjective: ")
  sadjective = input("Adjective: ")
  fnoun = input("Noun: ")
  snoun = input("Noun: ")
  fverb = input("Verb: ")
  preposition = input("Preposition: ")
  words.append(article + " " + fadjective + " " + fnoun + " " + fverb + " " + article)
  words.append(sadjective + " " + snoun + " " + preposition + " " + article + " " + sadjective + " " + fnoun)
  sentence = " ".join(words)
  print(sentence)

madlib()
