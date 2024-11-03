import cv2

imagem_colorida = cv2.imread(r"atividade_8\img\flor.jpg")


largura = int(imagem_colorida.shape[1] ) 
altura = int(imagem_colorida.shape[0] )    
imagem_redimensionada = cv2.resize(imagem_colorida, (largura, altura))

imagem_cinza = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)


_, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

imagem_cinza = imagem_binaria.astype('uint8')



cv2.imshow("imagem",imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()