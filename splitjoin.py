msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split(), type(msg.split()))
print(csv.split(","))
print(" | ".join(friends_list+friends_list))
print("".join(msg.split())) #to remove the white spaces between strings
#print(msg.replace(" ","")) <-another way to remove white sapces^