# Dijital Oyun Tasarımı - Oyun Projesi Süre ve Maliyet Hesaplayıcı
# Kullanılan veri tipleri: str, int, float, bool

# Kullanıcıdan oyun adını metin (str) olarak alıyoruz
oyun_adi = input("Oyun projesinin adı nedir? ")

# Kullanıcıdan bölüm sayısını tam sayıya (int) çevirerek alıyoruz
bolum_sayisi = int(input("Oyundaki toplam bölüm/sahne sayısı kaç? "))

# Bölüm başına ortalama geliştirme süresini ondalıklı sayıya (float) çevirerek alıyoruz
bolum_suresi = float(input("Bölüm başına ortalama geliştirme süresi (saat) nedir? "))

# Geliştirici saatlik ücretini ondalıklı sayıya (float) çevirerek alıyoruz
saatlik_ucret = float(input("Geliştirici saatlik ücreti (TL) nedir? "))

# Uç durum kontrolü: Negatif değer veya sıfır girilirse kullanıcıyı uyarıyoruz
if bolum_sayisi <= 0 or bolum_suresi <= 0 or saatlik_ucret < 0:
    print("\nUyarı: Bölüm sayısı ve süre 0'dan büyük, saatlik ücret ise 0 veya daha büyük olmalıdır!")
else:
    # Aritmetik operatör (*) ile toplam geliştirme süresini (saat) hesaplıyoruz
    toplam_sure = bolum_sayisi * bolum_suresi

    # Aritmetik operatör (*) ile toplam proje maliyetini (TL) hesaplıyoruz
    toplam_maliyet = toplam_sure * saatlik_ucret

    # Karşılaştırma operatörü (>) ile 50.000 TL bütçe sınırının aşılıp aşılmadığını (bool) kontrol ediyoruz
    butce_asildi_mi = toplam_maliyet > 50000

    # f-string kullanarak hesaplama sonuçlarını düzenli ve okunaklı biçimde yazdırıyoruz
    print("\n--- Oyun Projesi Maliyet Raporu ---")
    print(f"Proje Adı        : {oyun_adi}")
    print(f"Toplam Süre      : {toplam_sure:.1f} saat")
    print(f"Toplam Maliyet   : {toplam_maliyet:.2f} TL")
    print(f"Bütçe Aşıldı mı? : {butce_asildi_mi}")

    # Koşul yapısıyla bütçe durumuna göre ek bilgilendirme veriyoruz
    if butce_asildi_mi:
        print("Durum: Proje maliyeti 50.000 TL başlangıç bütçesini aşıyor, kapsam daraltılmalı.")
    else:
        print("Durum: Proje maliyeti belirlenen 50.000 TL bütçe sınırına uygun.")

# Pencerenin hemen kapanmaması için giriş bekliyoruz
input("\nÇıkmak için Enter tuşuna basın...")