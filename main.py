# Entrada de dados

nome = input('Informe o seu nome: \n')
nota = str(input('Informe a sua nota: \n')).replace(',', '.')

nota = float(nota)

# Verifica a nota

if nota >=7:
    print(f'{nome} está aprovado')
elif nota >=5:
    print(f'{nome} está de recuperação')
else:
    print(f'{nome} está reprovado')


    