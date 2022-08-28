import random

print('Welcome to the HI-Lo game')
print('You got 6 tries')
tries = 1
guess_no = random.randint(1, 100)
while tries < 10:
    tries += 1
    num = int(input('Guess a no between 1 & 100:'))
    if num == guess_no:
        print(f'Got it: The number is {guess_no}')
        break
    elif num < guess_no:
        print('Too low!')
    else:
        print('Too High')