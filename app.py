import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Niko Asistan Vet", page_icon="🐾")

# --- ÖZEL STİL (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; background-color: #1976d2; color: white; height: 3em; border-radius: 10px; font-weight: bold; }
    .recete-kutusu { border: 2px solid #1976d2; padding: 20px; border-radius: 15px; background-color: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- VERİTABANI ---
VERI = {
    'Kedi': {
        'ilac': 'Meloksikam (Ağrı Kesici)',
        'doz_oran': 0.1, 
        'form': '💉 Enjeksiyon (Deri Altı)', 
        'periyot': 'Günde 1 Kez',
        'ates_ref': (38.0, 39.2)
    },
    'Köpek': {
        'ilac': 'Karprofen (Antienflamatuar)',
        'doz_oran': 4.0, 
        'form': '💊 Tablet (Ağızdan)', 
        'periyot': '12 Saatte Bir',
        'ates_ref': (37.5, 39.2)
    },
    'Tavşan': {
        'ilac': 'Enrofloksasin (Antibiyotik)',
        'doz_oran': 5.0, 
        'form': '💧 Oral Süspansiyon', 
        'periyot': 'Günde 2 Kez',
        'ates_ref': (38.5, 40.0)
    }
}

# --- ARAYÜZ (YENİ İSİM) ---
st.markdown("<h1 style='text-align: center; color: #1976d2;'>🐾 YARDIMCI NİKO ASİSTAN VET</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Akıllı Klinik Karar Destek Sistemi</p>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns(2)
with col1:
    isim = st.text_input("Hasta Adı", "Pamuk")
    tur = st.selectbox("Tür", list(VERI.keys()))
with col2:
    kilo = st.number_input("Kilo (kg)", min_value=0.1, value=5.0, step=0.1)
    ates = st.number_input("Ateş (°C)", value=38.5, step=0.1)

if st.button("ANALİZİ BAŞLAT"):
    secilen = VERI[tur]
    toplam_doz = round(kilo * secilen['doz_oran'], 2)
    
    # Ateş Kontrolü
    durum = "STABİL" if secilen['ates_ref'][0] <= ates <= secilen['ates_ref'][1] else "KRİTİK"
    renk = "#2e7d32" if durum == "STABİL" else "#d32f2f"

    # --- REÇETE EKRANI ---
    st.markdown(f"""
    <div class="recete-kutusu">
        <h2 style="color: {renk}; text-align: center; margin-top:0;">{tur.upper()}: {isim.upper()} - {durum}</h2>
        <hr>
        <table style="width:100%; font-size: 18px;">
            <tr><td><b>🤖 Asistan Notu:</b></td><td>{secilen['ilac']} önerilir.</td></tr>
            <tr><td><b>⚖️ Hesaplanan Doz:</b></td><td><span style="color:red; font-weight:bold;">{toplam_doz} mg</span></td></tr>
            <tr><td><b>💉 Uygulama Şekli:</b></td><td>{secilen['form']}</td></tr>
            <tr><td><b>⏰ Kullanım Sıklığı:</b></td><td>{secilen['periyot']}</td></tr>
        </table>
        <br>
        <div style="background-color: #e3f2fd; padding: 10px; border-radius: 8px; border-left: 5px solid #1976d2;">
            <b>📱 Niko Paylaşım Notu:</b><br>
            *NİKO ASİSTAN* - {isim} ({tur}): Ateş {ates}°C. {secilen['ilac']} ({toplam_doz}mg, {secilen['form']}) uygun görüldü.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.caption("Nazilli Teknik Destek: Niko Asistan Vet v6.0")
