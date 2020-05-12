#!/usr/bin/env python
# coding: utf-8

# In[26]:


import json
from difflib import get_close_matches
data = json.load(open("data.json"))


# In[39]:


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        ans = input("Did you mean %s insted? Enter Y if Yes or N if No: " %get_close_matches(word,data.keys())[0])
        if ans == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ans =="N":
            return "Word doesn't exist please check the word again."
        else:
            return "We doesn't understand your entry."
    else:
        return "Word doesn't exist please check the word again."


# In[40]:


word = input("Enter the word you want to search: ")

output = search(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

