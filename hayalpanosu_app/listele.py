import json
import streamlit as st
from datetime import date

def hayal_listesini_goster():
    st.subheader("📚 Kaydedilen Hayaller")

    kategori_emoji = {
        "Seyahat": "✈️",
        "Kariyer": "💼",
        "Kişisel Gelişim": "🌱",
        "Sağlık": "🩺",
        "Ev & Aile": "🏡",
        "Diğer": "💫"
    }

    try:
        with open("hayaller.json", "r", encoding="utf-8") as f:
            hayaller = json.load(f)
    except FileNotFoundError:
        hayaller = []

    # 🔍 Filtreler
    filtre = st.radio("Filtre seç:", ["Tümü", "Tamamlananlar", "Tamamlanmamışlar"])
    if filtre == "Tamamlananlar":
        hayaller = [h for h in hayaller if h.get("tamamlandi") == True]
    elif filtre == "Tamamlanmamışlar":
        hayaller = [h for h in hayaller if h.get("tamamlandi") == False]

    kategoriler = sorted(set(h.get("kategori", "Diğer") for h in hayaller))
    secili_kategori = st.selectbox("Kategoriye göre filtrele:", ["Tümü"] + kategoriler)
    if secili_kategori != "Tümü":
        hayaller = [h for h in hayaller if h.get("kategori") == secili_kategori]

    # 📅 Tarihe göre sıralama
    hayaller = sorted(hayaller, key=lambda x: x.get("hedef_tarih", "9999-12-31"))

    if not hayaller:
        st.info("Şu anda bu kritere uyan bir hayal bulunmuyor.")
        return

    for i, h in enumerate(hayaller):
        st.markdown("---")
        kategori = h.get("kategori", "Diğer")
        emoji = kategori_emoji.get(kategori, "")
        durum = "✅ Tamamlandı" if h.get("tamamlandi") else "🕊️ Devam Ediyor"

        st.markdown(f"""
        **{emoji} {kategori}**
        - 💭 Hayal: {h['hayal']}
        - 🗓️ Hedef Tarih: {h['hedef_tarih']}
        - 📌 Durum: {durum}
        """)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✏️ Düzenle", key=f"edit_{i}"):
                yeni_metin = st.text_input("Yeni hayal metni", value=h['hayal'], key=f"new_text_{i}")
                yeni_tarih = st.date_input("Yeni hedef tarih", value=date.fromisoformat(h['hedef_tarih']), key=f"new_date_{i}")
                if st.button("💾 Kaydet", key=f"save_{i}"):
                    h["hayal"] = yeni_metin
                    h["hedef_tarih"] = str(yeni_tarih)
                    with open("hayaller.json", "w", encoding="utf-8") as f:
                        json.dump(hayaller, f, ensure_ascii=False, indent=2)
                    st.success("Hayal güncellendi! 🔄")
                    st.rerun()
        with col2:
            if st.button("🗑️ Sil", key=f"delete_{i}"):
                hayaller.pop(i)
                with open("hayaller.json", "w", encoding="utf-8") as f:
                    json.dump(hayaller, f, ensure_ascii=False, indent=2)
                st.warning("Hayal silindi 💨")
                st.rerun()