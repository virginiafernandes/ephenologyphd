import cv2
import numpy as np
from matplotlib import pyplot as plt

imagemTuring = cv2.imread("turing.jpg")
print imagemTuring.shape
print imagemTuring.item(0, 0, 2), imagemTuring.item(0, 0, 1), imagemTuring.item(0, 0, 0)

imagemTuring.itemset((0, 0, 2), 255)
imagemTuring.itemset((0, 0, 1), 0)
imagemTuring.itemset((0, 0, 0), 0)

bola = imagemTuring[180:250, 250:315]
cv2.imwrite("bola.jpg", bola)
imagemTuring[130:200, 200:265] = bola

#cv2.imwrite("turing.jpg", imagemTuring)

#Histogram
img = cv2.imread("turing.jpg")
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
cv2.imshow("Imagem Original", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

