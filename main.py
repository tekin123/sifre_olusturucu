import random

karakterler = "+-/*!&$?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

count = int(input("kaç karakterli bir şifre istersin:"))

sifre = ""

for i in range(count):
    sifre += random.choice(karakterler)

print(sifre)
print("bu şifreyi kopyalıyıp istediğiniz yere yapıştırın")