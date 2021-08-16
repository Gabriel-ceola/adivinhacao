tentativas = 3
rodada = 1
segredo = int(69)
while (rodada <= tentativas):
  adivinhacao = int(input('Digite um número '))

  if (rodada == tentativas):
    print('Você errou 3 vezes, sinto muito.')
    break
  if (adivinhacao == segredo):
    print('Você acertou o chute!')
    break
  elif(adivinhacao > segredo):
    rodada = rodada + 1
    print('O seu chute foi maior que o número secreto, tente novamente')
    print('Rodada {} de {}'.format(rodada, tentativas))
  elif(adivinhacao < segredo):
    rodada = rodada + 1
    print('O seu chute foi menor que o número secreto, tente novamente')
    print('Rodada {} de {}'.format(rodada, tentativas))

