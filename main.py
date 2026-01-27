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


lst = ["elm1", "elm2", "elm3"]
print(lst)
lst.append("elm4")
print(lst)
lst.append(30)
print(lst)
lst.remove("elm4")
lst.pop(0)
print(lst)

cnt = lst.count("elm1")
print(cnt)

print(len(lst))
print(lst.__len__())
print(lst[0])

# Pedir ao user 5 nomes, mostrar a lista dos nomes
nomes = []
for i in range(5):
    n = input("Nome: ")
    nomes.append(n)

for i in range(len(nomes)):
    print(nomes[i])
    
# Pedir n nomes ao user, mostrar a lista dos nomes até ser inserido 0, e mostrer a lista dos nomes
nomes2 = []
while True:
    n = input("Nome (0 para sair) -> ")
    if n == "0":
        break
    nomes2.append(n)

for nome in nomes2:
    print(nomes2)

aluno = {
    "nome": "Diogo",
    "media": 18,
    "estado": "aprovado"}

print(aluno)

aluno["escola"] = "ATEC"

print(aluno)

aluno["escola"] = "IEFP"

print(aluno)

aluno.pop("escola")

print(aluno)

aluno.popitem()
print(aluno)

for keys in aluno:
    print(keys)
for keys in aluno.keys():
    print(keys)    
for values in aluno.values():
    print(values)
for keys, values in aluno.items():
    print(f"{keys} -> {values}")


# Funcao
def nome():
    print("Antes")
    pass
    print("Depois")

def soma(val1, val2):
    return val1 + val2

res = soma(12, 12)

print(res)

def soma2(val1: int, val2: int) -> int:
    return val1 + val2

res = soma2(15, 25)
print(res)

def demo(num1:int, num2):
    pass