# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def num_lines_words (file_path):
    with open(file_path) as file:
        file_str = file.read()
        lines = file_str.splitlines()

        words = file_str.split()       

        print(f"Number of lines : {len(lines)}, numbers of words : {len(words)}")

#num_lines_words("C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/obama_speech.txt")

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages (file_path, number_of_languages):
    import json
    with open(file_path, encoding="utf-8") as file:
        data = json.loads(file.read())

    counts = dict()
    for country in data:
        for language in country["languages"]:
            counts[language] = counts.get(language, 0) + 1

    li_languages = sorted(counts.items(), key=lambda language: language[1], reverse=True)
    for i in range(number_of_languages):
        print(li_languages[i])

#most_spoken_languages("C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/countries_data.txt", 3)

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries (file_path, number_of_countries):
    import json
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

    data = sorted(data, key= lambda x: x["population"], reverse=True)
    for i in range(number_of_countries):
            print(f"Country : {data[i]['name']}, Population : {data[i]['population']}")

#most_populated_countries("C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/countries_data.txt", 3)

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
with open("C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/email_exchanges_big.txt") as file:
    file_str = file.read()
email_regex = r"[a-zA-Z0-9\._-]+@[a-zA-Z0-9\._-]+"
from_lst = re.findall(r"from.*\n", file_str, re.I)
email_lst = []
for line in from_lst:
    email_lst.extend(re.findall(email_regex, line))
#print(set(email_lst))

# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters
# - a string or a file and a positive integer, indicating the number of words.
# Your function will return an array of tuples in descending order. Check the output
def find_most_common_words (file_path, number_of_words):
    with open(file_path) as file:
        file_str = file.read().lower()

    words = re.findall(r"\w+", file_str)       
    top_words = dict()
    for word in words:
        top_words[word] = top_words.get(word, 0) + 1
    top_words = sorted(top_words.items(), key= lambda x: x[1], reverse=True)

    return top_words[:number_of_words]
#print(find_most_common_words("C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/obama_speech.txt", 4))

# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
# For instance check the similarity between the transcripts of Michelle's and Melina's speech.
# You may need a couple of functions, function to clean the text(clean_text),
# function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
def clean_text (file_path):
    with open(file_path) as file:
            file_str = file.read().lower()
    
    return re.findall(r"\w+", file_str)

def remove_support_words (words_lst):
    stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"}
    words_lst_removed = [word for word in words_lst if word not in stop_words]
    return words_lst_removed

def check_text_similarity (file_path1, file_path2):
    text1 = remove_support_words(clean_text(file_path1))
    text2 = remove_support_words(clean_text(file_path2))

    text1_top_words = dict()
    for word in text1:
        text1_top_words[word] = text1_top_words.get(word, 0) + 1

    text2_top_words = dict()
    for word in text2:
        text2_top_words[word] = text2_top_words.get(word, 0) + 1

    words_in_common = 0
    all_words = 0
    for key in text1_top_words:
        words_in_common += min(text1_top_words[key], text2_top_words.get(key, 0))
        all_words += text1_top_words[key]
    for key in text2_top_words:
            all_words += text2_top_words[key]
    return words_in_common / all_words * 100

print(check_text_similarity("C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/melina_trump_speech.txt", "C:/Users/Bryan/Desktop/Stage/Suisse/30DaysOfPython/repo/day_19/michelle_obama_speech.txt"))
    