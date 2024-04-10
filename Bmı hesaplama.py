import tkinter as tk
from random import choice


def vki_hesapla():
    try:
        kilo = float(kilo_entry.get())
        boy = float(boy_entry.get()) / 100  # Boyu cm'den m'ye çevir

        vki = kilo / (boy * boy)

        if vki < 18:
            durum = "Zayıf"
            mesajlar = ["Kuvvetli olmak için biraz daha yemek yemelisin!", "Zayıf bir süper kahraman mısın"]
            emoji = "🍔🥗"
            text_color = "blue"
        elif 18 <= vki < 25:
            durum = "Normal"
            mesajlar = ["Mükemmel! Sağlıklı bir vücuda sahipsin.", "Dengeli beslenme her zaman iyidir!",
                        "Formundan ödün verme!"]
            emoji = "🍏🏋️‍♂️"
            text_color = "green"
        elif 25 <= vki < 30:
            durum = "Kilolu"
            mesajlar = ["Daha fazla hareket etmelisin!", "Fast food'u biraz azaltabilir misin?",
                        "Biraz kilo vermek iyi olabilir."]
            emoji = "🍔🏃‍♂️"
            text_color = "orange"
        else:
            durum = "Obez"
            mesajlar = ["Sağlığınız için doktora danışmayı düşünebilirsiniz.",
                        "Sağlıklı beslenme ve egzersiz yapmak önemlidir.", "Obezite ciddi bir sağlık sorunudur."]
            emoji = "🍔🚫"
            text_color = "red"

        sonuc_label.config(text="Vücut Kitle İndeksiniz: {:.2f}\nDurumunuz: {}".format(vki, durum), fg=text_color)
        mesaj_label.config(text=choice(mesajlar), fg=text_color)
        emoji_label.config(text=emoji)

        # Pencereyi belirli bir süre sonra kapat
        pencere.after(20000, pencere.destroy)  # 20 saniye sonra pencereyi kapat
    except ValueError:
        sonuc_label.config(text="Lütfen kilo ve boy için geçerli değerler giriniz.", fg="red")


# Ana pencere
pencere = tk.Tk()
pencere.title("BMI Hesaplayıcı")
pencere.geometry("400x400")  # Pencere boyutunu 300x400 piksel olarak ayarla

# Kilo Girişi
kilo_etiket = tk.Label(pencere, text="Kilo (kg):")
kilo_etiket.grid(row=0, column=0, padx=10, pady=10)
kilo_entry = tk.Entry(pencere)
kilo_entry.grid(row=0, column=1, padx=10, pady=10)

# Boy Girişi
boy_etiket = tk.Label(pencere, text="Boy (cm):")
boy_etiket.grid(row=1, column=0, padx=10, pady=10)
boy_entry = tk.Entry(pencere)
boy_entry.grid(row=1, column=1, padx=10, pady=10)

# Hesapla Düğmesi
hesapla_dugme = tk.Button(pencere, text="BMI Hesapla", command=vki_hesapla)
hesapla_dugme.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Sonuç Etiketi
sonuc_label = tk.Label(pencere, text="", font=("Arial", 12, "bold"))
sonuc_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Eğlenceli Mesaj Etiketi
mesaj_label = tk.Label(pencere, text="", font=("Arial", 10, "italic"))
mesaj_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Eğlenceli Emoji Etiketi
emoji_label = tk.Label(pencere, text="", font=("Segoe UI Emoji", 24))
emoji_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

pencere.mainloop()
