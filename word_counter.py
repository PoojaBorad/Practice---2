print("Create a program that takes a paragraph of text as input and counts the frequency of each word.")

def count_word_frequency(text):
    #split text into words!
    words = text.split()

    #create an empty dictionary for words:
    word_frequency = {}

    #starting with for loop:
    for word in words:
        word = word.strip(".,!;:|/?\"'()[]{}").lower()
        

        #now using if statement:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    #At the end ask for return.        
    return word_frequency        

paragraph = input("Write a paragraph of text: ")

frequency_dict = count_word_frequency(paragraph)

print("Words frequencies: ")

for word, frequency in frequency_dict.items():
    print(f"{word} : {frequency}")


                  
                








