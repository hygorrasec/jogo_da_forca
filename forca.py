# JOGO DA FORCA CRIADO POR HYGOR RASEC E IDEALIZADO POR YURI COSTA EM 24/09/2022!

import random
import unicodedata

palavras = ['Espinafre', 'Nectarina', 'Carne de vitela', 'Alcachofra', 'Vinagre', 'Caqui', 'Tamareira', 'Figo', 'Rabanete', 'Vinagre', 'Caranguejo', 'Pomba', 'Besouro', 'Guaxinim', 'Carpa', 'Coala', 'Mosquito', 'Mula', 'Vaca', 'Cavalo', 'Solidariedade', 'Importa', 'Matemática', 'Fonética', 'Cálculo', 'Caderno', 'Cultura', 'Tutor', 'Pedagogia']

sorteio = random.choice(list(palavras))

# caso a palavra tenha acento, ele vai remover.
remove_acentos = unicodedata.normalize("NFD", sorteio)
remove_acentos = remove_acentos.encode("ascii", "ignore")
remove_acentos = remove_acentos.decode("utf-8")

# criando uma lista com cada letra da palavra.
list_sorteio = list(remove_acentos)

letras_descobertas = []
letras_usadas = []
tentativas = 6
acertou = 0

print(f'\nBoas vindas ao jogo da FORCA! Temos {len(palavras)} palavras em nosso banco de dados e iremos sortear uma para você tentar adivinhar. Lembre-se, você terá apenas {tentativas} tentativas.')
print('DIVIRTA-SE!!!')

for l in range(len(list_sorteio)):
    if list_sorteio[l] == ' ':
        letras_descobertas.append('-')
    else:
        letras_descobertas.append('_')

while tentativas > 0:
    while True:
        print('\nA palavra é: ', end='')
        for p in letras_descobertas:
            print(f'{p} ', end='')
        d = input('\nAdivinhe uma letra: ').upper()
        if d in letras_usadas:
            if len(letras_usadas) > 1:
                print('\nVocê já tentou as letras: ', end='')
                for l in letras_usadas:
                    print(f'{l!r}, ', end='')
                print('tente outra!')
            else:
                print(f'\nVocê já tentou a letra {d!r}.')
        else:
            break

    for l in range(len(list_sorteio)):
        if d == list_sorteio[l].upper():
            acertou = 1
            list_sorteio[l] = '*'
            letras_descobertas[l] = d.upper()

    if list_sorteio.count('*') == (len(sorteio) - letras_descobertas.count('-')):
        print('\n-----------------------------')
        print('PARABÉNS! Você ganhou o jogo!')
        print(f'A palavra era {sorteio.upper()!r}.')
        print('-----------------------------\n')
        break
    elif acertou:
        acertou = 0
        print('\n------------------------------------------------')
        print(f'Parabéns! Você descobriu a letra {d.upper()!r} na palavra!')
        print('------------------------------------------------')
    else:
        tentativas -= 1
        if tentativas != 0:
            print('\n-----------------------------')
            print(f'Não existe a letra {d.upper()!r} na palavra.')
            print(f'Você ainda tem {tentativas} tentativas.')
            print('-----------------------------')

    letras_usadas.append(d.upper())

if tentativas == 0:
    print('\n------------------------')
    print('Acabaram suas tentativas.\n')
    print(f'A palavra era: {sorteio.upper()!r}.')
    print('Você tentou:   \'', end='')
    for p in letras_descobertas:
        print(f'{p}', end='')
    print('\'.')
    print('\nE você tentou as letras: ', end='')
    for l in letras_usadas:
        print(f'{l!r} ', end='')
    print('\n------------------------\n')

print('Jogo criado por Hygor Rasec e idealizado por Yuri Costa em 24/09/2022!')
