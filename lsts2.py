friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.append("Harsh")
friends.insert(3,"Vedangi")
friends[0]="Avdhoot"
friends[1]="Parth"
friends[2]="Shubham"
friends[4]="Irfan"
friends[5]="Smitesh"
friends.extend(cars)
friends.pop()
friends.remove("Irfan")
del cars[4]
print(friends)
print(cars)
new_friends = friends[:]
new_friends2 = friends.copy()
new_friends3 = list(friends)
print(new_friends)
print(new_friends2)
print(new_friends3)