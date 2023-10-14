
text = "Yoooooo\nThis is some text\nHave a good one"
text1 = "\nYou appended me !!! "

with open('text', 'w') as file:
    file.write(text)

with open('text', 'a') as file:
    file.write(text1)
