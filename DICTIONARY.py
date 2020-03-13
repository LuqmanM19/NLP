# -*- coding: utf-8 -*-

f = open('recipe_Ital_115.txt','r')	#opens the file object "recipe_Ital_115.txt", commonly takes two arguments: open(filename, mode)

words = f.read()	#reads the entire content of a file or some quantity of data and stores it in words

d ={}	#creates an empty dictionary

for word in words.split():    
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

print("\nDictionary that defines each unique word and its frequency in recipe_Ital_115.txt:\n",d)
               
frequency_of = d['of']     

print("\n\nHow many times does the word 'of' occur in recipe_Ital_115.txt?:\n",frequency_of)

li = []

print("\n\nWords in recipe_Ital_115.txt that end with 'ly':")
for word in words.split():
         if word.endswith("ly"):
            print(word)
            li.append(word)

print(li)


f = open('results.txt', 'w')
f.write("\nDictionary that defines each unique word and its frequency in recipe_Ital_115.txt:\n")
s= str(d)
f.write(s)
f.write("\n\nHow many times does the word 'of' occur in recipe_Ital_115.txt?:\n")
s=str(frequency_of)
f.write(s)
f.write("\n\nWords in recipe_Ital_115.txt that end with 'ly':")
s=str(li)
f.write(s)
f.close

#        print('results.txt', results.txt, file=f)