csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

friends_list = (",".join(",".join(csv.split(";")).split(":")).split(","))
print(friends_list)
print("Replace", csv.replace(";",",").replace(":",",").split(","))