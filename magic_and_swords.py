t = int(input("Insira o número de casos testes: "))

magias = ["fire", "water", "earth", "air"]
dano = [200, 300, 400, 100]
lv1 = [20, 10, 25, 18]
lv2 = [30, 25, 55, 38]
lv3 = [50, 40, 70, 60]

dict_dano = dict(zip(magias, dano))
dict_lv1 = dict(zip(magias, lv1))
dict_lv2 = dict(zip(magias, lv2))
dict_lv3 = dict(zip(magias, lv3))

for i in range(t):
    w, h, x, y = map(int, input().split())
    magia, nivel, cx, cy = input().split()
    dict_da_vez = None
    nivel = int(nivel)
    cx = int(cx)
    cy = int(cy)
    
    if nivel == 1:
        dict_da_vez = dict_lv1
    elif nivel == 2:
        dict_da_vez = dict_lv2
    elif nivel == 3:
        dict_da_vez = dict_lv3

    deuDano = False
    raio = dict_da_vez[magia]
    dano = dict_dano[magia]
    
    if cx <= w and cy <= h:
        deuDano = True
    elif cx > w:
        if (cx - w) <= w:
            deuDano = True
    elif cy > h:
        if (cy - h) <= h:
            deuDano = True 

    if deuDano:
        print(dano)
    else:
        print(0)