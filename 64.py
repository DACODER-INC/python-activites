def match_words(words):
   ctr = 0
   ojvofj = []
   for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
      ojvofj.append(word)
   print('list of words with same 0 and -1 character',ojvofj )
   return ctr
count = match_words(['abc ', 'cfc' , 1221, 'aba', 132])
print(count)

