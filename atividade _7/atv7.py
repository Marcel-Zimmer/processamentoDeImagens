import cv2

imagem_colorida = cv2.imread(r"atividade _7\img\img.jpg")


largura = int(imagem_colorida.shape[1] * 0.3) 
altura = int(imagem_colorida.shape[0] * 0.3)    
imagem_redimensionada = cv2.resize(imagem_colorida, (largura, altura))

imagem_cinza = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)

_,imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

detBorda = cv2.Canny(imagem_binaria, 100, 200)



cv2.imshow("imagem",detBorda)
cv2.waitKey(0)
cv2.destroyAllWindows()