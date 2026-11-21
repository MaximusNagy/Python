import string
sentence = input("\nPlease type a sentence: ")
new_sentence = ""
for x in sentence:
    if x not in string. punctuation:
        new_sentence += x
print("\n\n *** Here is the same sentence without punctuation **** \n\n", new_sentence)