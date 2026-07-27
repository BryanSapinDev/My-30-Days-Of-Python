#Write a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id ():
    all_char = string.ascii_letters + string.digits
    result_id = ""
    for i in range(6):
        result_id += all_char[random.randint(0, len(all_char)-1)]
    return result_id

#Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import sys
def user_id_gen_by_user ():
    all_char = string.ascii_letters + string.digits
    id_lst = []
    for id in range(int(sys.argv[1])):
        result_id = ""
        for char_index in range(int(sys.argv[2])): 
            result_id += all_char[random.randint(0, len(all_char)-1)]
        id_lst.append(result_id)
    return id_lst
#Result
#python exercises.py 5 6
#['KdYa1J', 'qD4QsJ', 'tNP8dO', 'GtD2Iq', 't0OugI']

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen ():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return f"rgb({red},{green},{blue})"

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors (number_of_colors):
    result_lst = []
    all_char = "0123456789abcdef"
    for color in range(number_of_colors):
        result_color = "#"
        for char_index in range(6):
            result_color += all_char[random.randint(0,len(all_char)-1)]
        result_lst.append(result_color)
    return result_lst

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors (number_of_colors):
    result_lst = []
    for color in range(number_of_colors):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        result_lst.append(f"rgb({red},{green},{blue})")
    return result_lst

#Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors (colors_type, number_of_colors):
    result_lst = []
    if colors_type == "hexa":
        all_char = "0123456789abcdef"
        for color in range(number_of_colors):
            result_color = "#"
            for char_index in range(6):
                result_color += all_char[random.randint(0,len(all_char)-1)]
            result_lst.append(result_color)
    elif colors_type == "rgb":
        for color in range(number_of_colors):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            result_lst.append(f"rgb({red},{green},{blue})")
    else:
        return "Wrong type of colors"
    
    return result_lst

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuflle_list (lst_to_shuffle):
    result_lst = []
    for i in range(len(lst_to_shuffle)):
        result_lst.append(lst_to_shuffle.pop(random.randint(0,len(lst_to_shuffle)-1)))
    return result_lst

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_numbers ():
    result_lst = list()
    all_digits = list(string.digits)
    for i in range(7):
        result_lst.append(all_digits.pop(random.randint(0,len(all_digits)-1)))
    return result_lst
print(seven_random_numbers())
