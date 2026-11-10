secret_animal = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_animal and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input('enter animal name:')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('you lose')
else:
    print('you win')

exit()

#secret_word = 'begin'
#word =''

#while word != 'begin':
    #word = input('Enter word:')
#print('The while loop condition has been met')