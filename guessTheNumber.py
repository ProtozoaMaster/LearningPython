#Programa de "descobrir o número"
import random #funcao python para gerar valores aleatorios
secretNumber = random.randint(1,20) #a variavel ira receber um valor aleatorio
print('I am thinking of  a number between 1 and 20.')

#A interface pergunta para o usuário dar um palpite 6 vezes
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #o loop encerra caso o usuario acerte o valor

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
