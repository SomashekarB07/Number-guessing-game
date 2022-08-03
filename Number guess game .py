from random import randrange

computer_input = randrange(1,100)
user_input = int(input("Enter the number :"))
limit = 1

while limit<=9:
    if(user_input<computer_input):
        print("HIGHER NUMBER PLEASE")
        user_input = int(input("Enter the number again :"))
        limit +=1

    elif(user_input>computer_input):
        print("LOWER NUMBER PLEASE")
        user_input = int(input("Enter the number again :"))
        limit +=1

    else:
        print("NUMBER IS MATCHED")
        print(f"Number of attempts taken is {limit}")
        break
print(f'The random number taken by computer is {computer_input} ')

if(limit>9):
    print("Game over !!!!!!!!")
