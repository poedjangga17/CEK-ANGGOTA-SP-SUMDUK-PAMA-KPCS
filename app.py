
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cek Anggota SP & Sumduk", page_icon="✅", layout="centered")

st.title("📋 Aplikasi Cek Anggota SP & Sumduk")

# Upload file Excel
uploaded_file = st.file_uploader("📂 Upload file Excel (format .xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name="DB_MASTER")
        st.success("✅ File berhasil dimuat!")
        
        # Pastikan kolom sesuai
        required_columns = ["NRP", "Nama", "SP", "Sumduk"]
        if not all(col in df.columns for col in required_columns):
            st.error("❌ Kolom tidak lengkap. Harus ada: NRP, Nama, SP, Sumduk")
            st.stop()

        # Input NRP
        nrp_input = st.text_input("🔍 Masukkan NRP:")

        if nrp_input:
            result = df[df["NRP"].astype(str) == nrp_input]

            if not result.empty:
                nama = result.iloc[0]["Nama"]
                sp_status = str(result.iloc[0]["SP"]).strip().lower()
                sumduk_status = str(result.iloc[0]["Sumduk"]).strip().lower()

                st.write(f"### ✅ Hasil Pencarian untuk NRP **{nrp_input}**")
                st.write(f"**Nama:** {nama}")

                # Status SP
                if sp_status in ["ya", "yes", "anggota"]:
                    st.success("✔ Anggota SP")
                else:
                    st.error("✘ Bukan Anggota SP")

                # Status Sumduk
                if sumduk_status in ["ya", "yes", "anggota"]:
                    st.success("✔ Anggota Sumduk")
                else:
                    st.error("✘ Bukan Anggota Sumduk")

            else:
                st.warning("⚠ NRP tidak ditemukan di database.")
    except Exception as e:
        st.error(f"❌ Gagal memuat data: {e}")
else:
    st.info("📌 Silakan upload file Excel terlebih dahulu.")
