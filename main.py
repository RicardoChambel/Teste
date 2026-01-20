nome = "Rei Cardo"

print(nome)

print(f"Ola {nome}")
print("Ola",nome)
print("Ola " + nome)

idade = 10

# 1º
if idade < 18:
    print("Menor de idade")
elif idade >= 18:
    print("Maior de idade")
else:
    print("Idade invalida")

# 2º
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade >= 18:
    print("Adulto")


nota1 = int(input("Nota 1 -> "))
nota2 = int(input("Nota 2 -> "))

if nota1 < 10 and nota2 < 10:
    print("Reprovado")
elif nota1 >= 10 and nota2 >= 10:
    print("Aprovado")
else:
    print("Recuperação")


print("-- MENU --")
print("[1] Ola Mundo")
print("[2] Bom Dia")
print("[3] Boa Noite")
esc = int(input("Opc -> "))
match esc:
    case 1:
        print("Ola Mundo")
    case 2:
        print("Bom Dia")
    case 3:
        print("Boa Noite")
    case _:
        print("Opcao Invalida")


# tabuada

num = int(input("Tabuada de: "))
if num < 1 or num > 10:
    print("Numero invalido")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")