try:
    with open('text') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")

