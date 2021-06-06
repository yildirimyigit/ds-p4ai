from os import path


def read_products():
    if path.exists("/home/yigit/Desktop/products.txt"):
        f = open("/home/yigit/Desktop/products.txt", "r")

        for line in f:
            product_name_price = line.split("=")
            products[product_name_price[0]] = float(product_name_price[1].strip('\n'))
        f.close()


def write_products():
    f = open("/home/yigit/Desktop/products.txt", "w")
    for k in products:
        f.write(k + "=" + str(products[k]) + "\n")


def print_menu():
    print("1. Yeni ürün girişi")
    print("2. Ürün silme")
    print("3. Ürün listesi fiyat hesaplama")
    print("4. ÇIKIŞ")
    print("******")


def new_product(a, b):
    products[a] = b


def deleted_product(a):
    if a in products:
        products.pop(a)
    else:
        print("HATALI GİRİŞ")


def calculate_total(a):
    summ = 0
    for item in a:
        summ += products[item]
    return summ


products = dict()
read_products()
user_quit = False

while not user_quit:
    print_menu()
    choice = input("Seçim Yapınız: ")
    if choice == "1":
        product_name = input("Ürün adı giriniz: ")
        product_price = float(input("Ürün fiyatı giriniz: "))
        new_product(product_name, product_price)

    elif choice == "2":
        product_deleted = input("Silinicek ürünü seçin: ")
        deleted_product(product_deleted)

    elif choice == "3":
        user_input = input("Listeyi giriniz: ")
        stripped_ones = user_input.split(",")
        x = calculate_total(stripped_ones)
        print(x)

    elif choice == "4":
        user_quit = True
    else:
        print("HATALI GİRİŞ")


write_products()
