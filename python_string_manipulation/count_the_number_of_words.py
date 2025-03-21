#ask user to input a complete statement
statement = input('Enter a Complete Statement: ')
#split the statement into words and count them
word_count = len(statement.split())
#print number of words 
print(f'Statement word count: {word_count} words')