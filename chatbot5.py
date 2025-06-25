import tkinter as tk
from tkinter import messagebox
import random
import time
import re
from sklearn.linear_model import LinearRegression as lp
from PIL import Image
import openai as ai
import math as m
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
from datetime import datetime as dt
import datetime as d
welcome_messages = [
    "Hello! How can I assist you today?",
    "Hi there! What can I do for you?",
    "Greetings! How may I help you?",
    "Hey! What do you need help with?",
    "Welcome! How can I be of service?",
    "Hi! How can I assist you today?",
    "Hello! What can I help you with?",
    "Greetings! How can I assist you?",
    "Hey there! What do you need help with?",
    "Welcome! How may I assist you today?"
]
impossibility_replies = [
    "I'm sorry, that's not possible.",
    "Unfortunately, I am not integrated to that level yet.",
    "That task is beyond my capabilities.",
    "I'm afraid I can't help with that.",
    "That request is impossible for me to fulfill.",
    "I wish I could, but I do not have answer to that.",
    "Sorry, I don't have the ability to do answer that.",
    "I'm unable to perform that action.",
    "Sorry please try something more simpler.",
    "I'm sorry, but I can't assist with that."
]
scatter_plot = [
    "scatter graph",
    "scatter chart",
    "scatter diagram","pointed plot","pointed graph",
    "point plot","point graph",
    "scatter plot","scattered plot",
    "dot graph",
    "dot plot",
    "point cloud graph",
    "scattergram",
    "bubble chart",
    "bubble graph",
    "dotted chart",
    "dotted plot",
    "dotted graph","scattered graph"
]
pie_chart = ["pie graph", "circle chart","pie chart", "sector chart", "donut chart", "ring chart", "wedge chart"]

