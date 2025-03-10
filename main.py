def winda_lumon(pietra, zakazane):
         for i in range(len(zakazane)):
             pietra.remove(zakazane[i])
         return pietra


pietra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

zakazane = [2,6,7]

print(winda_lumon(pietra, zakazane))