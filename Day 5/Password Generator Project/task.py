import random
password=[]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#letters_size = len(letters)
#numbers_size = len(numbers)
#symbols_size = len(symbols)
#print(f'letters_size {letters_size} \nnumbers_size {numbers_size} \nsymbols_size {symbols_size}\n ')

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = nr_letters
nr_symbols = nr_letters

for _ in range(1,nr_letters+1):
    random_letter = random.choice(letters)  # Picks a random element from the letters list
    password.append(random_letter)
print(password)

for _ in range(1,nr_numbers+1):
    random_letter = random.choice(numbers)  # Picks a random element from the letters list
    password.append(random_letter)
print(password)

for _ in range(1,nr_symbols+1):
    random_letter = random.choice(symbols)  # Picks a random element from the letters list
    password.append(random_letter)
print(password)
random.shuffle(password)
print(password)


password_string=''
for constr in password:
    password_string +=  str(constr)

print(password_string)


#

