#menghitung nilai rata rata suatu himpunan
def rataRata(himpunan):
    return sum(himpunan)/len(himpunan)
himpunan = list()
a = int(input("banyaknya data: "))
for b in range(a):
    b = int(input("Masukkan nilai: "))
    himpunan.append(b)
print("Rata rata nilai adalah", rataRata(himpunan))
