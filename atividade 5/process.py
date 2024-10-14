import cv2
import numpy as np

def somaPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        soma_imagens = np.zeros((altura, largura, canais), dtype=np.uint8)
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    valor_somado = img1[y, x, c] + img2[y, x, c]
                    if valor_somado > 255:
                        valor_somado = 255
                    soma_imagens[y, x, c] = valor_somado

        cv2.imshow('Soma das Imagens', soma_imagens)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



def subPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        sub_imagens = np.zeros((altura, largura, canais), dtype=np.uint8)
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    valor_subtraido = img1[y, x, c] - img2[y, x, c]
                    if valor_subtraido > 255:
                        valor_subtraido = 255
                    sub_imagens[y, x, c] = valor_subtraido

        cv2.imshow('Sub das Imagens', sub_imagens)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def multPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        mul_imagens = np.zeros((altura, largura, canais), dtype=np.uint8)
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    valor_multiplicado = img1[y, x, c] * img2[y, x, c]
                    if valor_multiplicado > 255:
                        valor_multiplicado = 255
                    mul_imagens[y, x, c] = valor_multiplicado

        cv2.imshow('Mul das Imagens', mul_imagens)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def divPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        div_imagens = np.zeros((altura, largura, canais), dtype=np.uint8)
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    valor_dividido = img1[y, x, c] / img2[y, x, c]
                    if valor_dividido > 255:
                        valor_dividido = 255
                    div_imagens[y, x, c] = valor_dividido

        cv2.imshow('Div das Imagens', div_imagens)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def andPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        resultado_and = np.zeros((altura, largura, canais), dtype=np.uint8)
        
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    resultado_and[y, x, c] = img1[y, x, c] & img2[y, x, c]
   
        cv2.imshow('AND das Imagens', resultado_and)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def orPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        resultado_or = np.zeros((altura, largura, canais), dtype=np.uint8)
        
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    resultado_or[y, x, c] = img1[y, x, c] | img2[y, x, c]
   
        cv2.imshow('OR das Imagens', resultado_or)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def notPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        resultado_not = np.zeros((altura, largura, canais), dtype=np.uint8)
        
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    not_img1 = 255 - img1[y, x, c]
                    not_img2 = 255 - img2[y, x, c]
                    valor_final = not_img1 + not_img2
                    if valor_final > 255:
                        valor_final = 255
                        
                    resultado_not[y, x, c] = valor_final
   
        cv2.imshow('NOT das Imagens', resultado_not)
        cv2.waitKey(0)
        cv2.destroyAllWindows()        

def xorPixels(img1, img2):
    if img1.shape == img2.shape:
        altura, largura, canais = img1.shape
        resultado_xor = np.zeros((altura, largura, canais), dtype=np.uint8)
        
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):
                    # Usando XOR bit a bit
                    resultado_xor[y, x, c] = img1[y, x, c] ^ img2[y, x, c]
   
        cv2.imshow('XOR das Imagens', resultado_xor)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

imagemUm = cv2.imread('/home/virus/Documents/processamentoDeImagens/atividade 5/img/1.jpg')
imagemDois = cv2.imread('/home/virus/Documents/processamentoDeImagens/atividade 5/img/2.jpg')  

xorPixels(imagemUm,imagemDois)



