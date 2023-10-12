#animal = "cow"
#item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

# name = "Damian"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) #padding z prawej
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) #padding z lewej
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) #center

number = 3.14123
number1 = 1000

print('The number pi is {:.2f}'.format(number)) # wyswietli 3.14
print('The number pi is {:,}'.format(number1)) # wyswietli 1,000
print('The number pi is {:b}'.format(number1)) #binarny
print('The number pi is {:o}'.format(number1)) #osemkowy
print('The number pi is {:x}'.format(number1)) #szesnatskowy

