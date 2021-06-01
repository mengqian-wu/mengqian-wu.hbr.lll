import sys, operator, os, string, re
import itertools




# BUILD THE WORKING ENVIRONMENT

# - 1: download python 
# - 2: download sublime for writting scripts  
# - 3: get your commander ready for running scripts. 
# - 4: the interpreter and an interactive shell: https://www.python-course.eu/python3_interactive.php
# - 5: windows system(commander)/OS system(terminal.app)  https://www.youtube.com/watch?v=M323OL6K5vs

# INSTALL MODULES 

# - play around with it, quit(), help>modules
# - what are modules? https://docs.python.org/3/tutorial/modules.html    
# - modules refer to a file containing Python statements and definitions. We use modules to break down large programs into small manageable and organized files. 

# dictionaries are like lists, except that:
#  - instead of a ORDERED sequence that you can access by it's number,
#  - the information is stored as unordered KEY-VALUE pairs
#   in the example below, the cities are the KEYS, and the populations are the VALUES

   # you define dicionaries with squiggly brackets
   # KEYS are always before a colon, and VALUES are going after a colon. 
na_city_populations_dict = {
    "Mexico City": 8918653,
    "New York City": 8550405,
    "Los Angeles": 3971883,
}





# For Bates Story20 Dataset
# 1. look into the raw data
# dictionary: file(story28) > each kid > sign_list , turn-taking 
# dict = {kid1：list1, count1, kid2:list2, count2, kid3: list3, count3...}

def build_dictionary(directory):
    story28_dict = {}
    story_list = os.listdir(directory)
    for story in story_list:
        story28_dict[story] = read_in_file(directory, story)
    return story28_dict

# open each session records and return a sign_list representing turn-taking agents. 
def read_in_file(directory, story):

    alphebet_list = []
    sign_list = []
    file_name = directory + '/' + story 
    f = open(file_name, 'r', encoding = 'UTF-8')
  
    for line in f:
        if line[0] == '*':
            alphebet_list.append(line[0:4])


    for item in alphebet_list:
        if item == '*MOT':
            item = 1
        else:
            item = -1
        sign_list.append(item)
    
    f.close()
   
    return sign_list

    
# python code to find number of total utterances, adult's utterances, and child's utterances, and turn-taking.

def count_variables(sign_list):
  
    n = len(sign_list)
    m = 0
    c = 0
    for item in sign_list:
        if item == 1:
            m += 1
        if item == -1:
            c += 1

    output = len(list(itertools.groupby(sign_list, lambda sign_list: sign_list >0)))
    turn_taking = output - 1

    return n, m, c, turn_taking

def count_dict(story28_dict):
    
    var_dict = {}
    for story in story28_dict:
        var_dict[story] = count_variables(story28_dict[story])

    return var_dict


def output_data(story28_dict, count_dict):

    print(10* ' ' + 'Num_Ut    Num_Mom    Num_Kid    TT')
     
    
    for i in story28_dict:
        result = str(count_dict[i]).ljust(10)
        output_string = i + '     ' + result
        print(output_string)


def main():
    input_directory = sys.argv[1]
    story28_dict = build_dictionary(input_directory)
    #print(story28_dict)
    
    var_dict = count_dict(story28_dict)
    output_data(story28_dict, var_dict)

main()


