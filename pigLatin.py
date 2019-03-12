#pig latin = funny language simulator
#get sentence from user
original = input("Enter the sentence you want to translate: ").strip().lower()

#split sentence into words
words = original.split()

#loop through the words and convert to piglaatin
new_words = []
#starts with vowel just add 'yay'
#otherwise move first consonant cluster and move to end,andd 'ay'
for word in words:
    if word[0] in "aeiou":
        new = word+"yay"
        new_words.append(new)
    else:
        vowel_pos =0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos+1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        new = rest + cons + "ay"
        new_words.append(new)

#put the words back to sentence
output = " ".join(new_words)

#print
print(output)
