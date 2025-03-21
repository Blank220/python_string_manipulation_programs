#ask user to input fullname in incorrect casing
fullname = input('Enter Your Fullname in incorrect casing: ')
#convert to pascal case by using title() and removing spaces
pascal_case = fullname.title() .replace(' ', '')
#print fullname in pascal case
print(f'Name in Pascal casing: {pascal_case}')