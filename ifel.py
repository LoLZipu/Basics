is_raining = False
is_cold = True
print("Good morning.")

if is_raining and is_cold:
    print('Bring umbrella and jacket')
elif is_raining and not(is_cold):
    print('Bring umbrella')
elif is_cold and not(is_raining):
    print('Bring jacket')
else:
    print('Shirt is fine!')