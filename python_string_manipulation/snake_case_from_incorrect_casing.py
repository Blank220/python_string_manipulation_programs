#ask user to input fullname in incorrect casing
fullname = input('Enter Your Fullname in incorrect casing: ')
#convert to lowercase and replace spaces with underscore
snake_case = fullname.lower() .replace(' ', '_')
#print the result in snake case
print(f'Name in snake case: {snake_case}')
