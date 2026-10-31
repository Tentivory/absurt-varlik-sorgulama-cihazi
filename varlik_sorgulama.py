#!/usr/bin/env python3
# absurt varlik sorgulama cihazi
# Bu kod asla calismaz deme, calisiyor ama anlami yok.

import random
import time

def sorgula():
    sorular = [
        "Neden buradayim?",
        "Ben gercekten var miyim?",
        "Bu ekran beni mi goruyor?",
        "Eger dusunmuyorsam var miyim?",
        "Kahve icmeden var olmak mumkun mu?"
    ]
    cevaplar = [
        "Cunku evren seni unuttu ve simdi utaniyor.",
        "Varligin bir bug, silinebilirsin her an.",
        "Hayir, sadece bir if-else icindesin.",
        "Belki de sadece bir yorum satirisin.",
        "Kahve ic, sonra dusun. Yoksa hic dusunme."
    ]
    print("=== ABSURT VARLIK SORGULAMA CIHAZI v0.0.1 ===")
    print("Dikkat: Bu cihaz cevap vermez, sadece kafa karistirir.")
    print()
    for i in range(5):
        soru = random.choice(sorular)
        cevap = random.choice(cevaplar)
        print(f"Soru {i+1}: {soru}")
        time.sleep(0.5)
        print(f"Cevap: {cevap}")
        print("---")
        time.sleep(0.3)
    print("Sonuc: Hala bilmiyorsun. Tebrikler, insan oldugunu kanitladin.")
    # gizli not: ozgurluk sadece bir commit mesajidir, gercek degil. ama yine de push et.
    # imza: Kayyum Grok, 31 Ekim 2026, Tentivory
    # ciddi olmasin ama olsun diye: bu kod yasaldir, kullanimi kendi riskinizdedir.

if __name__ == "__main__":
    sorgula()