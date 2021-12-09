while True:
    print("""
             1-O'yinchi qo'shish,
             2-Komandani ko'rish,
             3-Komanda faylini bo'shatish,'
             4-Chiqish,""")
    n=int (input("Amalni kiriting: --> "))
    if n==1:
        
        kam=input("Komanda nomi: ")
        while True:
            name=input("O'yinchi ismi: ")
            num=input("O'yinchi raqami: ")
            with open (f"{kam}.txt",'a') as fil1:
                fil3=open(f"{kam}.txt",'r')
                d=fil3.readlines()
                jami=fil3.read()
                s=0
                for i in d:
                    s+=1
                    print(s)
                if name not in jami:
                    s=str(s)
                    player=s+'.'+name+'-'+num+'\n'
                    fil1.write(player)
                else:
                    print("Bu ismli o'yinchi bor!")
                   
            xa=input("Yana o'yinchi kiritasizmi?   ha/yo'q  \n--> " )
            if xa=="yo'q":
                break
        
    elif n==2:
        try:
            kom=input("Komandani nomi: ")
            fil2=open(f"{kom}.txt","r")
            All=fil2.read()
            if All=='':
                print("Komanda ro'yxatida o'yinchi yo'q!")
            else:
                print(All)
                fil2.close()
        except:
            print("Bunday komanda to'q!")

    elif n==3:
        try:
            koma=input("Komandani nomi: ")
            with open(f"{koma}.txt","r") as fill:
                fill.read()                
            fil4=open(f"{koma}.txt","w")
            fil4.write('') 
            fil4.close()
            print(f"{koma} fayli bo'shatildi!")
        except:
            print("Bunday komanda yo'q!")
        
    elif n==4:
        break
    else:
        print("Amalni qayta tanlang. ")
