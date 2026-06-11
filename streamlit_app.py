import streamlit as st

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="Sayang App",
    page_icon="💖",
    layout="centered"
)

# 2. CSS Kustom (Styling)
st.markdown("""
<style>
    /* Mengatur Warna Background menjadi Merah Muda Lembut */
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }

    /* Container untuk menengahkan konten secara vertical */
    .content-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        text-align: center;
    }

    /* Styling untuk Tulisan Utama */
    .love-text {
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Marker Felt', sans-serif;
        color: #ff0000;
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 3px 3px 6px #ff9999;
        margin-top: 30px;
        animation: pulse 2s infinite;
    }
    
    /* Efek Animasi Detik Jantung */
    @keyframes heartbeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.15); }
        28% { transform: scale(1); }
        42% { transform: scale(1.15); }
        70% { transform: scale(1); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(scale(1)); }
    }
</style>
""", unsafe_allow_html=True)

# 3. Konten HTML dengan Gambar HatiSVG (Tidak Perlu Link External)
st.markdown("""
<div class="content-container">
    <!-- Gambar Hati Besar (SVG) di Bagian Atas -->
    <svg width="250" height="250" viewBox="0 0 32 29.6" style="animation: heartbeat 1.5s infinite;">
        <path fill="#ff0000" d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
        c6.1-9.3,16-11.8,16-21.2C32,3.8,28.2,0,23.6,0z"/>
    </svg>
    
    <!-- Tulisan Utama -->
    <div class="love-text">
        I LOVE U SAYANGGG<br>♥️♥️♥️
    </div>
</div>
""", unsafe_allow_html=True)

# 4. (Opsional) Menambahkan pesan romantis dari bawah
st.markdown("""
<div style='text-align: center; color: #c62828; margin-top: 60px;'>
    <h4>Selalu di hatiku 💕</h4>
</div>
""", unsafe_allow_html=True)
