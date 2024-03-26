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

    if cx >= x and cx <= w and cy >= y and cy <= h:
        ...