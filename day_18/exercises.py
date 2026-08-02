import re
#What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
para_splited = re.split(" |\\.", paragraph)

result_dict = dict()

for word in para_splited:
    result_dict[word] = 0
for word in para_splited:
    result_dict[word] += 1

result_tuple = sorted(result_dict.items(), key= lambda x : x[1], reverse=True)
#print(result_tuple[0])

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction,
# 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance
# between the two furthest particles.

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

points = re.findall("-?\\d+", text)
points_integer = [int(number) for number in points]
distance = max(points_integer) - min(points_integer)


# Write a pattern which identifies if a string is a valid python variable

def is_valid_variable (variable_name):
    patern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    if re.match(patern, variable_name) == None:
        return False
    return True

print(is_valid_variable('first_name'), # True
is_valid_variable('first-name'), # False
is_valid_variable('1first_name'), # False
is_valid_variable('firstname') # True
)

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_sentence = re.sub("[^A-Za-z0-9,\\. ]", "", sentence)
splited_sentence = re.split("[ \\.,]", clean_sentence)
result_dict = dict()
for word in splited_sentence:
    result_dict[word] = 0
for word in splited_sentence:
    result_dict[word] += 1
del result_dict[""]
result_lst = result_dict.items()
result_lst = sorted(result_lst, key = lambda x : x[1], reverse=True)
print(result_lst[:3])