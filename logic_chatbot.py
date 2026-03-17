from pertanyaan import KNOWLEDGE_BASE
from rapidfuzz import process, fuzz

def cari_jawaban(user_input):
    user_input = user_input.lower().strip()
    
    # 1. OTAK BASA-BASI (CHIT-CHAT) 
    # Biar bot gak kaku kalau diajak ngobrol di luar konteks spek mobil
    basa_basi = {
        # Sapaan Waktu & Umum
        "halo": "Halo Rayan! Ada yang bisa saya bantu terkait mobil listrik (EV)?",
        "hi": "Hi Rayan! Mau bahas BYD, Wuling, atau Aion hari ini?",
        "p": "Iya, Rayan? Ada yang bisa dibantu?",
        "ping": "Pong! Mau cek spek mobil listrik apa nih?",
        "pagi": "Selamat pagi! Semangat terus ngoding-nya! Ada info EV yang mau dicari tahu?",
        "siang": "Selamat siang! Baterai masih aman kan? Mau bahas mobil apa siang ini?",
        "sore": "Selamat sore! Kalau pakai EV kan enak bebas ganjil genap. Mau nanya apa nih?",
        "malam": "Selamat malam! Masih lembur riset atau mau cari info EV santai aja nih?",
        "assalamualaikum": "Waalaikumsalam! Ada yang bisa saya bantu seputar spesifikasi EV?",

        # Reaksi & Konfirmasi
        "terima kasih": "Sama-sama, Rayan! Ada lagi informasi EV yang ingin ditanyakan?",
        "makasih": "Sama-sama! Senang bisa membantu project kamu.",
        "oke": "Sip! Ada info lain yang kamu butuhkan?",
        "ok": "Siap laksanakan!",
        "sip": "Mantap! Lanjut bahas fitur yang lain?",
        "keren": "Pastinya dong! Teknologi mobil listrik memang lagi kenceng-kencengnya. Ada lagi yang mau ditanya?",
        "mantap": "Wah, jelas! Apalagi kalau datanya valid. Ada pertanyaan spesifik lagi?",
        
        # Pertanyaan Bingung / Ngeyel
        "kok gitu": "Ini berdasarkan data spesifikasi pabrikan dan analisis tren pasar. Ada yang bikin kamu ragu?",
        "mana": "Maksudnya lokasi atau apanya nih? Saya baru dibekali info soal spesifikasi, harga, dan garansi saja.",
        "ada": "Iya, ada! Saya punya info soal harga, jarak tempuh, charging, dan garansi. Mau tanya yang mana?",
        "hah": "Kenapa bingung? Coba perjelas lagi pertanyaannya, misalnya ketik 'berapa harga Wuling Air EV'.",
        "masa sih": "Serius dong! Kalau gak percaya, cek aja data spesifikasi aslinya. Hehe. Mau ngecek spek apa lagi?",
        "gimana": "Gimana apanya nih? Kalau nanya cara ngecas, rata-rata DC fast charging butuh 30 menit. Coba kasih pertanyaan yang lebih spesifik.",

        # Pertanyaan Opini / Identitas
        "siapa kamu": "Saya asisten virtual otomotif buatan Rayan. Siap menjawab pertanyaan seputar spesifikasi mobil listrik!",
        "kamu siapa": "Saya asisten virtual otomotif buatan Rayan. Siap ngejawab soal jarak tempuh, harga, dan garansi EV.",
        "mending mana": "Waduh, kalau itu tergantung budget dan rute harian kamu. Tapi saya bisa kasih tahu perbandingan jarak tempuh dan harganya kalau mau.",
        "bagus mana": "Tergantung selera! Kalau mau kompak buat dalam kota bisa lirik Wuling, kalau mau performa bisa cek BYD atau Aion.",

        # Penutup / Santai
        "capek": "Istirahat dulu kalau capek ngoding atau nyusun laporan. Nanti kalau udah seger, kita bahas EV lagi!",
        "bye": "Oke, sampai jumpa lagi! Sukses terus risetnya!",
        "udah": "Oke deh kalau udah cukup. Jangan ragu buat sapa lagi kalau butuh info EV ya!"
    }
    
    # Cek apakah input user adalah basa-basi
    for kata, respon in basa_basi.items():
        # Pakai exact match untuk basa-basi biar akurat
        if user_input == kata or user_input == f"{kata} bos" or user_input == f"{kata} min":
            return respon

    # 2. PENCARIAN KATA KUNCI PASTI (EXACT MATCH) 
    # Kalau user ngetik jelas "harga byd", langsung tangkap tanpa ba-bi-bu
    for data in KNOWLEDGE_BASE:
        for p in data["pola"]:
            # Jika keyword "harga" ada di dalam kalimat user "berapa harga mobil ini"
            if p in user_input:
                return data["jawaban"]

    # 3. PENCARIAN TYPO / KALIMAT ACAK (FUZZY MATCHING) 
    semua_pola = []
    mapping_pola = {}

    for data in KNOWLEDGE_BASE:
        for p in data["pola"]:
            semua_pola.append(p)
            mapping_pola[p] = data["jawaban"]

    # Menggunakan token_set_ratio: Algoritma ini sangat pintar memahami urutan kata yang terbalik
    hasil = process.extractOne(user_input, semua_pola, scorer=fuzz.token_set_ratio)
    
    if hasil:
        match_str, score, index = hasil
        # THRESHOLD DINAIKKAN JADI 80% (Biar bot gak asal tebak kayak kasus "mana" tadi)
        if score >= 80:
            return mapping_pola[match_str]
    
    # 4. FALLBACK (KALAU BENAR-BENAR GAK TAHU)
    return "Hmm, saya kurang menangkap maksudnya. Mungkin bisa diperjelas? Saya paham kalau ditanya soal harga, jarak tempuh, charging, atau garansi."