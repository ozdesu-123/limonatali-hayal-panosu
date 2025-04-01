import json
import streamlit as st

def hayali_tamamla():
    try:
        with open("hayaller.json", "r", encoding="utf-8") as f:
            hayaller = json.load(f)
    except FileNotFoundError:
        st.warning("Henüz kayıtlı bir hayal yok.")
        return

    st.subheader("📌 Hayalini Tamamla")
    for i, hayal in enumerate(hayaller):
        if not hayal.get("tamamlandi", False):
            st.markdown(f"**🎯 {hayal['hayal']}** — ⏳ Hedef: {hayal['hedef_tarih']}")
            if st.button(f"✅ Tamamlandı olarak işaretle", key=f"btn_{i}"):
                hayal["tamamlandi"] = True
                with open("hayaller.json", "w", encoding="utf-8") as f:
                    json.dump(hayaller, f, ensure_ascii=False, indent=2)
                st.success("Hayal başarıyla tamamlandı olarak işaretlendi! 🎉")
                st.balloons()
                st.rerun()