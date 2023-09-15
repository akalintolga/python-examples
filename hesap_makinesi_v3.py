def hesap_makinesi():
    while True:
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
            islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")
            if islem == "+":
                print(sayi1, "+", sayi2, "=", sayi1+sayi2)
            elif islem == "-":
                print(sayi1, "-", sayi2, "=", sayi1-sayi2)
            elif islem == "*":
                print(sayi1, "*", sayi2, "=", sayi1*sayi2)
            elif islem == "/":
                print(sayi1, "/", sayi2, "=", sayi1/sayi2)
            else:
                print("Lütfen geçerli bir işlem seçin.")
            devam = input("Devam etmek istiyor musunuz? (E/H): ")
            if devam.upper() == "H":
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
