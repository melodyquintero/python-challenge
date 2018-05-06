
# Import Modules for Reading Data
import os

# Set path for file
textpath = os.path.join('raw_data','paragraph_1.txt')

# Open and read the file as string
Paragragh = open(textpath, 'r').read()

# List all the words in the paragragh by seperating space
Words = Paragragh.split(" ")

# List all the sentences in the paragragh by seperating "."/"!"/"?"
import re
Sentence = re.split(r'[.!?]+', Paragragh)

# Count the words
Word_Count = len(Words)

# Count the sentence
Sentence_Count = len(Sentence)-1

# Calculate the avarage letters number by summing up the number of letters in each words 
Average_Letter_Count = sum([len(letters) for letters in Words])/Word_Count

# Calculate the avarage sentence length
Average_Sentence_Length = Word_Count/Sentence_Count

# print the results
print("Paragraph Analysis")
print("-"*20)
print("Approximate Word Count: "+str(Word_Count))
print("Approximate Sentence Count: "+str(Sentence_Count))
print("Average Letter Count: "+str(Average_Letter_Count))
print("Average Sentence Length: "+str(Average_Sentence_Length))

# Export the results in text
with open("Paragragh_Analysis.txt", "w+") as f:
    f.write("Paragraph Analysis"+"\n")
    f.write("-"*20+"\n")
    f.write("Approximate Word Count: "+str(Word_Count)+"\n")
    f.write("Approximate Sentence Count: "+str(Sentence_Count)+"\n")
    f.write("Average Letter Count: "+str(Average_Letter_Count)+"\n")
    f.write("Average Sentence Length: "+str(Average_Sentence_Length)+"\n")
    f.close()



