teklifler= {}
ihale_bitti= False

def yuksek_teklif_bul(teklif_kaydi):
    en_yuksek_teklif= 0
    kazanan= ""
    
    for teklifçi in teklif_kaydi:
        teklif_miktari=teklif_kaydi[teklifçi] #döngü içindeki her bir teklif için teklif miktarı belirlenir
        if teklif_miktari > en_yuksek_teklif:
            en_yuksek_teklif=teklif_miktari
            kazanan=teklifçi
    print(f"  {en_yuksek_teklif} TL en yüksek teklifle kazanan {kazanan} ")
    
#bu satır bir döngü başlatır ihale bitti adında bir değişken kullanır
#bu değişken döngüden çıkılması gerektiğini belirtir
#döngü değişkeni true olana kadar devam eder
while not ihale_bitti:
    isim=input("adınız nedir?:")
    fiyat=int(input("teklifiniz nedir?:"))
    teklifler[isim]=fiyat
#kullanıcılardan teklif veren kişinin adını isim ve teklif miktarını fiyat alır
#bu bilgiler bir sözlük olan teklifler in içine kaydedilir
#her girişte teklif veren kişinin adı anahtar olarak kullanılır ve
#teklif miktarı değer olarak saklanır
    devam_mi=input("başka teklif veren var mı?: evet ya da hayır")
#bu satır kullanıcıya devam edip etmeyeceklerini sorar
    if devam_mi=="hayır":
        ihale_bitti=True
        yuksek_teklif_bul(teklifler)
    elif devam_mi=="yes":
        clear()

        
#100daysofcode/udemy
