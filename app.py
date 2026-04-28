import streamlit as st

# --- SAYFA AYARLARI VE TASARIM ---
st.set_page_config(page_title="Nazilli Animalya AI", page_icon="🐾", layout="centered")

# Burası uygulamayı renklendiren "Sihirli" kısım (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-title { color: #d32f2f; text-align: center; font-size: 40px; font-weight: bold; text-shadow: 2px 2px 4px #ccc; }
    .stButton>button { background-color: #d32f2f; color: white; border-radius: 20px; height: 3em; width: 100%; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #b71c1c; color: white; border: none; }
    .report-card { background: white; padding: 20px; border-radius: 15px; border-left: 10px solid #d32f2f; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- BAŞLIK ---
st.markdown('<p class="main-title">🐾 NAZİLLİ ANİMALYA VETERİNER</p>', unsafe_allow_html=True)
st.write("<p style='text-align: center; color: gray;'>Yapay Zeka Destekli Klinik Karar Sistemi</p>", unsafe_allow_html=True)

# --- VERİTABANI ---
DB = {
    'Kedi': {'ates': (38.0, 39.2), 'doz': 0.1, 'ilac': 'Meloksikam', 'ikon': '🐱'},
    'Köpek': {'ates': (37.5, 39.2), 'doz': 4.0, 'ilac': 'Karprofen', 'ikon': '🐶'},
    'Tavşan': {'ates': (38.5, 40.0), 'doz': 0.03, 'ilac': 'Buprenorfin', 'ikon': '🐰'}
}

# --- SEKMELER ---
tab1, tab2 = st.tabs(["📋 Klinik Muayene", "🔬 Laboratuvar Analizi"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        isim = st.text_input("Hasta Adı", placeholder="Örn: Pamuk")
        tur = st.selectbox("Tür", list(DB.keys()))
    with col2:
        kilo = st.number_input("Kilo (kg)", min_value=0.1, value=5.0)
        ates = st.slider("Ateş (°C)", 34.0, 44.0, 38.5)

    if st.button("ANALİZ RAPORU OLUŞTUR"):
        data = DB[tur]
        doz = round(kilo * data['doz'], 2)
        durum = "STABİL" if data['ates'][0] <= ates <= data['ates'][1] else "KRİTİK"
        renk = "green" if durum == "STABİL" else "red"

        # Zenginleştirilmiş Sonuç Kartı
        st.markdown(f"""
            <div class="report-card">
                <h2 style="color:{renk};">{data['ikon']} {isim.upper()} - {durum}</h2>
                <hr>
                <p><b>🩺 Önerilen İlaç:</b> {data['ilac']}</p>
                <p><b>⚖️ Hesaplanan Dozaj:</b> <span style="font-size: 20px; color: #d32f2f;">{doz} mg</span></p>
                <p><b>🌡️ Ölçülen Isı:</b> {ates} °C</p>
            </div>
        """, unsafe_allow_html=True)
        
        # WhatsApp İçin Hızlı Kopyala
        st.info(f"📲 **WhatsApp Mesajı:** *NAZİLLİ ANİMALYA* - {isim}: Durum {durum}, Doz: {doz}mg.")

with tab2:
    st.write("### 🔬 Laboratuvar Değerlendirmesi")
    wbc = st.number_input("WBC (Beyaz Kan Hücresi)", 0.0, 50.0, 10.0)
    if st.button("Tahlili Yorumla"):
        if wbc > 17.0:
            st.error("⚠️ Yüksek WBC: Enfeksiyon veya yangı belirtisi olabilir.")
        elif wbc < 6.0:
            st.warning("⚠️ Düşük WBC: Bağışıklık sistemi baskılanmış olabilir.")
        else:
            st.success("✅ WBC Değeri Normal sınırlarda.")

st.divider()
st.caption("Nazilli Lise GFB Üyesi tarafından Animalya için geliştirilmiştir. 2026")
