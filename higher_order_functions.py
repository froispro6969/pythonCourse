# a function that either:
# 1. accept a function as an arguent or
# 2. return a function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("HELLO")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))