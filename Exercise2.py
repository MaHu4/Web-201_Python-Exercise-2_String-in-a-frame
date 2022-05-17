# to runn Python file in terminal --> go to specific folder and then type "python3 + "class name" --> python3 class2.py OR
# /Users/marenhuser/Frauenloop/2.WebDev_Intermediate/Python /class2.py
# Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

# *********
# * Hello *
# * World *
# * in    *
# * a     *
# * frame *
# *********

# ## Solurtion 1.1.: My own solution - manually
# myList = ["Hello", "World", "in", "a", "frame"] 
# print("*********")
# print("* " + myList[0] + " *")
# print("* " + myList[1] + " *")
# print("* " + myList[2] + "    *")
# print("* " + myList[3] + "     *")
# print("* " + myList[4] + " *")
# print("*********")

# ## Solution 1.2.: Theresa's solution - manually with right distance for each word

# FrameContentList = ["Circle", "in", "a", "frame"]
# TopBottomFrame = ('**********') # 10x *

# print(TopBottomFrame)
# print('* ' + FrameContentList[0] + ' *') # 6-character-word 
# print('* ' + FrameContentList[1] + ' ' + ' ' + ' ' + ' '+ ' *') # 2-character-word --> spaces on right seide adapted
# print('* ' + FrameContentList[2] + ' ' + ' ' + ' ' + ' '+ ' '+ ' *') # 1-character-word --> spaces on right seide adapted
# print('* ' + FrameContentList[3] + ' '+ ' *')

# print(TopBottomFrame)

# ##Solution 2.1:  found at https://codereview.stackexchange.com/questions/128744/print-list-items-in-a-rectangular-frame

    #Function definition:
        # Function header: Keyword "def" marks the start + function name to uniquely identify the function + Parameters (arguments) through which we pass values to a function + colon (:) to mark the end of the function header
        # Function body: One or more valid python statements which must have the same indentation level (usually 4 spaces).
        # Return statement (optional) to return a value from the function.
    # Call a function

# def print_in_a_frame(*words): # only works with *, indicating that the number of arguments is unknown
#     size = max(len(word) for word in words)
#     print('*' * (size + 4)) # upper line with 
#     for word in words:
#         print('* {:<{}} *'.format(word, size)) # = print('* {a:<{b}} *'.format(a=word, b=size)), this tells format to print the keyword argument a (word), left-aligned, on a field of total width the keyword argument b; longest word a as min.
#     print('*' * (size + 4))  # bottom line with 

# print_in_a_frame("Hello", "Kathmandu", "in", "a", "box") # call of function: function name + parenthesis, incl. parameters within " ":



# ## Solution 2.2:  found at https://codereview.stackexchange.com/questions/128744/print-list-items-in-a-rectangular-frame
# def print_in_a_frame(*words):
#     size = len(max(words, key=len)) # different line compared to solution 2.1
#     print('*' * (size + 4))
#     for word in words:
#         print('* {:<{}} *'.format(word, size)) # = print('* {a:<{b}} *'.format(a=word, b=size))
#     print('*' * (size + 4))

# print_in_a_frame("Hello", "Kathmadnu", "in", "a", "box")


# ## Solution 3: 

# def print_in_a_frame(words, borderchar = '*'):
#     size = max(len(word) for word in words)
#     print(borderchar * (size + 4))
#     for word in words:
#         print('{bc} {:<{}} {bc}'.format(word, size, bc = borderchar))
#     print(borderchar * (size + 4))

# print_in_a_frame("Hello, Lumbini in a frame".split()) # .split ensures that one entire word per line is printed; without split-function, it would print oee charachter/letter per line

# #Changes text and frame
# print_in_a_frame("Hello, Lumbini in a frame".split(), '+')
# print_in_a_frame("Hello, Lumbini in a frame".split(), ':')

# ## Solution 4.1: Theresa's automated1
# FrameContentList = ["Circle", "in", "a", "frame", "without", "distance"]
# TopBottomFrame = ('**********')

# print(TopBottomFrame)

# for word in FrameContentList:
#     print('* ' + word + ' *')

# print(TopBottomFrame)

## Solution 4.2.: Theresa's automated 2
    # the function should 
        # 1. take the first item out of the list
        # 2. count the word length
        # 3. substract it from 6 (e.g. 10 stars - (first star + space) - (space + last star))
        # 4. remainder is number of spaces after word
        # 5. set variable space = ' '
     
# FrameContentList = ["Circle", "in", "a", "frame", "with", "the", "right", "distance"] #max 6-letter words!
# TopBottomFrame = ('************')
# spaceAfterWord = (' ')

# print(TopBottomFrame)

# for word in FrameContentList:
#     print('* ' + word + (8-len(word))*spaceAfterWord + ' *')

# print(TopBottomFrame)


# ## Solution 5: Theresa's complete automation

# # Frame with complete automation: op line orients itself on longest word in the list and adds 4

# # defines variables:
# FrameContentList = ["Circle", "in", "a", "frame", "with", "supervariable", "distance"] #no limit
# singleStar = ('*')
# spaceAfterWord = (' ')
# countLetters = len(max(FrameContentList, key=len)) # finds longest word/string based on length with max() and key, len() converts into int
# TopBottomFrame = ((countLetters + 4) * singleStar) # determines length of top and bottom line by taking number of longest word, adding 4 digits (for beginning and end + 1 space each )

# print(TopBottomFrame)

# for word in FrameContentList:
#     print('* ' + word + (countLetters - len(word)) * spaceAfterWord + ' *') # takes each item/ word of the list and puts it between the stars together with the corresponding spaces to make the vertical end line even

# print(TopBottomFrame)

# ### "word" can be exchanged by "i" ###
# FrameContentList = ["Circle", "in", "a", "frame", "with", "supervariable", "distance"]
# singleStar = ('*')
# spaceAfterWord = (' ')
# countLetters = len(max(FrameContentList, key=len))
# TopBottomFrame = ((countLetters + 4) * singleStar) 

# print(TopBottomFrame)

# for i in FrameContentList:
#     print('* ' + i + (countLetters - len(i)) * spaceAfterWord + ' *')

# print(TopBottomFrame)
