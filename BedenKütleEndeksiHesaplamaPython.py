kütle=input("Lütfen kütlenizi giriniz:")
boy=input("Lütfen boyunuzu giriniz metre cinsinden :")
kütle= float (kütle)
boy= float (boy)
Bki=kütle/(boy**2)
if Bki<18.5:
    print("Zayıf grubundasınız.")
elif Bki>=18.5 and Bki<24.9:
    print("Normal grubundasınız.")
elif Bki>=25 and Bki<29.9:
    print("Fazla kilolu grubundasınız.")
elif Bki>=30 and Bki<39.9:
    print("Şişman grubundasınız.")
elif Bki>40:
    print("Obez grubundasınız.")
else:
    print("Hatalı giriş!")
