#!/usr/bin/env python

import string
from os import system

alfabeto = list(string.ascii_lowercase)
megaSenha = 'eutenhoumiphonenano'
palavraRevelada = ['*' for letter in megaSenha]

def my_median(sorted_list):
  if len(sorted_list)%2 == 0:
    return (len(sorted_list)//2)
  elif (len(sorted_list)//2)-1 < 0:
    return 0
  else:
    return (len(sorted_list)//2)-1

listaDeIndexes = [(my_median(alfabeto), alfabeto) for letter in megaSenha]
contador = 20
while ''.join(palavraRevelada) != megaSenha and contador>0:
  system('clear')
  print('Descobrindo letras...')
  for idx, letra in enumerate(megaSenha):
    if listaDeIndexes[idx][0] < listaDeIndexes[idx][1].index(letra):
      listaDeIndexes[idx] = (
          my_median(alfabeto[listaDeIndexes[idx][0]:]),
          listaDeIndexes[idx][1][listaDeIndexes[idx][0]:]
      )
    elif listaDeIndexes[idx][0] > listaDeIndexes[idx][1].index(letra):
      listaDeIndexes[idx] = (
          my_median(alfabeto[:listaDeIndexes[idx][0]]),
          listaDeIndexes[idx][1][:listaDeIndexes[idx][0]]
      )
    elif listaDeIndexes[idx][0] == listaDeIndexes[idx][1].index(letra):
      palavraRevelada[idx] = listaDeIndexes[idx][1][listaDeIndexes[idx][0]]
  print(palavraRevelada)
  contador -= 1
