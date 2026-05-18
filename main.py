products = [
    ["Laptop", 25000, 5],
    ["Mouse", 500, 10],
    ["Klavye", 1200, 8],
    ["Kulaklık", 2000, 6],
    ["Monitör", 7000, 4]
]

cart = []

while True:
    print("\n===== E-TİCARET MENÜSÜ =====")
    print("1. Ürünleri Göster")
    print("2. Sepete Ürün Ekle")
    print("3. Sepeti Göster")
    print("4. Sepetten Ürün Çıkar")
    print("5. Siparişi Tamamla")
    print("6. Çıkış")

    option = input("Bir seçenek girin: ")

    if option == "1":
        print("\n--- ÜRÜN LİSTESİ ---")
        for i, product in enumerate(products, start=1):
            print(
                str(i) + ". " +
                product[0] +
                " - Fiyat: " + str(product[1]) +
                " TL - Stok: " + str(product[2])
            )

    elif option == "2":
        print("\n--- ÜRÜN LİSTESİ ---")
        for i, product in enumerate(products, start=1):
            print(
                str(i) + ". " +
                product[0] +
                " - Fiyat: " + str(product[1]) +
                " TL - Stok: " + str(product[2])
            )

        choice = input("Ürün numarasını girin: ")

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= len(products):
                quantity = input("Kaç adet almak istiyorsunuz? ")

                if quantity.isdigit():
                    quantity = int(quantity)
                    selected_product = products[choice - 1]

                    if quantity <= 0:
                        print("Adet 0'dan büyük olmalıdır.")
                    elif quantity > selected_product[2]:
                        print("Yeterli stok yok.")
                    else:
                        found = False

                        for item in cart:
                            if item[0] == selected_product[0]:
                                item[2] = item[2] + quantity
                                found = True
                                break

                        if found == False:
                            cart.append([selected_product[0], selected_product[1], quantity])

                        selected_product[2] = selected_product[2] - quantity
                        print(str(quantity) + " adet " + selected_product[0] + " sepete eklendi.")
                else:
                    print("Geçerli bir adet girin.")
            else:
                print("Geçersiz ürün numarası.")
        else:
            print("Geçerli bir sayı girin.")

    elif option == "3":
        print("\n--- SEPETİNİZ ---")
        if len(cart) == 0:
            print("Sepetiniz boş.")
        else:
            total = 0
            for item in cart:
                item_total = item[1] * item[2]
                total = total + item_total
                print(item[0] + " - " + str(item[2]) + " adet - Toplam: " + str(item_total) + " TL")
            print("Genel Toplam:", total, "TL")

    elif option == "4":
        print("\n--- SEPETİNİZ ---")
        if len(cart) == 0:
            print("Sepetiniz boş.")
        else:
            total = 0
            for item in cart:
                item_total = item[1] * item[2]
                total = total + item_total
                print(item[0] + " - " + str(item[2]) + " adet - Toplam: " + str(item_total) + " TL")
            print("Genel Toplam:", total, "TL")

            name = input("Çıkarmak istediğiniz ürün adını girin: ").strip().lower()
            removed = False

            for i in range(len(cart)):
                if cart[i][0].lower() == name:
                    removed_item = cart[i]

                    for product in products:
                        if product[0] == removed_item[0]:
                            product[2] = product[2] + removed_item[2]

                    cart.pop(i)
                    removed = True
                    print("Ürün sepetten çıkarıldı.")
                    break

            if removed == False:
                print("Sepette bu ürün bulunamadı.")

    elif option == "5":
        if len(cart) == 0:
            print("Sepetiniz boş.")
        else:
            print("\n--- SİPARİŞ ÖZETİ ---")
            total = 0
            for item in cart:
                item_total = item[1] * item[2]
                total = total + item_total
                print(item[0] + " - " + str(item[2]) + " adet - Toplam: " + str(item_total) + " TL")

            print("Ödenecek Toplam:", total, "TL")
            confirm = input("Siparişi onaylıyor musunuz? (evet/hayır): ").strip().lower()

            if confirm == "evet":
                print("Sipariş başarıyla tamamlandı.")
                cart.clear()
            elif confirm == "hayır":
                print("Sipariş iptal edildi.")
            else:
                print("Geçersiz cevap girdiniz.")

    elif option == "6":
        print("Uygulamadan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Tekrar deneyin.")
