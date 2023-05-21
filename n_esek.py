anna = ("Anna", 16, True, ["Piros", "Kék"])

print(anna)
print("szeméj neve és életkora: ", anna[0: 2])
print("Infók száma a szeméjről: ", len(anna))
anna[3][0] = "sárga"

print(anna[-1])
anna = anna[0], 20, anna[2:4]
print(anna[1])

gabor = "Gábor", anna[1:4]
print(gabor)
