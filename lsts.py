friends = ["Avdhoot","Parth","Shubham","Smitesh","Irfan"]
numl = [23,65,8,52,77]
print(friends)
print(numl)
print(friends[1]+str(numl[2]))
print(friends[4],numl[2])
print(numl[::-1])
print(len(friends),len(numl))
print(numl.index(77),friends.index("Smitesh"))
print(friends.count("Parth"))
friends.sort(reverse=True)
numl.sort()
print(min(friends))
print(sum(numl))