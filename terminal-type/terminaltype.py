import getch, sys, time, random, os

#Chooses random prompt
with open('250words.txt', 'r') as file:
    word_bank = file.read()
words = word_bank.split() #Splits the string of text into seperate words

#User picks how many words
prompt_length = int(input("Input word count: ex. 15, 30, 100, etc"))
print("\n")

#Adds x number of random words into prompt list
prompt_words = []
for word in range(prompt_length):
    next_word = words[random.randint(0,249)]
    prompt_words.append(next_word)

#Combines list of words into single string
seperator = " "
prompt = seperator.join(prompt_words)

#Displays typing prompt in terminal
print(" ")
print(prompt)

#Creates line
terminal_size = os.get_terminal_size()
terminal_width = terminal_size.columns
# Create a line
line = '-' * terminal_width
print(line)

print("Begin Text:")

#Initiate variables
user_input = []
char_count = 0 #Keeps track of what character the user is on
starttime = time.time()
incorrect_char = 0 

#Main loop
while True:
    #Collecting user input
    char = getch.getch()
    
    if char == "\n":
        if char_count != len(prompt):
            print()
            print("Did not complete")
            exit()
        else: break
        
     
    user_input.append(char)

    #Checks if char is correct
    try:
        if char == prompt[char_count]:
            sys.stdout.write(char)
            sys.stdout.flush()
            char_count += 1
            if char_count == 1:
                starttime = time.time()
        else:
            incorrect_char += 1
            

    except:
        break

#Calculations
netTime = time.time() - starttime
raw_wpm = (len(prompt)/5) // (netTime / 60)
net_wpm = raw_wpm - (incorrect_char / (netTime / 60))
if net_wpm <= 0:
    net_wpm = 0
accuracy = (len(prompt) - incorrect_char) / len(prompt)

print("Net Words per minute:", round(net_wpm))
print("Raw Words per minute:", round(raw_wpm))
print("Accuracy:", round((accuracy * 100), 2))
