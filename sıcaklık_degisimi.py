# Seçim Ekranı
print("""*****Lütfen Seçim yapınız.
1. Celcius --> Kelvin
2. Celcius --> Fahrenheit
3. Fahrenhit --> Celcius
4. Fahrenheit --> Kelvin
5. Kelvin --> Celcius
6. Kelvin --> Fahrenheit

* Programdan çıkış yapmak için "x" tuşuna basınız.
*****""")
while True:

    secim=input("Lütfen Seçim Yapınız..")
    if (secim=="x"):
        print("Çıkılıyor")
        break
    elif (secim=="1"):
       celcius=float(input("Lütfen Celcius Değeri Giriniz: "))
       kelvin=(celcius+273.15)
       print("{} Celcius {} Kelvin değerine eşittir.".format(celcius,kelvin))
    elif (secim=="2"):
       celcius=float(input("Lütfen Celcius Değeri Giriniz: "))
       fahrenheit=((celcius*9)/5)+32
       print("{} Celcius {} Fahrenheit değerine eşittir.".format(celcius,fahrenheit))
    elif (secim=="3"):
        fahrenheit=float(input("Lütfen Fahrenheit Değeri Giriniz: "))
        celcius=((fahrenheit-32)*5)/9
        print("{} Fahrenheit {} Celcius değerine eşittir.".format(fahrenheit,celcius))
    elif (secim=="4"):
        fahrenheit=float(input("Lütfen Fahrenheit Değeri Giriniz: "))
        kelvin=(((fahrenheit-32)*5)/9)+273
        print("{} Fahrenheit {} Kelvin değerine eşittir.".format(fahrenheit,kelvin))
    elif (secim=="5"):
        kelvin=float(input("Lütfen Kelvin Değeri Giriniz: "))
        celcius=(kelvin-273)
        print("{} Kelvin {} Celcius değerine eşittir.".format(kelvin,celcius))
    elif (secim=="6"):
        kelvin=float(input("Lütfen Kelvin Değeri Giriniz: "))
        fahrenheit=(((kelvin-273)*9)/5)+32
        print("{} Kelvin {} Fahrenheit değerine eşittir.".format(kelvin,fahrenheit))

    else:
         print("Hatalı bir seçim yaptınız. Lütfen tekrar deneyiniz.")


