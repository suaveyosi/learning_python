def count_words(A,n):
  '''return a list with the words wich lenght is greather than n'''
  result=[word for word in A if len(word)>n]
  return result
words=["hola","que","tal","a"]
print(len(words[0]))
print(count_words(words,2)) 