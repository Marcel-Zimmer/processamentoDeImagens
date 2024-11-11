import cv2

imagem_colorida = cv2.imread(r".\img\img.jpg")


imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)


#limiarização manual :
valor_limiar = 80
valor_maximo = 255
_, imagem_limiarizada_manual = cv2.threshold(imagem_cinza, valor_limiar, valor_maximo, cv2.THRESH_BINARY)

#limiarização otsu
_, imagem_limiarizada_otsu = cv2.threshold(imagem_cinza, 0, valor_maximo, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Aplicar a limiarização adaptativa
imagem_limiarizada_adaptativa = cv2.adaptiveThreshold(
    imagem_cinza, valor_maximo, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  
    cv2.THRESH_BINARY,  # Tipo de limiarização
    11, 
    2   
)

cv2.imshow("imagem",imagem_limiarizada_adaptativa)
cv2.waitKey(0)
cv2.destroyAllWindows()