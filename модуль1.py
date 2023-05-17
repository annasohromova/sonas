from module1 import *

laused=[] 
while True:
    menu=input("\n1-Sõnade tõlkimine \n2-Vaata sõnastikku \n3-Parandage viga sõnastikus")
    while menu.isdigit()==False:
        menu=input("Kirjuta ainult need numbrid, mis on ")
    print()
    if menu=="1":
        translate_word("rus.txt","est.txt")
    elif menu=="2":
        laused=loe_failist("rus.txt")
        for line in laused:
            print(line)
        print()
        laused=loe_failist("est.txt")
        for line in laused:
            print(line)
    elif menu=="3":
        edit_word("rus.txt","est.txt")
    elif menu=="4":
        add_word("rus.txt","est.txt")

