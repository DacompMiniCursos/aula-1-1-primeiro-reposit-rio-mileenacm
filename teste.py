
def par():

    a= int(input("Digite um número: "))

    if a%2==0:
        
        print("O número é par")
        return True
        
    else:
        
        print("O número é ímpar")
        return False

print(par())

