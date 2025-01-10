import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>UMKM DESA WAY MULI</h1>", unsafe_allow_html=True)

def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "UMKM 1 Way Muli",
            "UMKM 2 Way Muli"
        ],
        icons=[
            "shop",  # Icon valid untuk UMKM
            "shop"
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#e3f2fd"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((200, 200))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama Produk: {data_list[i]['Nama Produk']}")
            st.write(f"Deskripsi: {data_list[i]['Deskripsi']}")
            st.write(f"Kontak: {data_list[i]['Kontak']}")
            
            # Tambahkan tautan lokasi ke Google Maps
            if data_list[i]["Lokasi"]:
                st.markdown(f"[Siap untuk berkunjung? Temukan kami di Google Maps sekarang juga!]({data_list[i]['Lokasi']})", unsafe_allow_html=True)
            else:
                st.write("Lokasi: Tidak tersedia")

            st.write("  ")
    st.write("Semua gambar telah dimuat!")

menu = streamlit_menu()

if menu == "UMKM 1 Way Muli":
    def umkm_1_way_muli():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YXgrZDUg9OfifbqtV8EuXfmf62AREPLm",
        ]
        data_list = [
            {
                "Nama Produk": "Bakso Ikan Dua Saudara",
                "Deskripsi": "Bakso Ikan merupakan salah satu UMKM yang terkenal di Desa Way Muli dengan pengolahan yang dilakukan langsung dari rumah penduduk.",
                "Kontak": "08123456789",
                "Lokasi": "https://maps.app.goo.gl/5ag9QpoMi2vuXQkT7"  # Ganti dengan tautan Google Maps lokasi yang sesuai
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    umkm_1_way_muli()
