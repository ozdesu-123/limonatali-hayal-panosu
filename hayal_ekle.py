# hayal_ekle.py

import streamlit as st
from datetime import date
import json

def hayal_ekleme_sayfasi():
    st.subheader("🌸 Yeni Bir Hayal Ekle")

    hayal_metni = st.text_area("Hayalini yaz...", key="hayal_metni")
    hedef_tarih = st.date_input("🎯 Hedef Tarih", min_value=date.today(), key="hedef_tarih")

    kategori = st.selectbox(
        "📂 Kategori seç:",
        ["Seyahat", "Kariyer", "Kişisel Gelişim", "Sağlık", "Ev & Aile", "Diğer"]
    )

    if st.button("🌟 Hayalimi Kaydet"):
        if hayal_metni.strip() == "":
            st.warning("Lütfen bir hayal gir 📝")
        else:
            yeni_hayal = {
                "hayal": hayal_metni,
                "hedef_tarih": str(hedef_tarih),
                "tamamlandi": False,
                "ekleme_tarihi": str(date.today()),
                "kategori": kategori
            }

            try:
                with open("hayaller.json", "r", encoding="utf-8") as f:
                    hayaller = json.load(f)
            except FileNotFoundError:
                hayaller = []

            hayaller.append(yeni_hayal)

            with open("hayaller.json", "w", encoding="utf-8") as f:
                json.dump(hayaller, f, ensure_ascii=False, indent=2)

            st.success(f"Hayalin kaydedildi: '{hayal_metni}' → Hedef Tarih: {hedef_tarih}")