songs = {
    "Imagine": [
        "Imagine there's no heaven",
        "It's easy if you try",
        "No hell below us",
        "Above us only sky",
        "Imagine all the people living for today"
    ],
    "Bohemian Rhapsody": [
        "Is this the real life?",
        "Is this just fantasy?",
        "Caught in a landslide",
        "No escape from reality",
        "Open your eyes, look up to the skies and see"
    ],
    "Hey Jude": [
        "Hey Jude, don't make it bad",
        "Take a sad song and make it better",
        "Remember to let her into your heart",
        "Then you can start to make it better"
    ],
    "Hotel California": [
        "On a dark desert highway, cool wind in my hair",
        "Warm smell of colitas, rising up through the air",
        "Up ahead in the distance, I saw a shimmering light",
        "My head grew heavy and my sight grew dim",
        "I had to stop for the night"
    ],
    "Stairway to Heaven": [
        "There's a lady who's sure all that glitters is gold",
        "And she's buying a stairway to heaven",
        "When she gets there she knows, if the stores are all closed",
        "With a word she can get what she came for",
        "Ooh, ooh, and she's buying a stairway to heaven"
    ],
    "Let It Be": [
        "When I find myself in times of trouble",
        "Mother Mary comes to me",
        "Speaking words of wisdom, let it be",
        "And in my hour of darkness",
        "She is standing right in front of me"
    ],
    "Yesterday": [
        "Yesterday, all my troubles seemed so far away",
        "Now it looks as though they're here to stay",
        "Oh, I believe in yesterday",
        "Suddenly, I'm not half the man I used to be",
        "There's a shadow hanging over me"
    ],
    "Smells Like Teen Spirit": [
        "Load up on guns, bring your friends",
        "It's fun to lose and to pretend",
        "She's overboard and self-assured",
        "Oh no, I know a dirty word",
        "Hello, hello, hello, how low"
    ],
    "Billie Jean": [
        "She was more like a beauty queen from a movie scene",
        "I said don't mind, but what do you mean I am the one",
        "Who will dance on the floor in the round",
        "She said I am the one",
        "Who will dance on the floor in the round"
    ],
    "Like a Rolling Stone": [
        "Once upon a time you dressed so fine",
        "You threw the bums a dime in your prime, didn't you?",
        "People'd call, say, 'Beware doll, you're bound to fall'",
        "You thought they were all kiddin' you",
        "You used to laugh about everybody that was hangin' out"
    ]
}
passive_replies = [
    "Do as you please.",
    "Whatever works for you.",
    "It's up to you.",
    "Feel free to decide.",
    "Do what you think is best.",
    "Go ahead, it's your choice.",
    "Whatever you prefer.",
    "Do what you like.",
    "It's your call.",
    "You decide."
]
calculation_replies = [
    "The result is {}.",
    "After calculating, I found the answer to be {}.",
    "The answer to your calculation is {}.",
    "The final result is {}.",
    "Here's the result: {}.",
    "The calculation gives us {}.",
    "The computed answer is {}.",
    "The outcome of the calculation is {}.",
    "The result after calculation is {}."
]
search_replies = [
    "I don't have the answer to that, but I searched the web and found this:",
    "I'm not sure about that, but here's what I found on the web:",
    "I couldn't answer that directly, but I found this information online:",
    "I don't have the exact answer, but here's what I found from my web search:",
    "I couldn't provide an answer, but I found this on the web:",
    "I don't have the information, but here's what I found online:",
    "I'm not certain, but I searched the web and found this:",
    "I don't have the answer, but here's what I found from a web search:",
    "I couldn't answer that, but here's some information I found online:",
    "I don't have the exact answer, but here's what I found on the internet:"
]
link_replies = [
    "Here is the link:",
    "Check out this link for more:",
    "Here's the link for it:",
    "This link might give you further insight:",
    "Take a look at this link:",
    "You can view it this link for more details:",
    "Follow this link:",
    "Here's the URL:",
    "Click on this link to see more:"
]
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "magenta", "pink", "brown", "black", "white", "grey", "teal", "lime"]
bar_chart = [
    "histogram",
    "column chart",
    "bar graph",
    "block chart",
    "bar chart",
    "bar diagram",
    "vertical bar chart",
    "horizontal bar chart",
    "comparative bar graph",
    "grouped bar chart",
    "stacked bar chart",
    "bar plot",
    "data bars",
    "proportional bar graph",
    "chart with bars",
    "rectangular graph"
]
greetings = [
    "hi", "hello", "hey","heyyo","howdy", "greetings", "salutations", "what's up", "good day", "hiya", "yo","yooo","yoo", "how's it going", 
    "how are you", "howdy-do", "hey there", "hi there", "hello there", "good morning", "good afternoon", "good evening", "what's up", "what's popping",
    "sup", "what's happening", "what's new", "what's good", "what's going on", "how's everything", "how's life", "how far",
    "how's your day", "how's your day going", "how have you been", "how do you do", "nice to meet you", "pleased to meet you"
]
digit_pattern = r"\d+"
space = r"\s*"
passive = ["should i","could i","can i","may i","be sure to","am i allowed to","am i permitted to","can"]
calculation = ["calculate","+","-","*","/","divide","multiply","!","find","add","subtract","sum","product","quotient","minus","plus","total","remainder"]
add =  ["+","add","sum","plus","total number"]
divide  = ["/","divide","division","divided", f"divide {digit_pattern} by","quotient",f"quotient {digit_pattern}{space},{space}{digit_pattern}"]
modulus = ["%", "modulus", "remainder","mod","modulo"]
multiply = ["*", "multiply", "product", "times"]
factorial = ["factorial", "factorial of", f"fact of {digit_pattern}", f"{digit_pattern}!"]

