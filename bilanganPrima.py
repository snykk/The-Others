N = int(input(""))

if 1<=N<=100:
    prima = True
    for b in range(2, N-1):
        if N%b==0:
            prima = False
    if N == 1:
        print("boh bukan prima")
    elif prima == True:
        print("yay, aku prima")
    else:
        print("boh bukan prima")
        
