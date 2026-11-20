import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

KURS_GBP_IDR = 19000


def format_angka(angka, desimal=2):
    # format gaya US dulu (1,234.56), lalu tukar pemisahnya jadi gaya Indonesia (1.234,56)
    teks = f"{angka:,.{desimal}f}"
    return teks.replace(",", "X").replace(".", ",").replace("X", ".")


st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil', min_value=1990, max_value=2030, value=2017, step=1)
mileage = st.number_input('Input Km Mobil', min_value=0, value=20000, step=1000)
tax = st.number_input('Input Pajak Mobil', min_value=0.0, value=150.0)
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0.0, value=40.0)
engineSize = st.number_input('Input Engine Size', min_value=0.0, value=1.5)

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    harga_pound = float(predict[0])
    harga_idr = harga_pound * KURS_GBP_IDR

    st.write('Estimasi harga mobil bekas dalam pounds :')
    st.success(f"£ {format_angka(harga_pound)}")

    st.write('Estimasi harga mobil bekas dalam IDR :')
    st.success(f"Rp {format_angka(harga_idr, desimal=0)}")
