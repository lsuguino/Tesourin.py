print('''
***************************************************************************      
             __ _.--..--._ _
         .-' _/   _/\_   \_'-.
        |__ /   _/\__/\_   \__|
           |___/\_\__/  \___|
                  \__/
                  \__/
                  \__/
                   \__/
                 ___\__/___
           . - '             ' -.
          /                      |
~~~~~~~  ~~~~~ ~~~~~  ~~~ ~~~  ~~~~~
  ~~~   ~~~~~   ~!~~   ~~ ~  ~ ~ ~~~~~~~~~
***************************************************************************      
    
      ''')

print('Bem vindo à ilha do coqueiro!')
print('Aqui tem um tesouro surreal, quer procurar?')
print('Vamos começar com as charadas então, escolha certo que você vai ter sucesso')
print('Você entra em uma sala empoeirada')
choice1 = input ('Essa sala possui dois caminhos, qual você quer seguir? Digite "direita" ou "esquerda"  ')

if choice1 == "esquerda" or choice1 == "Esquerda":
    choice2 = input('Você chegou em outra sala suspeita com um relógio com contagem regressiva de 30 min\nO que você quer fazer? Digite "esperar" ou "voltar" ')
    if choice2 == "esperar" or choice2 == "Esperar":
        choice3 = input ('Você esperou e a porta se abriu \nVocê entra em outra sala e possui três portas, qual delas você escolhe? \nDigite "direita" ou "meio" ou "esquerda" ') 
        if choice3 == "direita" or choice3 == "Direita":
            print('Você foi trancado e a sala começou a pegar fogo. GAME OVER')
        elif choice3 == "meio" or choice3 == "Meio":
            print('Você achou um baú cheio de itens de ouro. You WIN!')
        elif choice3 == "esquerda" or choice3 == "Esquerda":
            print('Você entra em uma sala escura e foi picado por escorpiões. GAME OVER')
    else: 
        print('Você tentou voltar e a porta esmagou você. GAME OVER')
else:
    print('Você caiu em um buraco com espinhos. GAME OVER')