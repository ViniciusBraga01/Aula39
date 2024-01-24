from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {} '.format(nasc,idade,atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(atual))
elif idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado há {} anos '.format(saldo))
