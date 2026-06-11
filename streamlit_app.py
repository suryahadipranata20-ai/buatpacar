import streamlit as st

# 1. Konfigurasi Halaman Dasar
# Mengatur judul tab, icon hati, dan lebar halaman menjadi centered
st.set_page_config(
    page_title="Sayang App",
    page_icon="💖",
    layout="centered"
)

# 2. CSS Kustom (Styling)
# Kita menggunakan HTML dan CSS untuk mengatur tampilan background dan posisi elemen
st.markdown("""
<style>
    /* Mengatur Warna Background menjadi Merah Muda Lembut */
    .stApp {
        background: linear-gradient(to bottom, #ffe6e6, #fff0f5);
    }

    /* Container untuk menengahkan konten secara vertical */
    .content-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh; /* Membuatnya di tengah-tengah layar */
        text-align: center;
    }

    /* Styling untuk Gambar Hati di atas */
    .header-heart {
        width: 200px;
        height: auto;
        margin-bottom: 30px;
        animation: beat 1.5s infinite; /* Efek berdetik */
    }

    /* Styling untuk Tulisan Utama */
    .love-text {
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Marker Felt', sans-serif;
        color: #d32f2f; /* Warna Merah Tua */
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px #ffc1c1;
        animation: pulse 2s infinite; /* Efek membesar kecil */
    }
    
    /* Efek Animasi */
    @keyframes beat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# 3. Konten HTML
# Menempatkan gambar hati (dari internet) dan teks di tengah
st.markdown("""
<div class="content-container">
    <!-- Gambar Hati Besar di Bagian Atas -->
    <img src="https://cdn-icons-png.flaticon.com/512/123/123283.png" class="header-heart" alt="Love Heart">
    
    <!-- Tulisan Utama -->
    <div class="love-text">
        I LOVE U SAYANGGG<br>♥️♥️♥️
    </div>
</div>
""", unsafe_allow_html=True)

# 4. (Opsional) Menambahkan subtitle atau nama kecil
st.markdown("<div style='text-align: center; color: #b71c1c; margin-top: 50px;'><h3>Dari: Aku 💕</h3></div>", unsafe_allow_html=True)
