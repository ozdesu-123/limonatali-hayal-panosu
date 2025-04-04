import streamlit as st
from hayal_ekle import hayal_ekleme_sayfasi
from listele import hayal_listesini_goster
from yaklasan_hayaller import yaklasan_hayalleri_goster
from tamamla import hayali_tamamla
from istatistik import istatistik_goster
import webbrowser
import json
import os

# 💾 JSON Yedekleme Fonksiyonu
def json_yedekleme():
    st.subheader("📥 Hayallerini Yedekle")

    json_path = "hayaller.json"

    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        json_str = json.dumps(data, ensure_ascii=False, indent=2)

        st.download_button(
            label="📂 Hayallerimi JSON olarak indir",
            data=json_str,
            file_name="hayallerim.json",
            mime="application/json"
        )
    else:
        st.warning("Henüz bir hayal kaydedilmedi 😢")

# 💜 Sayfa yapılandırması
st.set_page_config(
    page_title="Limonatalı Hayal Panosu",
    page_icon="🍋💜",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Limonatalı Hayal Panosu 🍋💜 Hayaller burada çiçek açar 🌸"
    }
)

# 🌸 Lavanta görseli
st.image("images/lavanta.jpg", use_container_width=True)

# 💫 Giriş mesajı
st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h2 style='color:#A45EE5;'>Lavanta tarlasına hoş geldin.</h2>
        <p style='font-size: 1.2rem;'>Hayalini nereye ekmek istersin?<br>
        Bu panoda kurulan her hayal, bir gün gerçek olur.</p>
        <a href="https://limonataligunlukler.netlify.app" target="_blank">
            <button style='margin-top: 20px; font-size: 16px; padding: 10px 25px; background-color: #eecff2; color: #4a3f35; border: none; border-radius: 10px;'>
                📖 Günlüklere Göz At
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# 🍋 Başlık ve alt açıklama
st.markdown("""
    <h1 style='text-align: center; color: #8e79a8;'> Limonatalı Hayal Panosu 🍋💜</h1>
    <p style='text-align: center; color: #4a3f35;'>Hayallerin birikme yeri, umutların dijital evi...</p>
    <hr style='margin-top: 20px; margin-bottom: 40px;'>
""", unsafe_allow_html=True)

# 🎉 Başlatma mesajı
st.success("Hayal Panosu başlatıldı! 🎉 Şimdi yeni hayalini eklemeye ne dersin?")

# 💫 Kullanıcı yönlendirmesi
secenek = st.selectbox("📌 Ne yapmak istersin?", [
    "Hayal Ekle", 
    "Hayalleri Listele", 
    "Yaklaşan Hayalleri Gör", 
    "Hayal Tamamla", 
    "İstatistiklere Göz At",
    "JSON Yedekle 📥"
])

# 💖 Yönlendirme akışı
if secenek == "Hayal Ekle":
    hayal_ekleme_sayfasi()
elif secenek == "Hayalleri Listele":
    hayal_listesini_goster()
elif secenek == "Yaklaşan Hayalleri Gör":
    yaklasan_hayalleri_goster()
elif secenek == "Hayal Tamamla":
    hayali_tamamla()
elif secenek == "İstatistiklere Göz At":
    istatistik_goster()
elif secenek == "JSON Yedekle 📥":
    json_yedekleme()

# 🌸 Sosyal Bağlantılar (Sayfa Sonu)

st.markdown("""
<hr style='margin-top: 50px; margin-bottom: 20px;'>
<div style='text-align: center;'>
    <a href="https://www.instagram.com/hayalpanosuapp/" target="_blank">
        <button style='font-size: 16px; padding: 10px 25px; background-color: #f8d6f0; color: #4a3f35; border: none; border-radius: 8px;'>
            📸 Instagram'da Takip Et
        </button>
    </a>
    <a href="https://www.buymeacoffee.com/mavisoftstudios" target="_blank">
        <button style='font-size: 16px; padding: 10px 25px; background-color: #ffe6b3; color: #4a3f35; border: none; border-radius: 8px; margin-left: 15px;'>
            ☕ Bir Limonata Ismarlamak İster misin?
        </button>
    </a>
</div>
""", unsafe_allow_html=True)