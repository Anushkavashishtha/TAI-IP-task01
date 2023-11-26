import random

number = random.randint(1,100)
player_name=input("YOUR NAME:")
number_of_guess=0
print('Thankyou!' + player_name + 'I am guessing a number')
while number_of_guess<7:
    guess= int(input())
    number_of_guess += 1
    if guess< number:
        print('Your guess is to low. TRY AGAIN')
    elif guess>number:
        print('Your guess is to high. TRY AGAIN')
    else:
        break
if guess == number:
    print('CONGRATULATIONS,' + player_name + '! You guessed the number in' + str(number_of_guess) + 'tries')
else:
    print('Sorry!'+ player_name + 'you did not guess the number.The number was' + str(number))
