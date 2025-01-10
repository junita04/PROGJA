import streamlit as st

# Menambahkan session state untuk navigasi halaman
st.session_state.pindah = True

# Definisi halaman utama
Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="Halaman Utama UMKM Way Muli",
    default=True)

# Mengatur halaman yang terkait
UMKM1 = st.Page(
    "UMKM/UMKM1.py",
    title="UMKM Way Muli",
)

# Definisi navigasi halaman
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "UMKM": [UMKM1]
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 

pg.run()