combination = ["combination", "arrangement", "combination of", "arrangement of", "comb", "comb of", "c(","c ("]
permutation = ["permutation", "arrangement", "permutation of", "arrangement of", "perm", "perm of","p(", "p ("]
subtract = ["-", "subtract from", "minus","difference of" ]
square = ["square","^2","**2", "square of" , "squared","to the power of two","to power two" ,"to power 2","raise to the power of 2", "raise to the power of two"]
cube = ["cube", "cube of", "cubed", "raise to the power of 3", "raise to the power of three", f"{digit_pattern} cubed", f"{digit_pattern} cube", f"{digit_pattern}^3"]
square_root = ["square root", "root", "sqrt", "square root of", "find the square root of", "square root of", "root of"]
search = ["search", "find","who","when", "look up", "google", "google search", "search for", "look for", "find out", "look up for", "search up", "search on google"]
cube_root = ["cube root", "cbrt of", "cube root of", "find the cube root of", "cube root of", "cbrt", "^1/3"]
sine = ["sine", "sin", "sine of", "sin of", "find the sine of", "sine of"]
cosine = ["cosine", "cos", "cosine of", "cos of", "find the cosine of", "cosine of"]
tan = ["tan", "tangent", "tan of", "tangent of", "find the tan of", "tan of"]
cot = ["cot", "cotangent", "cot of", "cotangent of", "find the cot of", "cot of"]
sec = ["sec", "secant", "sec of", "secant of", "find the sec of", "sec of"]
cosec = ["cosec", "cosecant", "cosec of", "cosecant of", "find the cosec of", "cosec of","csc of"]
image = ["image", "show me an image of", "display the image", "picture","open he image", "photo","open an image","image of", "show me a picture of", "show me a photo of"]
graph = ["graph", "plot", "plot a graph of","chart", "draw a graph of", "draw a plot of", "plot a graph for", "draw a graph for", "draw a plot for"]
edit_image = ["edit", "edit an image of", "edit a picture of", "edit a photo of", "edit image", "edit picture", "edit photo"]
file = ["open file","open a file","extract this file","open the file"]
def img(x):
         woors = re.search(r"[a-zA-Z0-9-_.()]+\.png|[a-zA-Z0-9-_.()]+\.jpeg|[a-zA-Z0-9-_.()]+\.jpg",x)
         image_file = woors.group()
         image = Image.open(image_file)
         image.show()
         image.close()
def open_file(x):
        file_match = re.findall(r"[a-zA-Z0-9-_.]+\.html|[a-zA-Z0-9-_.]+\.txt|[a-zA-Z0-9-_.]+\.py|[a-zA-Z0-9-_.]+\.csv",x)
        real_file = str(file_match[0])
        open_file = open(real_file,"r+")
        the_file = open_file.read()
        messagebox.showinfo(real_file,the_file)

