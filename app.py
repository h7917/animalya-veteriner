import streamlit as st

# --- ANİMALYA UYGULAMA AYARLARI ---
st.set_page_config(page_title="Animalya Veteriner", page_icon="🐾")

st.title("🐾 NAZİLLİ ANİMALYA VETERİNER")
st.write("### Akıllı Klinik Karar Destek Sistemi")

# --- VERİ VE HESAPLAMA ---
tur = st.selectbox("Hayvan Türü", ["Kedi", "Köpek", "Tavşan"])
kilo = st.number_input("Kilo (kg)", min_value=0.1, value=5.0)

if st.button("HESAPLA"):
    # Basit bir dozaj mantığı (Örn: kg başına 0.1 mg)
    doz = round(kilo * 0.1, 2)
    st.success(f"Önerilen Dozaj: {doz} mg")
    st.info("Not: Bu bir yapay zeka asistanıdır, son karar hekimindir.")
