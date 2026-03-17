import streamlit as st
from logic_chatbot import cari_jawaban 

# Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Car Chatbot", page_icon="🚗")

def main():
    st.title("🚗 Car Chatbot")
    st.subheader("Tanya Jawab Seputar Mobil")
    st.markdown("---")

    # Inisialisasi Riwayat Chat (Session State)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Menampilkan Riwayat Chat di Layar
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input User (Chatbox di bawah)
    if prompt := st.chat_input("Tanya sesuatu tentang mobil listrik..."):
        # Tampilkan Pesan User
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # PROSES LOGIKA (Memanggil file logic_chatbot.py)
        response = cari_jawaban(prompt)

        # Tampilkan Balasan Assistant
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()