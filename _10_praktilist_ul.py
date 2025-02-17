#10 ulesanne
for j in range(10):
     a1=float(input("essa arv: "))
     a2=float(input("teine arv: "))
     if a1>a2:
         print(f"suurem on {a1}")
     elif a1<a2:
         print(f"suurem on {a2}")



#18 ulesanne    
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

print()
#19 ulesanne
print("19")
for i in range(20, 51):
    ref=i/7
    if ref==2 or ref==5 or ref==7:
        print(i)

#31 ulesanne
try:
    K = int(input("skok koklet: "))
    M = int(input("skok pomestitsja na skovorodku: "))

    if M < 0:
        print("viga")
    else:
        skokmesta = (K + M - 1) // M 
        print(f"nado {skokmesta} skovorodok")
        ostanetsja =K%M
        print(f"na skovorodke ostanetsja {ostanetsja} mesta")
except:
    print("viga ")

#17 ulesanne
korrutis=2
korrutaja=0
for i in range(1,10):
    korrutaja+=1
    print(f"{korrutis} x {korrutaja} = {korrutis*korrutaja}")


#15 ulesanne
for j in range(10):
    for i in range(10):
        print(i,end=" ")
    print()
print()


#6 ulesanne
minus=0
plus=0
nullik=0
while True:
    try:
        n=int(input("sisesta n: "))
        if n>1:
            for i in range(1,n+1):
                arv66=float(input(f"sisesta arv {i}: "))
                if arv66<0:
                    minus+=1
                elif arv77>0:
                    plus+=1
                else:
                    null +=1
            print(f"miinuste arv: {minus}, plus arv: {plus}, null:{nullik}")
            break
        else:
            print("ne to")
    except:
        print("vale formaat")


#5 ulesanne
summa=0
while True:
    try:
        n=int(input("sisesta n: "))
        if n>1:
            for i in range(1,n+1):
                arv66=float(input(f"sisesta arv {i}: "))
                if arv66<0:
                    summa+=arv66
            print(f"summa vordub {summa}")
            break
        else:
            print("n peab olema suurem kui 1")
    except:
        print("vale formaat")

#3 ulesanne
summa2=1
for i in range(8):
    while True:
        try:
            aarv=int(input(f"sisesta arv {i+1}: "))
            if aarv>0:
                summa2=summa2*aarv
                print(f"summa {summa2}")
                break
            else:
                print("arv peab olema positiivne")
        except:
            print("see pole täisarv")



#2 ulesanne
summa=0
a=int(input("sisesta arv: "))
while True:
    try:
        if a>1:
            for i in range(1,a+1):
                summa=summa+arv
                print(f"summa vordub {summa}-ga")
            break
        else:
            print('arv peab olema suurem kui 1')
    except:
        print('see pole täisaarv')


#1 ulesanne
täisarv=0
for i in range(5):
    while True:
        try:
            arv=float(input(f"sisesta {i+1} arv: "))
            break
        except:
            print("kirjuta ainult numbrid")
    if arv==int(arv):
        täisarv+=1
print(f"taisarvude kogus: {täisarv}")