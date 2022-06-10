import cv2
import numpy as np

#negativo

# Imagem é carregada, primeiro parametro é o caminho da imagem e o segundo parametro é uma flag para definir se a imagem é lida em colorido ou preto e branco
img_in = cv2.imread('data/t1.jpg',0)

# Explicação da implementação em python:
#   A variavel img_in e img_out, sem utilizar a função cv2.imshow retorna uma matriz contendo os valores da imagem em forma de matriz
#   ao diminuir todos os valores da matriz por 255 resulta nas cores inverterem, criando assim a imagem negativa 
img_out = 255 - img_in

print("Matriz original: ")
print(img_in)
print("Matriz negativa: ")
print(img_out)

cv2.imshow('in', img_in)
cv2.waitKey(0)
cv2.imshow('out', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()