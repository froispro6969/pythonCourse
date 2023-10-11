#dictionary = A changeable, unordered collection of unique key: value pairs. Fast because they use hashing, allow us to acces a value quickly.

capitals = {"USA": "Washinghton",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")
#capitals.clear()

#print(capitals["Germany"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items()) # wyswietla caly slownik

for key,value in capitals.items():
    print(key, value)