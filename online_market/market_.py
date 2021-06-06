from datetime import date

from customer import Customer
from product import Product


def print_first_menu():
    print("***Ana Menu***")
    print("1. Urun")
    print("2. Kullanici")
    print("3. Kullanici Siparis")
    print("4. ÇIKIŞ")
    print("**************")


def print_product_menu():
    print("1. Yeni ürün girişi")
    print("2. Stok ekleme")
    print("3. Ürün silme")
    print("4. ÇIKIŞ")
    print("******")


def print_customer_menu():
    print("1. Yeni kullanici girişi")
    print("2. Kullanici silme")
    print("3. ÇIKIŞ")
    print("******")


def check_depo(urunler):
    urun_list = urunler.split(",")
    elimde_olanlar = []

    for urun in urun_list:
        for prod in products:
            if urun == prod.name:
                elimde_olanlar.append(urun)
                break

    return elimde_olanlar




products = []
customers = []

print('*** Hosgeldiniz ***')
uq = False

while not uq:
    print_first_menu()
    choice = input('Seciminiz: \n')

    if choice == '1':
        print_product_menu()
        new_choice = input('Seciminiz: \n')

        if new_choice == '1':
            n = input('Urun Adi: ')
            b = input('Marka (Varsa): ')
            p = float(input('Birim Fiyati: '))
            bb = input('SKT: ')
            a = float(input('Stok Miktari: '))

            temp_product = Product(n, b, a, bb, p)
            products.append(temp_product)

        elif new_choice == "2":
            product_name = input("Stogu artirilacak urun: ")
            prod_amount = float(input("Eklenecek miktari giriniz: "))

            msg = ""
            for prod in products:
                if product_name == prod.name:
                    prod.add_inventory(prod_amount)
                    msg = "Toplam: " + str(prod.amount)
                    break
                else:
                    msg = "Urun bulunamadi"

            print(msg)

        elif new_choice == "3":
            pass
        elif new_choice == "4":
            uq = True
        else:
            print('Hatali secim')

    elif choice == '2':
        print_customer_menu()
        new_choice = input('Seciminiz: \n')

        if new_choice == '1':
            isim = input('Musteri Adi: ')
            soyad = input('Musteri Soyadi: ')
            tel = input('Telefon: ')
            musteri_adres = input('Adres: ')
            kayit_zamani = date.today()
            son_alisveris_zamani = ""

            temp_customer = Customer(isim, soyad, tel, musteri_adres, kayit_zamani, son_alisveris_zamani)
            customers.append(temp_customer)
            print("Musteri girildi")

    elif choice == '3':
        musteri = input("Musteri Telefon: ")
        siparis = input("Urunleri giriniz: ")

        olanlar = check_depo(siparis)

        found = False
        price = 0
        for c in customers:
            if c.phone == musteri:
                price = c.shop(olanlar)
                found = True
                break

        if found:
            print(price)

    elif choice == '4':
        uq = True

    else:
        print('Hatali secim')

print("*** Hoscakalin ***")







# cust0 = Customer()
# cust0.name = 'vedude rabia'
# cust0.surname = 'sozkesen'
# cust0.phone = ...
#
# cust1 = Customer()
# ...
#
# prod0 = Product()
# prod0.name = 'havuc'
# prod0.amount = 25
# prod0.bb = "2021.09.15"
# prod0.price_per_unit = 4.87

# prod0 = Product('havuc', 25, '2021.09.15')
# v = Customer('vedude rabia', 'sozkesen', '05349771294', 'ds mahallesi ...')
# kagan = Customer('muzaffer kagan', 'uzun', '04649771294', 'mh mahallesi ...')