# Chatbot main brain(where the main response comes from)
def chatbot_response(user_input):
     user_input = user_input.lower()
     global impossibility_replies
     try:
        if any(word in user_input for word in image):  
         img(x=user_input) 
         return "Bot:  Your Image was just displayed"
        elif any(word in user_input for word in file):
           open_file(x= user_input)
           return "Bot:  showed"
        elif "what is your name"in user_input or "who are you" in user_input or "what's your name" in user_input:
           return "Bot:  I'm just a simple chatbot named ALGEBOT"
        elif "how are you" in user_input:
            return"Bot:  I'm just a chatbot,I don't have feelings but thanks for asking"
        elif any(word in user_input for word in passive):
            return f"Bot:  {random.choice(passive_replies)}"
        elif any(word in user_input for word in greetings):
           return f"Bot:  {random.choice(welcome_messages)}"
        elif any(word in user_input for word in sine) and any(word in user_input for word in cosine) and any(word in user_input for word in tan) and any(word in user_input for word in cot) and any(word in user_input for word in sec) and any(word in user_input for word in cosec):
            return"Bot:  I'm sorry, I can only calculate one trigonometric function at a time"
        elif any(word in user_input for word in graph):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                x = []
                y = []
                digit_lenght = len(digits)
                half = digit_lenght / 2
                for i in range(int(half)):
                    x.append(int(digits[i]))
                for i in range(int(half),len(digits)):
                    y.append(int(digits[i]))
                if any(word in user_input for word in bar_chart):
                    plt.bar(x,y,color = random.choice(colors))
                    plt.show() 
                    return"Bot:  Here is your bar chart"
                elif any(word in user_input for word in scatter_plot):
                    plt.scatter(x,y, color = random.choice(colors))
                    plt.show()
                    return "Bot: Here is your scatter plot"
                elif any(word in user_input for word in pie_chart):
                    digits = list(map(int, re.findall(r'\d+', user_input)))
                    labels = [f"label {i+1} for angle {digits[i]}o" for i in range(len(digits))]
                    sum_digits = sum(tuple(digits))
                    first_angle = int(((digits[0])/sum_digits)*360)
                    plt.pie(digits, labels=labels, autopct="%1.2f%%", startangle=first_angle)
                    plt.show()
                    return "Bot: Here is your pie chart"

                else:
                    plt.plot(x,y, color = random.choice(colors))
                    plt.show()
                    return"Bot:  Here is your line graph"
        elif any(word in user_input for word in sine) and any(word in user_input for word in add):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                add_list = []
                for digit in digits:
                    digit = int(digit)
                    add_list.append(digit)
                    add_tuple = tuple(add_list)
                final_add = sum(add_tuple)
                ans = m.sin(m.radians(final_add))
                final_answer = random.choice(calculation_replies).format(ans)
                return(f"Bot:  {final_answer}")
            
        elif any(word in user_input for word in cosine) and any(word in user_input for word in add):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                add_list = []
                for digit in digits:
                    digit = int(digit)
                    add_list.append(digit)
                    add_tuple = tuple(add_list)
                final_add = sum(add_tuple)
                ans = m.cos(m.radians(final_add))
                final_answer = random.choice(calculation_replies).format(ans)
                return(f"Bot:  {final_answer}")
            
        elif any(word in user_input for word in tan) and any(word in user_input for word in add):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                add_list = []
                for digit in digits:
                    digit = int(digit)
                    add_list.append(digit)
                    add_tuple = tuple(add_list)
                final_add = sum(add_tuple)
                ans = m.tan(m.radians(final_add))
                final_answer = random.choice(calculation_replies).format(ans)
                return(f"Bot:  {final_answer}")
            
        elif any(word in user_input for word in cot) and any(word in user_input for word in add):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                add_list = []
                for digit in digits:
                    digit = int(digit)
                    add_list.append(digit)
                    add_tuple = tuple(add_list)
                final_add = sum(add_tuple)
                ans = m.tan(m.radians(final_add))
                ans = 1/ans
                final_answer = random.choice(calculation_replies).format(ans)
                return(f"Bot:  {final_answer}")
            
        elif any(word in user_input for word in cosec) and any(word in user_input for word in add):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                add_list = []
                for digit in digits:
                    digit = int(digit)
                    add_list.append(digit)
                    add_tuple = tuple(add_list)
                final_add = sum(add_tuple)
                ans = m.sin(m.radians(final_add))
                ans = 1/ans
                final_answer = random.choice(calculation_replies).format(ans)
                return(f"Bot:  {final_answer}")
            
        elif any(word in user_input for word in sec) and any(word in user_input for word in add):
            digits = re.findall(r"\d+", user_input)
            if len(digits) > 1:
                add_list = []
                for digit in digits:
                    digit = int(digit)
                    add_list.append(digit)
                    add_tuple = tuple(add_list)
                final_add = sum(add_tuple)
                ans = m.cos(m.radians(final_add))
                ans = 1/ans
                final_answer = random.choice(calculation_replies).format(ans)
                return(f"Bot:  {final_answer}")
            
        elif "sing" in user_input:
            title = random.choice(list(songs.keys()))
            song_list =[]
            for line in songs[title]:
                 song_list.append(line)
            real_song = str(song_list)
            return f"Bot:  I will sing {title}  for you by an anonymous artist\n{real_song}"
        
        #the block that handles some basic calculation
        elif any(word in user_input for word in calculation) or not(any(word in user_input for word in calculation)):
            time.sleep(2)
            # addition
            if any(word in user_input for word in add):
                digits = re.findall(r"\d+",user_input)
                digit_list = []
                for digit in digits :
                    digit = int(digit)
                    digit_list.append(digit)
                digit_tuple = tuple(digit_list)
                final_add = sum(digit_tuple)
                final_answer = random.choice(calculation_replies).format(final_add)
                return(f"Bot:  {final_answer}")
            
            #Division
            elif any(word in user_input for word in divide):
                digits =  re.findall(r"\d+",user_input)
                digit_list = []
                for digit in digits:
                    digit =  int(digit)
                    digit_list.append(digit)
        
                if len(digit_list) == 2:
                    try:
                     ans = digit_list[0] / digit_list[1]
                     final_answer = random.choice(calculation_replies).format(ans)
                     return(f"Bot:  {final_answer}")
                    except ZeroDivisionError:
                     return "Bot:  I'm sorry, you cannot divide by zero"
                elif len(digit_list) == 3 :
                    try:
                        ans = digit_list[0] / digit_list[1] / digit_list[2]
                        final_answer = random.choice(calculation_replies).format(ans)
                        return(f"Bot:  {final_answer}")
                    except ZeroDivisionError:
                        return"Bot:  I'm sorry, you cannot divide by zero"
                elif len(digit_list) == 4 :
                    try:
                     ans = digit_list[0]/digit_list[1]/digit_list[2]/digit_list[3]
                     final_answer = random.choice(calculation_replies).format(ans)
                     return(f"Bot:  {final_answer}")
                    except ZeroDivisionError:
                        return"Bot:  I'm sorry, you cannot divide by zero"

                elif len(digit_list) == 5 :
                    try:
                     ans = digit_list[0]/digit_list[1]/digit_list[2]/digit_list[3]/digit_list[4]
                     final_answer = random.choice(calculation_replies).format(ans)
                     return(f"Bot:  {final_answer}")
                    except ZeroDivisionError:
                        return"Bot:  I'm sorry, you cannot divide by zero"
                else:
                    return"Bot:  I'm sorry, I can only divide at most five numbers at a time"

            #modulus
            elif any(word in user_input for word in modulus):
                digits = re.findall(r"\d+", user_input)
                if len(digits) == 2:
                    ans = int(digits[0]) % int(digits[1])
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                else:
                    return"Bot:  I'm sorry, I can only find the modulus of two numbers at a time"

            #multiplication
            elif any(word in user_input for word in multiply):
                digits = re.findall(r"\d+", user_input)
                digit_list = []
                for digit in digits:
                    digit = int(digit)
                    digit_list.append(digit)
                #digit_list = [int(digit) for digit in digits]
                if len(digit_list) > 1:
                 ans = 1
                 for digit in digit_list:
                    ans *= digit
                 final_answer = random.choice(calculation_replies).format(ans)
                 return(f"Bot:  {final_answer}")
                else:
                 return"Bot:  I'm sorry, I need at least two numbers to multiply"
                
            #Subtraction
            elif any(word in user_input for word in subtract):
                digits = re.findall(r"\d+", user_input)
                digit_list = []
                for digit in digits:
                    digit = int(digit)
                    digit_list.append(digit)
                if len(digit_list) == 2:
                    ans = digit_list[0] - digit_list[1]
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                else:
                    return("Bot:  I'm sorry, I can only subtract two numbers at a time")
                
            #Factorial
            elif any(word in user_input for word in factorial) or re.match(r"^.*\s+(\d+)+\!$",user_input):
                digits = re.findall(r"\d+", user_input)
                if len(digits) == 1:
                 ans = m.factorial(int(digits[0]))
                 final_answer = random.choice(calculation_replies).format(ans)
                 return(f"Bot:  {final_answer}")
                else:
                 return("Bot:  I'm sorry, I can only find the factorial of one number at a time")
                
            #Combination
            elif any(word in user_input for word in combination):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 2:
                    ans = m.comb(int(digits[0]), int(digits[1]))
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return("Bot:  I'm sorry, I can only find the combination of two numbers at a time")
                except:
                    return"Bot:  I'm sorry, there's an error in your input"
                
            #Permutation
            elif any(word in user_input for word in permutation):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 2:
                    ans = m.perm(int(digits[0]), int(digits[1]))
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return("Bot:  I'm sorry, I can only find the permutation of two numbers at a time")
                except:
                    return"Bot:  I'm sorry, there's an error in your input"
                
            #Square root
            elif any(word in user_input for word in square_root):
                digits = re.findall(r"\d+", user_input)
                if len(digits) == 1:
                    ans = m.sqrt(int(digits[0]))
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                else:
                    return"Bot:  I'm sorry, I can only find the square root of one number at a time"
                
            #Square
            elif any(word in user_input for word in square):
                try:
                    digits = re.findall(r"\d+", user_input)
                    if len(digits) == 1:
                        ans = int(digits[0]) ** 2
                        if str(digits[0]) == str(ans):
                         final_answer = random.choice(calculation_replies).format(f"still {ans}")
                         return(f"Bot:  {final_answer}")
                        else:
                            final_answer = random.choice(calculation_replies).format(ans)
                            return f"Bot:  {final_answer}"
                    elif len(digits) > 1:
                        return"Bot:  I'm sorry, I can only find the square of one number at a time"
                    else:
                        return"Bot:  I'm sorry, I can only work with numbers"
                except:
                    messagebox.showerror("Bot:  I'm sorry, there's an error in your input")

                #Cube root
            elif any(word in user_input for word in cube_root):
                digits = re.findall(r"\d+", user_input)
                if len(digits) == 1:
                    ans = int(digits[0]) ** (1/3)
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                else:
                    return"Bot:  I'm sorry, I can only find the cube root of one number at a time"
            
            #Cube
            elif any(word in user_input for word in cube):
                digits = re.findall(r"\d+", user_input)
                if len(digits) == 1:
                    ans = int(digits[0]) ** 3
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                else:
                    return"Bot:  I'm sorry, I can only find the cube of one number at a time"
                
            #sine
            elif any(word in user_input for word in sine):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 1:
                    ans = m.sin(m.radians(int(digits[0])))
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return"Bot:  I'm sorry, there's an error in your input"
                except:
                    messagebox.showerror("Bot:  I'm sorry, there's an error in your input")    

            #cosine
            elif any(word in user_input for word in cosine):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 1:
                    ans = m.cos(m.radians(int(digits[0])))
                    ans = round(ans, 6)
                    final_answer = random.choice(calculation_replies).format(round(ans,2))
                    return(f"Bot:  {final_answer}")
                 else:
                    return("Bot:  I'm sorry, there's an error in your input")
                except:
                    return("Bot:  I'm sorry, there's an error in your input")
                
            #tan
            elif any(word in user_input for word in tan):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 1:
                    ans = m.tan(m.radians(int(digits[0])))
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return"Bot:  I'm sorry, there's an error in your input"
                except:
                    return("Bot:  I'm sorry, there's an error in your input")
            #cot
            elif any(word in user_input for word in cot):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 1:
                    ans = m.tan(m.radians(int(digits[0])))
                    ans = 1/ans
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return("Bot:  I'm sorry, there's an error in your input")
                except:
                    return("Bot:  I'm sorry, there's an error in your input")
                
            #sec
            elif any(word in user_input for word in sec):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 1:
                    ans = m.cos(m.radians(int(digits[0])))
                    ans = 1/ans
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return("Bot:  I'm sorry, there's an error in your input")
                except:
                    return("Bot:  I'm sorry, there's an error in your input")
                
            #cosec
            elif any(word in user_input for word in cosec):
                try:
                 digits = re.findall(r"\d+", user_input)
                 if len(digits) == 1:
                    ans = m.sin(m.radians(int(digits[0])))
                    ans = 1/ans
                    final_answer = random.choice(calculation_replies).format(ans)
                    return(f"Bot:  {final_answer}")
                 else:
                    return "Bot:  I'm sorry, there's an error in your input"
                except:
                    return "Bot:  I'm sorry, there's an error in your input"
                
                #google search   
            elif any(word in user_input for word in search):
            
                API_KEY = 'AIzaSyD7LlikRTWQzhLpAquy-qAM3_mjGAK7sPI'
                SEARCH_ENGINE_ID = '64a20cc87f59e4935'

                service = build("customsearch", "v1", developerKey=API_KEY)

                # Perform the search
                query = user_input
                response = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()

                # Display results from search
                item_title_list = []
                item_content_list = []
                item_link_list = []
                for item in response.get('items', []):
                   item_title_list.append((item["title"]))
                   item_content_list.append(item["snippet"])
                   item_link_list.append(item["link"])
                second_title=random.choice(item_title_list)
                return f"Bot:  {random.choice(search_replies)}  \n\n1.{item_title_list[0]} {item_content_list[0]} and {random.choice(link_replies)}  {item_link_list[0]} .\n2.{second_title} {item_content_list[item_title_list.index(second_title)]} and {random.choice(link_replies)} {item_link_list[item_title_list.index(second_title)]}." 
            else:
                return f"Bot:  {random.choice(impossibility_replies)}"
                  
                   
                    
     except Exception as e:
            return f"Bot: Sorry an error occured \n{str(e)}"
