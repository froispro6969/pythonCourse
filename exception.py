
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! ")

except ValueError:
    print("Enter only numbers!")

except Exception:
    print("something went wrong :(")

else:
    print(result)

finally:
    print("This will always execute")