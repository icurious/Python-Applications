import json
from difflib import get_close_matches

#import json data in python dict
data = json.load(open("data.json"))

#function to return meaning of a word
def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys(),n=1, cutoff = 0.8)) > 0:   #checks for similar words in Dictionary
        similar = get_close_matches(word,data.keys())[0]
        yn = input("Did you meant %s instead? Enter (Y/N): "%(similar))
        if yn.lower() == "y":
            return data[similar]
        elif yn.lower() == "n":
            return "Word doesnt exists in the Dictionary.Please Double check"
        else:
            return "We didnt understand your entry."



    else:
        return "Word doesnt exists in the Dictionary.Please Double check"



#take word from user and print result
word = input("Enter Word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
