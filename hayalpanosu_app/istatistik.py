# istatistik.py

import json
import streamlit as st
from collections import Counter

def istatistik_goster():
    try:
        with open("hayaller.json", "r", encoding="utf-8") as f:
            hayaller = json.load(f)
    except FileNotFoundError:
        st.warning("Henüz hiç hayal eklenmedi 🙈")
        return

    toplam = len(hayaller)
    tamamlanan = sum(1 for h in hayaller if h.get("tamamlandi"))
    tamamlanmayan = toplam - tamamlanan

    kategoriler = [h.get("kategori", "Diğer") for h in hayaller]
    kategori_sayilari = Counter(kategoriler)

    st.subheader("📊 Hayal İstatistikleri")
    st.write(f"💫 Toplam Hayal Sayısı: **{toplam}**")
    st.write(f"✅ Tamamlanan Hayal Sayısı: **{tamamlanan}**")
    st.write(f"⏳ Devam Eden Hayal Sayısı: **{tamamlanmayan}**")

    st.markdown("### 📂 Kategorilere Göre Dağılım")
    for kategori, sayi in kategori_sayilari.items():
        st.write(f"- **{kategori}**: {sayi} hayal")