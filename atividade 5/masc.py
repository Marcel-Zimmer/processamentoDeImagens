import numpy as np
import cv2

def convolucao_manual_colorida(imagem, mascara):
    altura, largura, canais = imagem.shape
    resultado = np.zeros((altura, largura, canais), dtype=np.float32)
    m, n = mascara.shape
    offset_x = m // 2
    offset_y = n // 2

    for c in range(canais):
        for y in range(offset_x, altura - offset_x):
            for x in range(offset_y, largura - offset_y):
                valor_pixel = 0
                for mi in range(m):
                    for nj in range(n):
                        valor_pixel += imagem[y + mi - offset_x, x + nj - offset_y, c] * mascara[mi, nj]
                resultado[y, x, c] = valor_pixel

    return resultado

imagemUm = cv2.imread('/home/virus/Documents/processamentoDeImagens/atividade 5/img/1.jpg')

mascara_unilateral = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])

mascara_bilateral = np.array([[1, 2, 1],
                              [2, 4, 2],
                              [1, 2, 1]]) / 16

imagem_unilateral = convolucao_manual_colorida(imagemUm, mascara_unilateral)
imagem_bilateral = convolucao_manual_colorida(imagemUm, mascara_bilateral)

imagem_unilateral = np.clip(imagem_unilateral, 0, 255).astype(np.uint8)
imagem_bilateral = np.clip(imagem_bilateral, 0, 255).astype(np.uint8)

cv2.imshow('Imagem Convoluida Unilateral (Sobel)', imagem_unilateral)
cv2.imshow('Imagem Convoluida Bilateral (Gaussian)', imagem_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
