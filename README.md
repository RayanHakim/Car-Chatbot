# 🚗 Car Chatbot System

Sistem chatbot interaktif berbasis Python yang dirancang untuk memberikan informasi seputar spesifikasi, harga, dan layanan kendaraan listrik (EV). Proyek ini mengintegrasikan antarmuka web modern dengan logika pencarian teks yang cerdas.

---

## 🌟 Fitur Utama
* **Interactive Chat Interface:** Antarmuka percakapan yang responsif menggunakan Streamlit.
* **Natural Language Processing (NLP) Lite:** Menggunakan algoritma *Fuzzy Matching* untuk mengenali input pengguna meskipun terdapat kesalahan pengetikan (*typo*).
* **Multi-stage Logic:** * Penanganan percakapan umum (*Chit-chat*).
    * Pencarian kata kunci spesifik (*Exact Match*).
    * Pemrosesan kemiripan kalimat (*Fuzzy Matching*).
* **Session Persistence:** Menyimpan riwayat percakapan selama sesi pengguna aktif.

---

## 🛠️ Arsitektur Teknologi
* **Language:** [Python 3.x](https://www.python.org/)
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Matching Engine:** [RapidFuzz](https://github.com/rapidfuzz/RapidFuzz)
* **Data Storage:** Local Knowledge Base (`pertanyaan.py`)

---

## 📂 Struktur Repositori
| Nama File | Deskripsi |
| :--- | :--- |
| `app.py` | Entry point aplikasi dan konfigurasi UI Streamlit. |
| `logic_chatbot.py` | Mesin pemrosesan logika dan algoritma pencarian. |
| `pertanyaan.py` | Dataset berisi pola pertanyaan dan jawaban. |
| `requirements.txt` | Daftar dependensi library Python yang dibutuhkan. |

---

## 🚀 Panduan Instalasi

1. **Clone Repository:**
   ```bash
   git clone [https://github.com/RayanHakim/Car-Chatbot.git](https://github.com/RayanHakim/Car-Chatbot.git)
   cd Car-Chatbot
