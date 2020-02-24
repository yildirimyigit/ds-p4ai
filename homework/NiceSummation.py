# nice_sum fonksyonu size verilmis durumda. Bu fonksyon
# kendisine gonderilen bir sayi listesi icerisinde, yanyana bulunan elemanlarin
# buyuk olanlarindan yeni bir liste olusturup, olusturulan listedeki elemanlari
# ve toplamlarini donduruyor.

# Ornek: bir 1,  4,  3,  2,  5 listesi icin
#     MAX     \ / \ / \ / \ /
#   CIKTI-1    4   4   3   5
#               \__|   |__/
#     SUM           \_/
#   CIKTI-2         16

# 1) Verilen herhangi bir liste icin, elemanlarini nasil siralarsak nice_sum operasyonu
#    sonucu en buyuk degerini alir?
# 2) Yukarida olusturdugunuz matematiksel cozumu, donguler ve liste operasyonlari kullanarak
#    kodlayiniz.


def nice_sum(arr):
    max_arr = [max(l, r) for l, r in zip(arr[1:], arr[:-1])]
    return max_arr, sum(max_arr)


print(nice_sum([1, 4, 3, 2, 5]))


def nice_sum(arr):
    max_arr = [max(l, r) for l, r in zip(arr[1:], arr[:-1])]
    return max_arr, sum(max_arr)

# kullanicidan deger oku, "," lerden ayir ve her bir karakteri sayiya cevir
list_a = [int[char] for char in input("bir liste giriniz: ").split(',')]

# kullanici listesini sirala
list_a.sort()
# Bos sonuc listesi olustur
res = []
# Listenin ortasina kadar gidecek olan bir dongu tanimla
for i in range(int(len(list_a)/2)):
    # orta noktaya gelene kadar bastan ve sondan (en kucuk ve en buyuk) elemanlari sirayla ekle
    res.extend([list_a[i], list_a[len(list_a)-1-i]])
# Uzunlugu tek sayi olan bir liste verilmis ise eklenmemis olan ortadaki elemani ekle
if len(list_a)%2==1:
    res.append(list_a[int(len(list_a)/2)])

res
nice_sum(res)
