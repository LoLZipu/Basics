name = input("Please enter your name: ")
km = input("Enter the distance in kilometres: ")
mile = float(km)/1.609
print(f"Greetings {name.title()}! {km} kilometres is equivalent to {round(mile,2)} miles")
