qtd = maioridade = midade = msex = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dec = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    qtd += 1
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        msex += 1
    if sexo == 'F' and idade < 20:
        midade += 1
    if dec == 'N':
        break
print(f'''{qtd} pessoas cadastradas
{maioridade} pessoas acima de 18 anos
{msex} homens
{midade} mulheres com menos de 20 anos.''')