#def plus_hour():
    #while True:
        #time.sleep(0)
        #plus_hour += 1
        #return plus_hour
#def plus_min():
    #while True:
        #time.sleep(0)
        #plus_min += 1
        #return plus_min


def date_time():
   now = dt.now()
   date = now.date()
   hrs = now.hour
   mins = now.minute
   if hrs == 12 and mins < 10:
    return f"  {hrs}:0{mins}PM"
   elif hrs == 12 and  mins> 10:
    return f"  {hrs}:{mins}PM"
   elif hrs ==0 and mins< 10:
    return f"  {hrs+12}:0{mins}AM"
   elif hrs == 0 and mins >10:
    return f"  {hrs+12}:{mins}AM"
   elif hrs > 12 and mins < 10:
      hrs = hrs - 12
      return f" {hrs}:0{mins} PM"
   elif hrs > 12 and mins > 10:
      hrs = hrs - 12
      return f" {hrs}:{mins} PM"
   elif hrs < 12 and mins < 10:
      return f" {hrs}:0{mins} AM"
   else :
      return f"  {hrs}:{mins} AM"


# Function to send user input and get bot response
def send_message():
    user_message = user_input.get()
    if user_message.strip():  # Ensure input is not empty
        chat_history.insert(tk.END, "You: " + user_message + "\n")
        response = chatbot_response(user_message)
        chat_history.insert(tk.END, response + "\n\n")
    user_input.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title(f"ALGEBOT🤖🤖🤖                                {date_time( )}")
root.geometry("800x600")
root.iconbitmap("food.jpg")
# Chat history area
chat_history = tk.Text(root, bg="wheat",fg="red", height=30, width=100)
chat_history.pack(pady=10)

# Takes the user input from the GUI
user_input = tk.Entry(root, width=100,border=3)
user_input.pack(side=tk.LEFT, padx=10,)

# Send button
send_button = tk.Button(root,bg="black",fg="yellow",width=5, text='''
  ⏫
s e n d''', command=send_message)
send_button.pack(side=tk.RIGHT, padx=10)

# Run the GUI application
root.mainloop()