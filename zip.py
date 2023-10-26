usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssw0rd","abc123","quest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key,value)


users_info = zip(usernames,passwords,login_date)

for i in users_info:
    print(i)