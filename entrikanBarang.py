total = 0
command = "y"
unexpectedChar = list()
while True:
    if command == "y":
        jumlahBarang = int(input("Entrikan jumlah barang yang dibeli: "))
        hargaBarang = int(input("Entrikan harga satuan barang: "))
        total += jumlahBarang * hargaBarang
    elif command == "t":
        print("Total pembayaran: Rp", "{:,}".format(total))
        break
    else:
        unexpectedChar.append(command)
    command = input("apakah ada lagi item barang yang akan dientrikan atau tidak?[y/t]")
a = -1
for b in unexpectedChar:
    for i in b:
        a +=1
        print("Karakter salah indeks ke",str(a), "adalah", b)
