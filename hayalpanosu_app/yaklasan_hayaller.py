# yaklasan_hayaller.py

import json
from datetime import date, timedelta
import streamlit as st

def yaklasan_hayalleri_goster():
    try:
        with open("hayaller.json", "r", encoding="utf-8") as f:
            hayaller = json.load(f)
    except FileNotFoundError:
        hayaller = []

    bugun = date.today()
    yedi_gun_sonra = bugun + timedelta(days=7)

    yaklasanlar = [
        h for h in hayaller
        if "hedef_tarih" in h and bugun <= date.fromisoformat(h["hedef_tarih"]) <= yedi_gun_sonra
    ]

    if yaklasanlar:
        st.subheader("📅 Hedef Tarihi Yaklaşan Hayaller")
        for h in yaklasanlar:
            kalan = (date.fromisoformat(h["hedef_tarih"]) - bugun).days
            st.info(f"💭 {h['hayal']} \n\n ⏳ {kalan} gün kaldı!", icon="⏰")
    else:
        st.success("Şu anda hedef tarihi yaklaşan bir hayal yok, ama limonatayı taze tutmaya devam! 🍋")