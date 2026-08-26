import colorsys

def cor_complementar(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """
    # 1) normaliza RGB para 0-1
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # 2) RGB -> HSV (H em 0-1, nao graus)
    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    # 3) soma 180 graus ao matiz
    # (equivale a somar 0.5)
    h_complementar = (h + 0.5) % 1.0
    
    # 4) converte de volta,
    # mantendo S e V
    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_complementar, s, v)

    # 5) desnormaliza para 0-255
    return (round(r2 * 255),
            round(g2 * 255),
            round(b2 * 255))

def cor_analoga(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """
    # 1) normaliza RGB para 0-1
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # 2) RGB -> HSV (H em 0-1, nao graus)
    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    # 3) soma 180 graus ao matiz
    # (equivale a somar 0.5)
    angulo = 30/360
    h_analogo = (h + angulo) % 1.0
    h_analogo2 = (h - angulo) % 1.0
    # 4) converte de volta,
    # mantendo S e V
    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_analogo, s, v)

    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_analogo2, s, v)

    rr2 = round(r2 * 255)
    rg2 = round(g2 * 255)
    rb2 = round(b2 * 255)

    rr3 = round(r3 * 255)
    rg3 = round(g3 * 255)
    rb3 = round(b3 * 255)

    # 5 desnormaliza para 0-255
    return (rr2,rg2,rb2,rr3,rg3,rb3)


def cor_triadica(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """
    # 1) normaliza RGB para 0-1
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # 2) RGB -> HSV (H em 0-1, nao graus)
    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    # 3) soma 180 graus ao matiz
    # (equivale a somar 0.5)
    angulo = 120/360
    h = h % 1.0
    h_triadico2 = (h + angulo) % 1.0
    h_triadico3 = (h - angulo) % 1.0
    # 4) converte de volta,
    # mantendo S e V
    
    r1, g1, b1 = colorsys.hsv_to_rgb(
            h, s, v)

    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_triadico2, s, v)

    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_triadico3, s, v)

    r1 = round(r1 * 255)
    g1 = round(g1 * 255)
    b1 = round(b1 * 255)

    rr2 = round(r2 * 255)
    rg2 = round(g2 * 255)
    rb2 = round(b2 * 255)

    rr3 = round(r3 * 255)
    rg3 = round(g3 * 255)
    rb3 = round(b3 * 255)

    # 5 desnormaliza para 0-255
    return (r1, g1, b1, rr2,rg2,rb2,rr3,rg3,rb3)



def cor_split(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """
    # 1) normaliza RGB para 0-1
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # 2) RGB -> HSV (H em 0-1, nao graus)
    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    # 3) soma 180 graus ao matiz
    # (equivale a somar 0.5)
    angulo = 150/360
    h_split = (h + angulo) % 1.0
    h_split2 = (h - angulo) % 1.0
    # 4) converte de volta,
    # mantendo S e 
    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_split, s, v)

    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_split2, s, v)

    rr2 = round(r2 * 255)
    rg2 = round(g2 * 255)
    rb2 = round(b2 * 255)

    rr3 = round(r3 * 255)
    rg3 = round(g3 * 255)
    rb3 = round(b3 * 255)

    # 5 desnormaliza para 0-255
    return (rr2,rg2,rb2,rr3,rg3,rb3)

def cor_triadica(r, g, b):
    """
    Recebe uma cor RGB (0-255) e retorna
    sua cor complementar, girando o matiz
    (H) em 180 graus no circulo cromatico.
    """
    # 1) normaliza RGB para 0-1
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # 2) RGB -> HSV (H em 0-1, nao graus)
    h, s, v = colorsys.rgb_to_hsv(
        r_norm, g_norm, b_norm)

    # 3) soma 180 graus ao matiz
    # (equivale a somar 0.5)
    angulo = 60/360
    h = h % 1.0
    h_2 = (h + angulo) % 1.0
    h_3 = (h + 3*angulo) % 1.0
    h_4 = (h - 2*angulo) % 1.0
    # 4) converte de volta,
    # mantendo S e V
    
    r1, g1, b1 = colorsys.hsv_to_rgb(
            h, s, v)

    r2, g2, b2 = colorsys.hsv_to_rgb(
        h_2, s, v)

    r3, g3, b3 = colorsys.hsv_to_rgb(
        h_3, s, v)

    rr2 = round(r2 * 255)
    rg2 = round(g2 * 255)
    rb2 = round(b2 * 255)

    rr3 = round(r3 * 255)
    rg3 = round(g3 * 255)
    rb3 = round(b3 * 255)

    rr4 = round(r3 * 255)
    round(g3 * 255)
    round(b3 * 255)

    # 5 desnormaliza para 0-255
    return (r1, g1, b1, rr2,rg2,rb2,rr3,rg3,rb3)



# Exemplo de uso:
cor_original = (230, 57, 70)  # um vermelho
cores_comp = cor_complementar(*cor_original)
cores_analogas = cor_analoga(*cor_original)
triade = cor_triadica(*cor_original)
split = cor_split(*cor_original)




print(f"Original:     RGB{cor_original}")
print(f"Complementar: RGB{cores_comp}")
print(f"Analogas: RGB{cores_analogas[0:3]} RGB{cores_analogas[3:6]}")
print(f"Triade: RGB{triade[0:3]} RGB{triade[3:6]}  RGB{triade[6:9]}")
print(f"Split: RGB{split[0:3]} RGB{split[3:6]}")


# Saida:
# Original:     RGB(230, 57, 70)
# Complementar: RGB(57, 230, 217)