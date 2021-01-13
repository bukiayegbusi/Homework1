# program to store a random number 1-10 in a variable - task 1
import random
random.randint(1, 10)
number =(random.randint(1, 10))
# program to ask a user for their name and store as a variable
name = input('What is your name? ')
# program to ask a user to guess the number between 1 and 10
print(name, 'Can you guess a number between 1 and 10? ')
guess = int(input('Whats your guess? '))
if guess == number:
    print(name, 'Welldone!, You have guessed correctly!')
else:
    print(name, 'Sorry!, That is wrong!')

# Program to asks a user for their favourite number between 1 and 100 - task 2
number =(random.randint(1, 100))
print(name, 'What is your favourite number? ')
answer = int(input('Answer:'))
if answer <35:
    print(name, 'What is the worst school trip? The one to the principals office!')
elif answer <=70:
    print(name, 'I invented a new word, Plagiarism!')
elif answer <= 100:
    print(name, 'Why do we tell actors to break a leg? Because every play has a cast.')
else:
   print (name, 'That number is incorrect!')

# Program that allows user to enter their favourite starter, main course, dessert and drink - task 3
starter = input('What is your favourite starter? ')
main_course = input ('What is your favourite main course? ')
desert = input('What is your favourite desert? ')
drink = input('what is your favourite drink? ')
statement = f'{starter} {main_course} {desert} with a glass of {drink}'
print(name, 'Your favourite meal is', statement)

# Program to run loop - task 4
for i in range (2000,800,-200):
    print(i)

# Program - task 5
number_one = int(input('Guess a number: '))
number_two = int(input('Guess another number: '))
choice = int(input('make a choice from 8 options 1 to 8, 1 to add both numbers, 2 to subtract, 3 to divide the '
                   'numbers, 4 to multiply both numbers, 5 for your first number raised two the power'
                   'of 3 and 6 for your second number to the power of 3, 7 is square of number one'
                   ', and finally 8 is square of number 2: '))
option_one = number_one + number_two
option_two = number_two - number_one
option_three = number_two / number_one
option_four = number_two * number_one
option_five = number_one ** 3
option_six = number_two ** 3
option_seven = number_one * number_one
option_eight = number_two * number_two
if choice == 1:
   print(option_one)
elif choice == 2:
   print(option_two)
elif choice == 3:
   print(option_three)
elif choice == 4:
   print(option_four)
elif choice == 5:
    print(option_five)
elif choice == 6:
    print(option_six)
elif choice == 7:
    print(option_seven)
elif choice == 8:
    print(option_eight)
else:
   print('you have made an invalid choice')
