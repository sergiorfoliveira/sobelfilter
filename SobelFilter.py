# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

def inicializa(matriz_in):
    '''
    Opcional: zero padding
    '''
    x,y,z = np.shape(matriz_in)
    matriz_out = np.zeros((x+2,y+2,z), dtype=np.uint8)
    for i in range(x):
        for j in range(y):
            matriz_out[i+1][j+1]=matriz_in[i][j]
    return matriz_out

def correl(m0, m1, m2):
    '''
    m0 e m1: filtros 3x3 vertical e horizontal
    m2: matriz a ser filtrada
    '''
    x,y,z = np.shape(m2)
    submatriz=np.zeros((3,3,3), dtype=np.uint8)
    result=np.zeros((x-2,y-2,3), dtype=np.uint8)
    for j in range(x-2):
        for k in range(y-2):
            submatriz =     [
                              [m2[j  ,k],m2[j  ,k+1],m2[j  ,k+2]],
                              [m2[j+1,k],m2[j+1,k+1],m2[j+1,k+2]],
                              [m2[j+2,k],m2[j+2,k+1],m2[j+2,k+2]]
                            ]
            result[j,k] = np.sqrt((sum(np.sum(m0 * submatriz, axis=1)))**2 + 
                                  (sum(np.sum(m1 * submatriz, axis=1)))**2)
            result[j,k] = np.clip(np.round(result[j,k]),a_min=0,a_max=255)
    return result

def main():
    # ref: https://en.wikipedia.org/wiki/Sobel_operator
    dx = np.array ([
                    [   
                        [-1],[0],[1]
                    ],
                    [
                        [-2],[0],[2]
                    ],
                    [
                        [-1],[0],[1]
                    ]
                   ])
    dy = np.array ([
                    [   
                        [-1],[-2],[-1]
                    ],
                    [
                        [0],[0],[0]
                    ],
                    [
                        [1],[2],[1]
                    ]
                   ])


    image = Image.open("C:\\Users\\F9910101\\Pictures\\cat03.jpg")
    immatriz = np.array(image)
    #pix = inicializa(pix) # nao necessario
    result=correl(dx,dy,immatriz)
    del immatriz
    img = Image.fromarray(result)
    img.show()

main()


