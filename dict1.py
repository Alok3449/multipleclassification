# my_dict={}
# print(type(my_dict))
# key=['Name','Age','City']
# values=['Alok',19,'Varenasi']
# #my_dict={'Name':"Alok",'Age':19,'City':'Varanasi'}
# new_dict={key:values for (key,values) in zip(key,values)}
# print(new_dict)
# print(my_dict)


# import string


# def word_frequency(text):

#     text = text.lower()
#     text = text.translate(str.maketrans('', '', string.punctuation))
#     words = text.split()

#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1

#     return freq


# input_text = "Hello world. Hello Python."
# print(word_frequency(input_text))


# def char_frequency(word):
#     word = word.lower()  # optional: ignore case
#     freq = {}

#     for char in word:
#         freq[char] = freq.get(char, 0) + 1

#     return freq


# # Example usage:
# word = "Python ppp"
# result = char_frequency(word)
# print(result)


# dict1 = {'a': 10, 'b': 20}
# dict2 = {'b': 30, 'c': 40}

# merged_dict = {}

# # Add all items from dict1
# for key in dict1:
#     merged_dict[key] = dict1[key]

# # Add items from dict2
# for key in dict2:
#     if key in merged_dict:
#         merged_dict[key] += dict2[key]  # sum values if key exists
#     else:
#         merged_dict[key] = dict2[key]

# print(merged_dict)

# d={}
# d["Dhoni"]="Keeper"
# d["Virat"]="Batsman"

# data=d.get("Amitabh","Not Found")
# print(data)

# word="Alok"

# lettersfrequency={}

# for ch in word:
#     lettersfrequency[ch]=1+lettersfrequency.get(ch,0)

# print(lettersfrequency)


# for key,value in lettersfrequency.items():
#     print(key,value)

def count_vowels_consonants(sentence):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    # Convert to lowercase to handle case-insensitive comparison
    sentence = sentence.lower()

    for char in sentence:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count 

# Example usage
sentence = "Jack and Jill went up the hill."
vowels, consonants = count_vowels_consonants(sentence)
print("Vowels:", vowels)
print("Consonants:", consonants)



vowel=("a","e","i","o","u")
#consonent=("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
def read_vowels_and_consonenta_in_paragraph():
    paragraph = input("Enter a paragraph: ")
    vowels_count = 0
    consonents_count = 0
    for char in paragraph:
        if char in vowel:
            vowels_count += 1
        #elif char in consonent:
        else:
            
            consonents_count += 1
    print("Number of vowels:", vowels_count)
    print("Number of consonents:", consonents_count)
read_vowels_and_consonenta_in_paragraph()




def count_frequencies(numbers):
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict

# Example usage:
input_list = [1, 2, 2, 3, 4, 4, 4]
result = count_frequencies(input_list)
print(result)  # Output: {1: 1, 2: 2, 3: 1, 4: 3}
