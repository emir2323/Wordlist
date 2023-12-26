import random
import string


kelime_uzunlugu = int(input("Kelimenin uzunluğunu girin: "))
sozluk_karakterleri = input("Kelimede hangi karakterlerin olmasını istersiniz (örnek: abc123)? ")
tekrar_etme_sayisi = int(input("Harf/rakam tekrar etme sayısını girin: "))


karakterler = list(sozluk_karakterleri)


wordlist = []

def generate_words(word, depth):
    if depth == kelime_uzunlugu:
        wordlist.append(word)
        return
    for char in karakterler:
        generate_words(word + char, depth + 1)

generate_words('', 0)


random.shuffle(wordlist)


hedef_parola = input("Hocanın belirlediği parolayı girin: ")
if hedef_parola in wordlist:
    pozisyon = wordlist.index(hedef_parola)
    print(f"Parola wordlist içinde bulundu. Pozisyon: {pozisyon + 1}")
else:
    print("Parola wordlist içinde bulunamadı.")


with open("wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("Wordlist başarıyla 'wordlist.txt' dosyasına yazıldı.")