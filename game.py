import random
erros=0
acertos=[]
digitadas=[]
 
def main():
    print("="*39)
    print("="*12, "Jogo da Forca", "="*12)
    print("="*39)
    embaralha()
    opcao()
    print("="*39)
 
def imprimir():
    print("Palavra Chave -> %s"%senha)
    print("Você errou %d vezes"%erros)
    print("Letras digitadas")
    for x in digitadas:
        print(x, end="|")
    print()
 
def embaralha():
    global palavras, secreta, senha
    palavras =["casa", "carro", "loja","analfabeto","reflexao","interrupcao","necessarios","ambulantes","humanidade",
    "juventude","shopping","supermercado","proporcionar","sensatez","incidente","governo","flexibilidade"]
    random.shuffle(palavras)
    senha = palavras[0]
    secreta =[]
    x = 0
    while x < len(senha):
        secreta.append("_")
        x+=1
    for x in secreta:
        print(x, end=" ")
    print()
 
def opcao():
    global letra
    while True:
        letra = input("Digite uma letra ou (0) para sair: ")
        print("="*39)
        while len(letra) != 1 :
            print("Digite apenas uma letra!")
            letra = input("Digite uma letra ou (0) para sair: ")
            print("="*39)
 
        while letra in digitadas:
            print("Letra repetida")
            letra = input("Digite outra letra ou (0) para sair: ")
            print("="*39)
        if letra == "0":
            break
        else:
            analisa()
        if erros == 7:
            break
        elif len(acertos) == len(senha):
            print("Parabéns Você venceu")
            break
 
def boneco():
    while True:
        print("Você errou %s vez(es)"%erros)
        if erros == 1:
            print("|")
            break
        elif erros == 2:
            print("|\n|")
            break
        elif erros == 3:
            print("/| \n | ")
            break
        elif erros == 4:
            print("/|\ \n |")
            break
        elif erros == 5:
            print("/|\ \n |\n/")
            break
        elif erros == 6:
            print("/|\ \n |\n/ \ ")
            break
        else:
            print("Enforcado, Você perdeu!")
            print(" O\n/|\ \n |\n/ \ ")
            break
 
def analisa():
    global erros, digitadas, acertos
    while True:
        if letra in senha:
            digitadas.append(letra)
            p = 0
            while p > -1:
                p = senha.find(letra,p)
                if p >=0:
                    secreta[p] = letra
                    acertos.append(letra)
                    p+=1
            for x in secreta:
                print(x, end=" ")
            print()
            print("Você acertou",len(acertos),"de",len(senha),"letras!")
            print("Digitadas!")
            print("="*39)
            for c in digitadas:
                print(c, end="|")
            print()
            break
        else:
            digitadas.append(letra)
            print("Digitadas!")
            print("="*39)
            for c in digitadas:
                print(c, end="|")
            print()
            erros+=1
            boneco()
            break
 
 
 
main()
imprimir()
