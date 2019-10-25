count=999
while count<1000:
    x=count
    y=998
    while y>0:
        deger=x*y
        yazi=str(deger)
        i=len(str(deger))
        Sayilar = []
        for x in yazi:
            Sayilar.append(x)
        print(deger)
        if deger>99999:
            if Sayilar[0]==Sayilar[5] and Sayilar[1]==Sayilar[4] and Sayilar[2]==Sayilar[3]:
                    print(deger)
                    print(count)
                    break
    y-=1
count-=1

