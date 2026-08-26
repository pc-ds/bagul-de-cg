from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("robozao.jpeg")
grey = img.convert("L")
grey.save("robozaocinza.jpeg")
largura, altura = grey.size
pixels = grey.load()
imagem = [[pixels[x, y] for x in range(largura)] for y in range(altura)]

def histograma(imagem):
    largura, altura = imagem.size
    vetor = [0] * 256
    for x in range(largura):
        for y in range(altura):
            i = imagem.getpixel((x,y))
            vetor[i] += 1 
    return vetor

def limiarizar(imagem, T):
    largura, altura = imagem.size
    saida = [[0] * altura for _ in range(largura)]
    for x in range(largura):
            for y in range(altura):
                if imagem.getpixel((x,y)) > T:
                     saida[x][y] = 255
                else:
                     saida[x][y] = 0
    return saida

def equalizar(imagem):
    h = histograma(imagem)
    largura, altura = imagem.size
    N = largura*altura

    cdf = [0] * 256
    soma = 0
    for i in range (255):
        soma += h[i]
        cdf[i] = soma

    nova = [0] * 255
    for i in range (255):
        nova[i] = round(cdf[i]*255/N)

    saida = [[0] * altura for _ in range(largura)]
    for x in range (largura):
            for y in range (altura):
                saida[x][y] = nova[imagem.getpixel((x,y))]
    return saida
                 
def aplicar_kernel(imagem, kernel):
    altura, largura = len(imagem), len(imagem[0])
    k = len(kernel)
    borda = k // 2
    saida = [[0]*largura for _ in range(altura)]
    for y in range(borda, altura-borda):
        for x in range(borda, largura-borda):
            soma = 0.0
            for i in range(k):
                iy = y + i - borda
                row = imagem[iy]
                for j in range(k):
                    ix = x + j - borda
                    soma += row[ix] * kernel[i][j]
            saida[y][x] = max(0, min(255, round(soma)))
    return saida
kernel_media = [[1/9]*3 for _ in range(3)]
imagem_media = aplicar_kernel(imagem, kernel_media)

h = histograma(grey)

plt.bar(range(256), h)
plt.xlabel("Intensidade de cinza")
plt.ylabel("Número de pixels")
plt.title("Histograma")
plt.show()

plt.imshow(imagem_media, cmap = "gray")
plt.axis("off")
plt.show()



resultado = limiarizar(grey, 80)

plt.imshow(resultado, cmap = "gray")
plt.axis("off")
plt.show()


'''
resultado_eq = equalizar(grey)

def criar_grafico(sla):
     plt.bar(len(sla), sla)
     plt.show()

criar_grafico(histograma(grey))
'''