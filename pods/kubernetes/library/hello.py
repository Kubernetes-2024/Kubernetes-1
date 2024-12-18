import requests
import re

url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)
html_content  = response.text
cleaned_text = re.sub('<[^<]+?>', ' ',html_content)
words = re.findall(r'\b\w+\b', cleaned_text)

def has_unique_char_words(word):
    return re.match(r'^(?!)')

longest_word = ""
for word in words:
    if has_unique_char_words(word) and len(word) > len(longest_word)
        longest_word = word
if longest_unique_word:
    print(f"the longest word is  {longest_word}")
else:
    print("no words in url")
