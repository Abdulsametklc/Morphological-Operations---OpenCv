# Erozyon, genişleme, açma, kapatma ve morfolojik gradyan
# Erozyon ön plandaki nesnenin sınırlarını aşındırır
# Genişleme erozyonun tam tersi
# Açma = Erozyon + Genişleme
# Kapatma = Genişleme + Erozyon, açmanın tam tersi
# Morfolojik Gradyan = Bir görüntünün genişlemesi ve erozyonu arasındaki fark

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içer aktar
img = cv2.imread("datai_team.jpg",0)
plt.figure(), plt.imshow(img, cmap ="gray"), plt.axis("off"), plt.title("Orijinal")

#Erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1) # İterasyon arttıkça daha çok küçülme olacaktır.
plt.figure(), plt.imshow(result, cmap ="gray"), plt.axis("off"), plt.title("Erozyon")

#Genişleme dilation
result2 = cv2.dilate(img, kernel, iterations = 2) # iterasyon arttıkça daha çok büyüme olacaktır.
plt.figure(), plt.imshow(result2, cmap ="gray"), plt.axis("off"), plt.title("Genişleme")

# white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise")

noise_img = whiteNoise + img 
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("with white noise")

#Açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("opening")

#black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = whiteNoise*(-255)
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise")

black_noise_img = blackNoise + img 
black_noise_img[black_noise_img <= -245] = 0 
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise img")

#kapatma
closing = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("closing")


# Morfolojik Gradyan, gradient 
gradient =cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("gradient")
