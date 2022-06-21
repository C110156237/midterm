i = int(input('Please enter a number'))

if (i <= 0):
  print('Please try again later.')
else:
  for a in range(i):
    name, email = input('Please enter your name and email. (use spaces to separate)').split(' ')
    dict = {name: email}
    dict[name] = email

print(dict)


while True:
    i = input(" Please enter your name and email. (use spaces to separate or Enter to quit): ")
    if not i:
        break
    print("Your input:", i)
print("While loop has exited")



