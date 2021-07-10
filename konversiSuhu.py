pilihan = input("Pilih suhu yang ingin anda ubah: [C/R/F/K]" )
if pilihan == "C": 
    C = int(input("Masukkan nilai suhu Celsius: "))
    cUbahKe = input("ubah ke?[R/F/K] ")
    if cUbahKe == "R":
        R = (4/5)*C
        print("Konversi suhu",C, "C ke Reamur adalah",R,"R")
    elif cUbahKe == "F":
        F = (9/5)*C + 32
        print("Konversi suhu",C, "C ke Fahrenheit adalah",F,"F")
    elif cUbahKe == "K":
        K = C + 273
        print("Konversi suhu",C, "C ke Kelvin adalah",K,"K")
    else:
        print("Konversi suhu yang anda masukkan tidak sesuai dengan [R/F/K]")
elif pilihan == "R":
    R = int(input("Masukkan nilai suhu Reamur: "))
    rUbahKe = input("ubah ke?[C/F/K] ")
    if rUbahKe == "C":
        C = (5/4)*R
        print("Konversi suhu",R, "R ke Celcius adalah",C,"C")
    elif rUbahKe == "F":
        F = (9/4)*R + 32
        print("Konversi suhu",R, "R ke Fahrenheit adalah",F,"F")
    elif rUbahKe == "K":
        K = (5/4)*R + 273
        print("Konversi suhu",R, "R ke Kelvin adalah",K,"K")
    else:
        print("Konversi suhu yang anda masukkan tidak sesuai dengan [C/F/K]")
elif pilihan == "F":
    F = int(input("Masukkan nilai suhu Fahrenheit: "))
    fUbahKe = input("ubah ke?[C/R/K] ")
    if fUbahKe == "C":
        C = (5/4)*(F-32)
        print("Konversi suhu",F, "F ke Celcius adalah",C,"C")
    elif fUbahKe == "R":
        R = (4/9)*(F-32)
        print("Konversi suhu",F, "F ke Reamur adalah",R,"R")
    elif fUbahKe == "K":
        K = (5/9)*(F-32) + 273
        print("Konversi suhu",F, "F ke Kelvin adalah",K,"K")
    else:
        print("Konversi suhu yang anda masukkan tidak sesuai dengan [C/R/K]")

elif pilihan == "K":
    K = int(input("Masukkan nilai suhu Kelvin: "))
    kUbahKe = input("ubah ke? [C/R/F] ")
    if kUbahKe == "C":
        C = K - 273
        print("Konversi suhu",K, "K ke Celcius adalah",C,"C")
    elif kUbahKe == "R":
        R = (4/5)*(K - 273)
        print("Konversi suhu",K, "K ke Reamur adalah",R,"R")
    elif kUbahKe == "F":
        F = (9/5)*(K - 273) + 32
        print("Konversi suhu",K, "K ke Fahrenheit adalah",F,"F")
    else:
        print("Konversi suhu yang anda masukkan tidak sesuai dengan [C/R/K]")
else:
    print("Pilihan tidak sesuai dengan [C/R/F/K]")
