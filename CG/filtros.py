from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("robozao.jpeg")
grey = img.convert("L")
grey.save("robozaocinza.jpeg")
largura, altura = grey.size

# Convertendo a imagem PIL para matriz bidimensional [y][x]
pixels = grey.load()
imagem = [[pixels[x, y] for x in range(largura)] for y in range(altura)]

def histograma(img_matriz):
    alt = len(img_matriz)
    larg = len(img_matriz[0])
    vetor = [0] * 256
    for y in range(alt):
        for x in range(larg):
            i = img_matriz[y][x]
            vetor[i] += 1 
    return vetor

def limiarizar(img_matriz, T):
    alt = len(img_matriz)
    larg = len(img_matriz[0])
    saida = [[0] * larg for _ in range(alt)]
    for y in range(alt):
        for x in range(larg):
            if img_matriz[y][x] > T:
                saida[y][x] = 255
            else:
                saida[y][x] = 0
    return saida

def equalizar(img_matriz):
    h = histograma(img_matriz)
    alt = len(img_matriz)
    larg = len(img_matriz[0])
    N = largura * altura

    cdf = [0] * 256
    soma = 0
    for i in range(256):
        soma += h[i]
        cdf[i] = soma

    nova = [0] * 256
    for i in range(256):
        nova[i] = round(cdf[i] * 255 / N)

    saida = [[0] * larg for _ in range(alt)]
    for y in range(alt):
        for x in range(larg):
            saida[y][x] = nova[img_matriz[y][x]]
    return saida
                 
def aplicar_kernel(img_matriz, kernel):
    altura_m, largura_m = len(img_matriz), len(img_matriz[0])
    k = len(kernel)
    borda = k // 2
    saida = [[0] * largura_m for _ in range(altura_m)]
    for y in range(borda, altura_m - borda):
        for x in range(borda, largura_m - borda):
            soma = 0
            for i in range(k):
                iy = y + i - borda
                row = img_matriz[iy]
                for j in range(k):
                    ix = x + j - borda
                    soma += row[ix] * kernel[i][j]
            saida[y][x] = max(0, min(255, round(soma)))
    return saida

kernel_media = [[1/9, 1/9, 1/9], 
                [1/9, 1/9, 1/9], 
                [1/9, 1/9, 1/9]]

imagem_media = aplicar_kernel(imagem, kernel_media)
imagem_limiarizada = limiarizar(imagem, 80)
imagem_equalizada = equalizar(imagem)

plt.subplot(2, 2, 1)
plt.imshow(grey, cmap="gray")
plt.title("Imagem Original (Cinza)")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(imagem_limiarizada, cmap="gray")
plt.title("Threshold")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(imagem_media, cmap="gray")
plt.title("Filtro de Média")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(imagem_equalizada, cmap="gray")
plt.title("Equalização")
plt.axis("off")

plt.tight_layout()
plt.show()