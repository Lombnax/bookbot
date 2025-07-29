
# Counting all words
def word_count(text):
    list_of_words = text.split()
    counting_of_words = len(list_of_words)
    return counting_of_words
    
# Counting all characters
def character_count(text):
    dictionary = {}
    for char in text.lower():
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary

# Sorting Dictionarys
def sorting(dictionary):
    list = [] #Empty list.
    for key in dictionary: #Iterating over key & value.
        value = dictionary[key]
        new_dict = {"char": key, "num": value} #Puts them in a new dictionary as one value.
        list.append(new_dict) #appends to a list since append only sends one value.

    def sort_on(item): #noe jeg ikke vet hva gjør, må være her for at .sort skal funke.
        return item["num"]

    list.sort(reverse=True, key=sort_on) #takes list of dictionaries and sorts them with < command, then returns it.
    return list


            








