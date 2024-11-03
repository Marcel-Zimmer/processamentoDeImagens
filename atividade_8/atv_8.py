import cv2

imagem_colorida = cv2.imread(r"atividade_8\img\flor.jpg")



imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)


filtragem = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

_, imagem_binaria = cv2.threshold(filtragem, 127, 255, cv2.THRESH_BINARY)

_, imagem_binaria2 = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)


cv2.imshow("imagem",imagem_binaria2)
cv2.waitKey(0)
cv2.destroyAllWindows()