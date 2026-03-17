# Dataset Tanya Jawab Mobil
KNOWLEDGE_BASE = [
    {
        "tag": "jarak_tempuh",
        "pola": ["jarak tempuh", "berapa kilo", "sejauh mana", "baterai awet", "kapasitas baterai", "range"],
        "jawaban": "Berdasarkan standar pengetesan (NEDC/WLTP), berikut komparasi jarak tempuh beberapa EV populer:\n\n"
                   "- **BYD Seal:** Tipe Premium bisa mencapai **650 km**, sedangkan tipe Performance (AWD) sekitar **580 km**.\n"
                   "- **Aion Hyptec HT:** Mampu menempuh jarak hingga **600 km** dalam sekali *charge* penuh.\n"
                   "- **Wuling Air EV:** Tipe Standard Range **200 km**, dan tipe Long Range **300 km**.\n\n"
                   "💡 *Catatan: Jarak tempuh *real-world* bisa berbeda tergantung gaya berkendara, kondisi lalu lintas (macet), dan suhu AC.*"
    },
    {
        "tag": "harga",
        "pola": ["harga", "berapa duit", "price list", "biaya beli", "harganya", "pricelist"],
        "jawaban": "Berikut adalah estimasi harga OTR Jakarta untuk lineup mobil listrik tersebut:\n\n"
                   "💰 **Segmen Compact/City Car:**\n"
                   "- **Wuling Air EV:** Rp 190 Juta (Lite) hingga Rp 275 Juta (Long Range).\n\n"
                   "🏎️ **Segmen Premium Sedan & SUV:**\n"
                   "- **BYD Seal:** Rp 629 Juta (Premium) - Rp 719 Juta (Performance).\n"
                   "- **Aion Hyptec HT:** Estimasi di angka Rp 685 Juta (Premium).\n\n"
                   "Harga ini belum termasuk insentif pajak PPN 1% dari pemerintah ya!"
    },
    {
        "tag": "charging",
        "pola": ["ngecas", "berapa lama", "charge", "pengisian", "stasiun", "spklu", "watt", "daya rumah"],
        "jawaban": "Durasi pengisian daya EV terbagi menjadi dua metode utama:\n\n"
                   "⚡ **DC Fast Charging (SPKLU):**\n"
                   "Sangat cepat! Untuk mengisi dari 10% hingga 80%, rata-rata hanya membutuhkan waktu **30 - 45 menit**.\n\n"
                   "🔌 **AC Home Charging (Wallbox/Portable):**\n"
                   "Lebih lambat tapi aman untuk umur baterai. Membutuhkan waktu sekitar **8 hingga 11 jam** (tergantung kapasitas baterai dan daya listrik rumah). Minimal daya listrik rumah yang disarankan adalah **2200W - 3500W** untuk *portable charger*."
    },
    {
        "tag": "garansi",
        "pola": ["garansi", "baterai rusak", "servis", "perawatan", "aftersales", "rusak"],
        "jawaban": "Ini yang paling penting sebelum beli EV! Rata-rata pabrikan memberikan dua jenis garansi:\n\n"
                   "🛡️ **Garansi Umum Kendaraan:** Biasanya 3 sampai 5 tahun.\n"
                   "🔋 **Garansi Baterai (Core EV Parts):** Standar industri adalah **8 tahun atau 160.000 km** (mana yang tercapai lebih dulu).\n\n"
                   "Bahkan, beberapa *brand* seperti Wuling dan BYD sempat memberikan promo **Lifetime Core EV Components Warranty** (Garansi Seumur Hidup) khusus untuk pembeli tangan pertama. Jadi nggak perlu khawatir baterai rusak!"
    }, # <-- PERHATIKAN ADA KOMA DI SINI UNTUK MENYAMBUNGKAN KE DATA BERIKUTNYA
    {
        "tag": "fitur_keselamatan",
        "pola": ["fitur", "keselamatan", "adas", "airbag", "aman gak", "rem otomatis", "safety"],
        "jawaban": "Keamanan adalah prioritas utama di EV modern. Hampir semua EV menengah ke atas sudah dilengkapi **ADAS (Advanced Driver Assistance Systems) Level 2**.\n\n"
                   "🛡️ **Contoh Fitur ADAS:**\n"
                   "- *Adaptive Cruise Control*: Mobil bisa ngerem dan gas sendiri ngikutin mobil depan.\n"
                   "- *Lane Keeping Assist*: Setir otomatis belok kalau mobil keluar jalur.\n"
                   "- *Automatic Emergency Braking*: Ngerem otomatis kalau ada pejalan kaki/kendaraan berhenti mendadak.\n\n"
                   "Sebagai catatan, **BYD Seal** bahkan sudah mendapatkan rating bintang 5 dari Euro NCAP (sangat aman)!"
    },
    {
        "tag": "v2l_powerbank",
        "pola": ["v2l", "powerbank", "listrik rumah", "mati lampu", "vehicle to load", "colokan", "camping"],
        "jawaban": "Salah satu fitur paling revolusioner di mobil listrik adalah **V2L (Vehicle-to-Load)**! 🏕️\n\n"
                   "Fitur ini memungkinkan mobil kamu berubah menjadi *genset berjalan* atau *powerbank raksasa*. Kamu bisa colok alat elektronik rumah tangga (seperti laptop, teko listrik, microwave, atau proyektor) langsung ke mobil.\n\n"
                   "⚡ **Aion Hyptec HT** dan **BYD Seal** sudah mendukung fitur V2L dengan output daya rata-rata hingga **3000 Watt**. Sangat berguna saat *camping* atau mati lampu di rumah! *(Catatan: Wuling Air EV standar belum memiliki fitur ini bawaan pabrik)*."
    },
    {
        "tag": "pajak_tahunan",
        "pola": ["pajak", "pkb", "pajak tahunan", "stnk", "biaya pajak", "insentif", "stnk ev"],
        "jawaban": "Kabar gembira! Pajak tahunan Mobil Listrik (BEV) di Indonesia itu **SUPER MURAH** karena adanya insentif pemerintah. 🇮🇩\n\n"
                   "Sesuai aturan terbaru, tarif PKB (Pajak Kendaraan Bermotor) dan BBNKB untuk mobil listrik murni ditetapkan sebesar **0%**. Artinya, kamu bebas dari bayar pajak kendaraan tahunan yang mahal.\n\n"
                   "🧾 Saat perpanjang STNK tahunan, kamu umumnya cuma perlu bayar **SWDKLLJ (Sumbangan Wajib Dana Kecelakaan Lalu Lintas Jalan)** saja, yang biayanya sekitar **Rp 143.000 per tahun**. Jauh lebih murah dari motor bensin 150cc sekalipun!"
    },
    {
        "tag": "tipe_baterai",
        "pola": ["tipe baterai", "jenis baterai", "lfp", "blade battery", "lithium", "nmc", "terbakar", "meledak"],
        "jawaban": "Saat ini, industri EV (terutama merek Tiongkok) didominasi oleh baterai berjenis **LFP (Lithium Iron Phosphate)**. 🔋\n\n"
                   "Kenapa LFP sangat populer?\n"
                   "- **Lebih Aman:** LFP punya ketahanan suhu panas yang sangat tinggi sehingga sangat minim risiko terbakar (*thermal runaway*).\n"
                   "- **Umur Panjang:** Bisa di-charge hingga 100% setiap hari tanpa bikin baterai cepat rusak (degradasi minim).\n\n"
                   "Sebagai contoh, BYD terkenal dengan teknologi patennya yaitu **Blade Battery** (berbasis LFP) yang diklaim sebagai salah satu baterai EV paling aman di dunia karena lolos uji tusuk paku (*nail penetration test*)."
    },
    {
        "tag": "biaya_operasional",
        "pola": ["biaya", "irit", "lebih murah", "konsumsi listrik", "rupiah per km", "bensin vs listrik", "hemat"],
        "jawaban": "Secara *running cost*, EV jauh mengalahkan mobil ICE (Internal Combustion Engine) alias mobil bensin! 💸\n\n"
                   "⚡ **Hitungan Kasar:**\n"
                   "Tarif listrik rumah (Token/Pascabayar) rata-rata **Rp 1.699 per kWh**. Jika sebuah EV seperti Wuling Air EV butuh sekitar 1 kWh untuk jalan 10 km, maka biayanya cuma **Rp 170 per kilometer**!\n\n"
                   "Bandingkan dengan LCGC bensin (misal 15 km/liter pakai Pertamax Rp 13.000). Biayanya sekitar **Rp 866 per kilometer**. EV bisa 4-5 kali lipat lebih hemat! Belum lagi biaya servis berkalanya yang jauh lebih murah karena tidak perlu ganti oli mesin."
    },
    {
        "tag": "dealer_service",
        "pola": ["bengkel", "dealer", "service center", "lokasi", "kantor", "beli dimana", "showroom"],
        "jawaban": "Untuk layanan purna jual (aftersales), saat ini jaringan dealer terus berkembang pesat:\n\n"
                   "- **Wuling:** Memiliki jaringan terluas dengan lebih dari **150 dealer** di seluruh Indonesia.\n"
                   "- **BYD:** Baru saja meresmikan puluhan dealer di kota-kota besar (Jakarta, Bandung, Medan, Surabaya) bekerja sama dengan Arista Group.\n"
                   "- **Aion:** Sedang membangun jaringan dealer utama di wilayah Jabodetabek dan kota besar lainnya.\n\n"
                   "📍 *Saran: Kamu bisa cek lokasi persisnya via Google Maps dengan mengetik '[Merk Mobil] Dealer Terdekat'.*"
    },
    {
        "tag": "harga_jual_kembali",
        "pola": ["jual lagi", "harga bekas", "resale value", "turun harga", "depresiasi", "investasi"],
        "jawaban": "Ini pertanyaan menarik! 📈\n\n"
                   "Secara umum, *resale value* EV masih dalam tahap penyesuaian pasar. Namun, mobil seperti **Wuling Air EV** punya harga bekas yang cukup stabil karena permintaannya tinggi di pasar mobil bekas kota besar.\n\n"
                   "Faktor yang menjaga harga jual tetap tinggi:\n"
                   "1. **Kondisi Kesehatan Baterai (SOH):** Jika dirawat dengan baik, harga tetap oke.\n"
                   "2. **Garansi Lifetime:** Adanya garansi komponen inti yang panjang bikin pembeli mobil bekas merasa aman."
    },
    {
        "tag": "performa_kecepatan",
        "pola": ["kenceng", "ngebut", "akselerasi", "0-100", "tenaga", "torsi", "hp", "speed"],
        "jawaban": "Kalau kamu cari sensasi *instant torque*, EV adalah pemenangnya! 🏎️\n\n"
                   "- **BYD Seal (Performance):** Raja jalanan! 0-100 km/jam cuma dalam **3.8 detik** (setara *supercar*).\n"
                   "- **Aion Hyptec HT:** Punya tenaga sekitar 340 HP yang bikin tarikan awal sangat responsif.\n"
                   "- **Wuling Air EV:** Meski mungil, tarikan bawahnya sangat gesit untuk *stop-and-go* di kemacetan kota."
    },
    {
        "tag": "ground_clearance_banjir",
        "pola": ["banjir", "hujan", "pendek", "tinggi mobil", "ground clearance", "genangan", "aman lewat air"],
        "jawaban": "Banyak yang khawatir EV konslet kena air, padahal sebenarnya sangat aman! 🌊\n\n"
                   "- **Baterai Kedap Air:** Baterai EV sudah tersertifikasi **IP67 atau IP69**, artinya tahan rendaman air dalam waktu tertentu.\n"
                   "- **Ground Clearance:** \n"
                     "  - **Aion Hyptec HT:** Tinggi (SUV), sangat aman untuk jalanan tidak rata.\n"
                     "  - **BYD Seal:** Cukup rendah (Sedan), jadi harus lebih hati-hati di polisi tidur tinggi atau genangan dalam.\n"
                     "  - **Wuling Air EV:** Aman untuk genangan air setinggi ban, tapi tidak disarankan untuk menerjang banjir parah."
    },
    {
        "tag": "desain_eksterior",
        "pola": ["warna", "desain", "pintu", "keren mana", "tampilan", "lampu", "interior"],
        "jawaban": "Desain EV sekarang unik-unik, Rayan! ✨\n\n"
                   "- **Aion Hyptec HT:** Viral karena pintu belakangnya yang bermodel **Gullwing** (terbuka ke atas) seperti Tesla Model X.\n"
                   "- **BYD Seal:** Mengusung bahasa desain *Ocean Aesthetics* yang sangat aerodinamis dan sporty.\n"
                   "- **Wuling Air EV:** Desain *Future-Tech* yang mungil dan imut, sangat mudah untuk parkir di tempat sempit."
    },
    {
        "tag": "perawatan_rutin",
        "pola": ["perawatan", "servis", "service berkala", "ganti oli", "onderdil", "biaya rawat", "maintenance"],
        "jawaban": "Salah satu keuntungan terbesar EV adalah minim perawatan! 🛠️\n\n"
                   "- **Tanpa Oli Mesin:** Kamu nggak perlu ganti oli, busi, filter udara mesin, atau *fan belt*.\n"
                   "- **Komponen Utama:** Yang perlu diperiksa secara berkala hanyalah: *Cairan pendingin baterai (coolant)*, *minyak rem*, *filter AC*, dan *ban*.\n"
                   "- **Biaya:** Estimasi biaya servis berkala EV bisa **50-70% lebih murah** dibandingkan mobil bensin konvensional karena jumlah komponen bergeraknya jauh lebih sedikit."
    },
    {
        "tag": "regenerative_braking",
        "pola": ["pengereman", "nambah baterai", "isi otomatis", "brake", "regerenative", "one pedal", "rem kaki"],
        "jawaban": "Mobil listrik punya fitur canggih bernama **Regenerative Braking**! 🔋🔄\n\n"
                   "Saat kamu angkat kaki dari pedal gas, motor listrik akan berubah fungsi menjadi generator. Energi kinetik dari putaran roda diubah kembali menjadi listrik dan dimasukkan lagi ke dalam baterai.\n\n"
                   "✨ **Efeknya:**\n"
                   "- Jarak tempuh (range) bisa bertambah sedikit demi sedikit, terutama di kemacetan.\n"
                   "- Kampas rem jadi jauh lebih awet karena mobil melambat dengan bantuan magnet motor listrik."
    },
    {
        "tag": "pemasangan_wallbox",
        "pola": ["pasang charger", "wallbox", "pln", "tambah daya", "listrik rumah", "instalasi", "biaya pasang"],
        "jawaban": "Mau ngecas nyaman di rumah? Kamu butuh **Wallbox Charger**. 🔌🏠\n\n"
                   "- **Daya Listrik:** Disarankan daya rumah minimal **7.700 VA** untuk pemasangan Wallbox 7 kW agar tidak jepret.\n"
                   "- **Program PLN:** Saat ini PLN sering memberikan promo **'Home Charging Services'** berupa diskon tambah daya atau pemasangan meteran khusus untuk pengisian EV di malam hari (jam 22.00 - 05.00) dengan diskon tarif listrik hingga 30%!"
    },
    {
        "tag": "interior_kabin",
        "pola": ["interior", "kursi", "bagasi", "luas gak", "layar", "head unit", "speaker", "Panoramic"],
        "jawaban": "Interior EV modern umumnya terasa sangat luas dan futuristik karena tidak ada terowongan transmisi di lantai. ✨\n\n"
                   "- **BYD Seal:** Layar utamanya bisa berputar (*rotating touchscreen*) dan punya *Panoramic Glass Roof* yang sangat luas.\n"
                   "- **Aion Hyptec HT:** Kabinnya sangat lega dengan kualitas material kulit yang premium.\n"
                   "- **Wuling Air EV:** Meskipun kecil, desain dasbornya minimalis dengan panel instrumen digital yang modern."
    },
    {
        "tag": "ac_efisiensi",
        "pola": ["ac dingin", "boros baterai", "panas", "udara", "suhu", "kompresor"],
        "jawaban": "Di mobil listrik, AC digerakkan langsung oleh listrik dari baterai utama (bukan putaran mesin). ❄️\n\n"
                   "- **Efisiensi:** Menggunakan AC dalam waktu lama saat parkir hanya mengonsumsi sedikit daya (sekitar 1-2 km jarak tempuh per jam).\n"
                   "- **Pre-Conditioning:** Di mobil seperti **BYD** atau **Aion**, kamu bisa menyalakan AC lewat aplikasi HP sebelum kamu masuk ke mobil, jadi pas masuk kabin sudah dingin!"
    },
    {
        "tag": "risiko_kebakaran",
        "pola": ["terbakar", "meledak", "bahaya", "api", "aman gak", "thermal runaway", "short circuit"],
        "jawaban": "Keamanan baterai adalah fokus utama teknologi EV saat ini. 🛡️\n\n"
                   "- **Proteksi Multi-Lapis:** Baterai EV modern dibungkus cangkang baja yang sangat kuat dan memiliki sistem pendingin cair (*liquid cooling*) untuk menjaga suhu.\n"
                   "- **Blade Battery (BYD):** Menggunakan teknologi LFP yang sudah lulus uji tusuk paku (*nail penetration test*). Bahkan jika ditusuk, baterai ini tidak mengeluarkan api atau asap.\n"
                   "- **Sistem BMS:** *Battery Management System* akan otomatis memutus aliran listrik dalam hitungan milidetik jika terdeteksi adanya benturan keras atau hubungan arus pendek (korsleting)."
    },
    {
        "tag": "fitur_aplikasi",
        "pola": ["aplikasi hp", "remote", "kontrol", "nyalain ac", "cek baterai", "smart app", "koneksi"],
        "jawaban": "Hampir semua EV modern (Aion, BYD, Wuling) sudah punya aplikasi khusus di Smartphone! 📱\n\n"
                   "- **Kontrol Jarak Jauh:** Kamu bisa menyalakan AC, mengunci pintu, atau membunyikan klakson lewat HP.\n"
                   "- **Monitoring Real-time:** Kamu bisa cek sisa baterai, estimasi jarak tempuh, dan lokasi parkir mobil secara langsung.\n"
                   "- **Notifikasi:** Jika pengisian daya sudah penuh atau ada pintu yang belum rapat, HP kamu akan memberikan peringatan otomatis."
    },
    {
        "tag": "suspensi_kenyamanan",
        "pola": ["empuk", "keras", "suspensi", "shockbreaker", "nyaman", "polisi tidur", "limbung", "handling"],
        "jawaban": "Karakter suspensi EV biasanya berbeda karena bobot baterai yang berat di bagian bawah (Center of Gravity rendah): 🚗\n\n"
                   "- **BYD Seal:** Punya suspensi yang agak kaku (*sporty*) untuk stabilitas tinggi saat menikung, tapi tetap nyaman meredam guncangan kecil.\n"
                   "- **Aion Hyptec HT:** Menggunakan *Double Wishbone* di depan dan *Five-link Independent* di belakang, memberikan kenyamanan maksimal layaknya SUV Eropa.\n"
                   "- **Wuling Air EV:** Karena ban kecil, suspensinya terasa lebih *stiff* (keras) jika melewati lubang besar, tapi sangat stabil untuk bermanuver di gang sempit."
    },
    {
        "tag": "kursi_ergonomi",
        "pola": ["jok", "kursi", "lega", "duduk", "baris kedua", "penumpang", "pijat", "ventilasi"],
        "jawaban": "Kenyamanan kabin EV seringkali melebihi mobil bensin di kelas harga yang sama:\n\n"
                   "- **Aion Hyptec HT:** Kursi belakang bisa direbahkan hingga **143 derajat** (seperti *first class* di pesawat).\n"
                   "- **BYD Seal:** Jok depan model *Bucket Seat* yang memeluk badan dengan fitur ventilasi (kursi dingin) agar punggung tidak berkeringat.\n"
                   "- **Wuling Air EV:** Meski terlihat kecil dari luar, ruang kaki (*legroom*) baris depan sangat luas karena tidak ada konsol tengah yang menghalangi."
    },
    {
        "tag": "emisi_lingkungan",
        "pola": ["ramah lingkungan", "polusi", "asap", "karbon", "eco friendly", "hijau", "lca"],
        "jawaban": "EV adalah solusi mobilitas hijau karena memiliki **Zero Tailpipe Emission** (Tanpa Knalpot). 🌿\n\n"
                   "- **Kualitas Udara:** Penggunaan EV secara massal sangat efektif mengurangi polusi udara di kota besar seperti Jakarta atau Yogyakarta.\n"
                   "- **Efisiensi Energi:** Secara keseluruhan (dari pembangkit listrik hingga roda berputar), EV jauh lebih efisien dalam mengubah energi menjadi gerak dibandingkan mesin pembakaran internal yang membuang banyak energi dalam bentuk panas."
    },
    {
        "tag": "perbandingan_merek",
        "pola": ["banding", "vs", "lawan", "pilih mana", "kelebihan kekurangan", "perbedaan"],
        "jawaban": "Bingung pilih yang mana? Ini ringkasan karakternya:\n\n"
                   "1. **Wuling Air EV:** Cocok buat kamu yang butuh mobil kedua untuk operasional harian, belanja, atau kuliah yang super irit dan mudah parkir.\n"
                   "2. **BYD Seal:** Cocok buat penyuka kecepatan (*performance*) dan desain mewah futuristik.\n"
                   "3. **Aion Hyptec HT:** Cocok buat keluarga yang mengutamakan kenyamanan maksimal dan ruang kabin yang sangat lega.\n\n"
                   "Semuanya sudah bebas ganjil-genap dan pajaknya sangat murah!"
    },
    {
        "tag": "mobil_bensin",
        "pola": ["bensin", "ice", "pertamax", "pertalite", "mesin biasa", "konvensional", "avanza", "xpander"],
        "jawaban": "Mobil bensin (ICE - Internal Combustion Engine) masih menjadi pilihan populer di Indonesia. ⛽\n\n"
                   "- **Kelebihan:** Infrastruktur SPBU sangat luas hingga ke pelosok, harga beli unit biasanya lebih murah dari EV/Hybrid, dan pilihan model sangat banyak.\n"
                   "- **Kekurangan:** Terkena aturan ganjil-genap, pajak tahunan lebih mahal dari EV, dan biaya operasional (BBM) mengikuti fluktuasi harga minyak dunia.\n"
                   "- **Contoh Populer:** Toyota Avanza, Mitsubishi Xpander, Honda Brio."
    },
    {
        "tag": "mobil_diesel",
        "pola": ["diesel", "solar", "dex", "fortuner", "pajero", "torsi", "irit solar", "mesin diesel"],
        "jawaban": "Mesin Diesel dikenal sebagai 'Raja Torsi' dan sangat tangguh untuk perjalanan jauh. 🚜\n\n"
                   "- **Karakteristik:** Memiliki torsi besar di putaran bawah, sangat kuat menanjak dan membawa beban berat.\n"
                   "- **Bahan Bakar:** Sangat disarankan menggunakan *High Quality Diesel* (seperti Pertamina Dex) untuk menjaga performa mesin modern (Common Rail).\n"
                   "- **Kelebihan:** Konsumsi bahan bakar biasanya lebih irit dibanding mesin bensin untuk ukuran bodi yang sama.\n"
                   "- **Contoh Populer:** Toyota Fortuner, Mitsubishi Pajero Sport, Toyota Innova Reborn Diesel."
    },
    {
        "tag": "mobil_hybrid",
        "pola": ["hybrid", "hev", "phev", "dua mesin", "irit banget", "innova zenix", "yaris cross"],
        "jawaban": "Mobil Hybrid adalah jembatan antara mobil bensin dan listrik. 🔌+⛽\n\n"
                   "Mobil ini memiliki **dua mesin**: Mesin Bensin dan Motor Listrik yang bekerja bergantian atau bersamaan.\n"
                   "- **HEV (Hybrid Electric Vehicle):** Tidak perlu dicolok listrik (ngecas otomatis saat jalan). Contoh: Kijang Innova Zenix Hybrid.\n"
                   "- **Kelebihan:** Sangat irit bensin (terutama di kemacetan kota) dan emisi lebih rendah, tapi tetap tenang karena bisa isi bensin di mana saja.\n"
                   "- **Catatan:** Di Indonesia, mobil Hybrid belum dapat insentif pajak sebanyak EV (masih bayar pajak tahunan normal)."
    },
    {
        "tag": "perbandingan_mesin",
        "pola": ["pilih mana", "bagus mana", "listrik vs bensin", "hybrid vs listrik", "bedanya bensin diesel"],
        "jawaban": "Bingung pilih jenis mesin? Ini panduan cepatnya:\n\n"
                   "1. **Pilih Listrik (EV):** Jika kamu ingin bebas ganjil-genap, pajak murah, dan punya akses ngecas di rumah.\n"
                   "2. **Pilih Hybrid:** Jika ingin sangat irit bensin tapi sering perjalanan luar kota yang minim SPKLU.\n"
                   "3. **Pilih Bensin:** Jika budget beli mobil terbatas dan ingin kemudahan servis di mana saja.\n"
                   "4. **Pilih Diesel:** Jika sering melewati medan tanjakan atau butuh mobil tangguh untuk muatan berat."
    },
    {
        "tag": "emisi_perbandingan",
        "pola": ["polusi bensin", "asap diesel", "emisi hybrid", "lingkungan", "karbon"],
        "jawaban": "Tingkat emisi kendaraan dari yang paling rendah ke tinggi:\n\n"
                   "1. **EV (Listrik):** Nol emisi gas buang (Zero Tailpipe).\n"
                   "2. **Hybrid:** Emisi sangat rendah karena mesin bensin sering mati saat kecepatan rendah.\n"
                   "3. **Bensin:** Emisi standar (tergantung teknologi EURO mesin).\n"
                   "4. **Diesel:** Jika tidak dirawat atau pakai solar murah, bisa menghasilkan emisi partikulat yang lebih tinggi (asap hitam)."
    },
    {
        "tag": "transmisi_matic",
        "pola": ["transmisi", "matic", "cvt", "at", "kopling", "gigi", "dual clutch", "dct"],
        "jawaban": "Transmisi matic modern terbagi jadi dua yang paling populer di Indonesia:\n\n"
                   "- **CVT (Continuously Variable Transmission):** Perpindahan gigi sangat halus, tidak terasa hentakan, dan lebih irit BBM. Cocok buat santai di kota. (Contoh: Honda Brio, Toyota Avanza baru).\n"
                   "- **AT (Conventional Torque Converter):** Terasa lebih bertenaga saat akselerasi dan lebih bandel buat muatan berat atau tanjakan curam. (Contoh: Toyota Innova Reborn, Fortuner).\n"
                   "- **DCT (Dual Clutch):** Perpindahan gigi super cepat seperti mobil balap. (Contoh: Beberapa model KIA atau VW)."
    },
    {
        "tag": "penggerak_roda",
        "pola": ["fwd", "rwd", "awd", "4wd", "penggerak depan", "penggerak belakang", "nanjak", "kuat nanjak"],
        "jawaban": "Sistem penggerak roda sangat menentukan karakter mobil:\n\n"
                   "- **FWD (Front Wheel Drive):** Roda depan yang narik. Kelebihannya kabin lebih luas (gak ada gundukan di lantai) dan lebih irit. (Contoh: Xpander, Stargazer).\n"
                   "- **RWD (Rear Wheel Drive):** Roda belakang yang dorong. Lebih jago nanjak karena beban pindah ke belakang saat nanjak, sehingga ban nggak selip. (Contoh: Avanza lama, Innova).\n"
                   "- **AWD/4WD:** Semua roda gerak. Sangat stabil di jalan licin atau medan berat (Off-road). (Contoh: Subaru, Jeep, BYD Seal Performance)."
    },
    {
        "tag": "mesin_turbo",
        "pola": ["turbo", "turbocharger", "tenaga mesin", "mesin kecil", "irit kenceng", "perawatan turbo"],
        "jawaban": "Banyak mobil bensin jaman sekarang pakai mesin kecil tapi ada **Turbo**-nya! 🌀\n\n"
                   "- **Cara Kerja:** Memanfaatkan gas buang untuk muterin kipas yang nekan udara lebih banyak ke mesin. Hasilnya, mesin 1.000cc Turbo bisa punya tenaga setara mesin 1.500cc biasa.\n"
                   "- **Kelebihan:** Pajak murah (karena CC kecil) tapi tenaga tetap jos.\n"
                   "- **Perawatan:** Wajib pakai oli berkualitas tinggi dan bahan bakar oktan tinggi (Pertamax Turbo/Dex) agar komponen turbo tidak cepat rusak."
    },
    {
        "tag": "pajak_bensin_diesel",
        "pola": ["pajak bensin", "pajak diesel", "pajak mahal", "pkb mobil biasa", "stnk bensin"],
        "jawaban": "Berbeda dengan EV yang pajaknya hampir nol, mobil bensin dan diesel kena pajak normal:\n\n"
                   "- **PKB (Pajak Kendaraan Bermotor):** Dihitung berdasarkan Nilai Jual Kendaraan (NJKB) dan bobot kendaraan. Semakin mahal harga mobilnya, semakin tinggi pajaknya.\n"
                   "- **Progresif:** Kalau kamu punya mobil lebih dari satu atas nama yang sama, pajak mobil kedua dan seterusnya bakal naik drastis (biasanya nambah 0.5% - 1% per mobil).\n"
                   "- **Diesel:** Pajaknya seringkali sedikit lebih mahal dibanding bensin untuk CC yang sama karena faktor bobot kendaraan yang lebih berat."
    },
    {
        "tag": "ketahanan_tanjakan",
        "pola": ["tanjakan curam", "kuat nanjak gak", "letoy", "tanjakan spongebob", "nanjak parah"],
        "jawaban": "Tips buat kamu yang sering lewat daerah pegunungan (seperti arah Kaliurang atau perbukitan):\n\n"
                   "- **Mobil Diesel RWD:** Juara untuk tanjakan karena torsi melimpah dan traksi roda belakang kuat.\n"
                   "- **Mobil Listrik (EV):** Sangat kuat nanjak karena torsi maksimal langsung tersedia dari 0 RPM (tidak perlu nunggu putaran mesin).\n"
                   "- **Mobil Bensin FWD:** Harus lebih pintar jaga momentum. Jika tanjakan sangat curam dan licin, ban depan berisiko selip karena beban kendaraan pindah ke belakang."
    },
    {
        "tag": "biaya_servis_perbandingan",
        "pola": ["biaya servis", "ongkos bengkel", "mahal mana servis", "perawatan mesin", "ganti oli berapa"],
        "jawaban": "Perbandingan biaya servis berkala hingga 100.000 km:\n\n"
                   "- **Mobil Listrik (EV):** Paling murah! Estimasi total biaya servis hanya **Rp 3 - 5 Jutaan** karena cuma ganti filter AC dan cek rem.\n"
                   "- **Mobil Hybrid:** Menengah. Mesin bensinnya tetap butuh ganti oli, tapi komponen rem lebih awet karena *regenerative braking*. Estimasi **Rp 10 - 13 Jutaan**.\n"
                   "- **Mobil Bensin/Diesel:** Paling tinggi. Banyak komponen habis pakai (bus, oli, filter udara, belt). Estimasi **Rp 15 - 20 Jutaan** (tergantung merek)."
    },
    {
        "tag": "depresiasi_harga",
        "pola": ["harga jatuh", "depresiasi", "rugi berapa", "investasi mobil", "nilai jual"],
        "jawaban": "Setiap mobil pasti mengalami penyusutan harga (depresiasi). Rata-rata penurunannya:\n\n"
                   "- **Tahun Pertama:** Biasanya turun **15% - 20%** dari harga baru.\n"
                   "- **Mobil Jepang (Toyota/Honda):** Cenderung lebih stabil karena peminatnya sangat banyak di Indonesia.\n"
                   "- **Mobil Listrik:** Masih bervariasi. Namun, adanya garansi baterai 8 tahun membantu menjaga harga jual kembali agar tidak terjun bebas."
    },
    {
        "tag": "tips_mobil_bekas",
        "pola": ["beli bekas", "second", "cek mobil", "bekas tabrak", "bekas banjir", "inspeksi"],
        "jawaban": "Mau beli mobil bekas? Wajib cek 3 hal 'Haram' ini:\n\n"
                   "1. **Bekas Tabrak Struktur:** Cek tulang sasis depan dan pilar pintu. Kalau ada bekas las-lasan tidak rapi, mending skip.\n"
                   "2. **Bekas Banjir:** Cek bau apek di kabin, karat di kolong jok, atau pasir di sela-sela kabel mesin.\n"
                   "3. **Dokumen:** Pastikan nomor rangka dan mesin cocok dengan STNK/BPKB. \n\n"
                   "💡 *Tips: Gunakan jasa inspektor profesional agar lebih aman!*"
    },
    {
        "tag": "ban_khusus_ev",
        "pola": ["ban ev", "ban khusus", "ban berisik", "torsi ban", "ban mobil listrik", "tekanan ban"],
        "jawaban": "Tahukah kamu? Mobil listrik butuh ban khusus (EV-Rated Tires)! 🛞\n\n"
                   "- **Dinding Ban Kuat:** Harus mampu menahan beban baterai yang sangat berat.\n"
                   "- **Senyap:** Karena mesin EV tidak bersuara, ban harus sangat hening agar tidak terdengar bising di kabin.\n"
                   "- **Low Rolling Resistance:** Didesain agar gesekan dengan aspal minim, sehingga baterai lebih irit."
    },
    {
        "tag": "sunroof_panoramic",
        "pola": ["sunroof", "moonroof", "panoramic roof", "kaca diatas", "atap kaca", "bocor"],
        "jawaban": "Biar nggak ketukar, ini bedanya tipe atap kaca:\n\n"
                   "- **Sunroof:** Kaca kecil yang bisa terbuka (angkat/geser) untuk sirkulasi udara.\n"
                   "- **Panoramic Roof:** Kaca sangat luas dari depan ke belakang, tapi biasanya tidak bisa dibuka (hanya untuk pemandangan). Contoh: **Aion Hyptec HT**.\n"
                   "- **Panoramic Sunroof:** Kombinasi keduanya. Kaca luas dan bagian depan bisa digeser terbuka. Contoh: **BYD Seal**."
    },
    {
        "tag": "oli_mesin",
        "pola": ["jenis oli", "sae", "kental", "encer", "oli mesin bensin", "oli diesel"],
        "jawaban": "Jangan salah isi oli! 🛢️\n\n"
                   "- **Mesin Turbo/Modern:** Biasanya pakai oli encer (0W-20 atau 5W-30) agar pelumasan ke celah mesin sempit tetap lancar.\n"
                   "- **Mesin Diesel:** Butuh oli khusus diesel yang mampu menahan panas tinggi dan membersihkan sisa jelaga karbon (Contoh: SAE 10W-40 atau 5W-40 khusus Diesel)."
    },
    {
        "tag": "brio_umum",
        "pola": ["apa itu brio", "kelebihan brio", "kenapa beli brio", "city car", "honda brio"],
        "jawaban": "Honda Brio adalah *city car* paling populer di Indonesia. 🚗\n\n"
                   "- **Kelebihan Utama:** Konsumsi BBM sangat irit, mesin paling bertenaga di kelasnya (90 PS), dan harga jual kembali (resale value) yang sangat stabil.\n"
                   "- **Varian:** Terbagi menjadi **Brio Satya** (LCGC) untuk efisiensi budget, dan **Brio RS** untuk tampilan lebih sporty dan fitur lebih lengkap."
    },
    {
        "tag": "brio_mesin",
        "pola": ["mesin brio", "cc brio", "tenaga brio", "i-vtec", "berapa silinder", "performa brio"],
        "jawaban": "Dapur pacu Honda Brio menggunakan mesin legendaris:\n\n"
                   "- **Tipe:** 1.2L SOHC 4-Silinder Segaris, 16 Katup **i-VTEC + DBW**.\n"
                   "- **Tenaga:** Maksimal **90 PS** pada 6.000 rpm (Terbesar di kelas 1.200cc).\n"
                   "- **Torsi:** **110 Nm** pada 4.800 rpm.\n\n"
                   "Karena pakai 4 silinder, mesin Brio jauh lebih minim getaran dibandingkan kompetitornya yang pakai 3 silinder (seperti Agya/Ayla lama)."
    },
    {
        "tag": "brio_bbm",
        "pola": ["brio irit", "konsumsi bbm brio", "1 liter berapa km", "bensin brio", "irit gak"],
        "jawaban": "Honda Brio terkenal sebagai 'Raja Irit'. ⛽\n\n"
                   "- **Dalam Kota:** Rata-rata **14 - 16 km/liter** (kondisi macet).\n"
                   "- **Luar Kota/Tol:** Bisa tembus **20 - 22 km/liter** jika dikemudikan secara konstan (Eco Driving).\n"
                   "- **Bahan Bakar:** Disarankan minimal **Pertamax (Oktan 92)** untuk menjaga performa mesin i-VTEC tetap optimal."
    },
    {
        "tag": "brio_transmisi",
        "pola": ["transmisi brio", "brio matic", "cvt brio", "brio manual", "pindah gigi"],
        "jawaban": "Honda Brio menawarkan dua pilihan transmisi:\n\n"
                   "- **CVT (Earth Dreams Technology):** Perpindahan gigi sangat halus tanpa hentakan dan membantu efisiensi BBM.\n"
                   "- **Manual 5-Percepatan:** Cocok buat kamu yang suka kendali penuh dan tarikan yang lebih responsif.\n\n"
                   "CVT Honda dikenal sebagai salah satu yang terbaik karena minim efek *rubber-band* (telat gas)."
    },
    {
        "tag": "brio_vs",
        "pola": ["bedanya satya dan rs", "brio rs vs satya", "pilih satya atau rs", "perbedaan brio"],
        "jawaban": "Ini perbedaan utama **Brio Satya** vs **Brio RS**:\n\n"
                   "1. **Eksterior:** RS punya lampu depan LED, *velg* 15 inch (Satya 14 inch), dan spion lipat otomatis.\n"
                   "2. **Interior:** RS pakai *Head Unit* layar sentuh dan jok dengan jahitan oranye yang lebih sporty.\n"
                   "3. **Suspensi:** RS disetel sedikit lebih kaku untuk stabilitas tinggi, Satya lebih empuk untuk kenyamanan harian."
    },
    {
        "tag": "brio_pajak",
        "pola": ["pajak brio", "pajak tahunan brio", "biaya stnk brio", "pkb brio"],
        "jawaban": "Pajak tahunan Honda Brio termasuk terjangkau:\n\n"
                   "- **Brio Satya:** Sekitar **Rp 2,2 jt - Rp 2,8 jt** per tahun.\n"
                   "- **Brio RS:** Sekitar **Rp 3 jt - Rp 3,5 jt** per tahun.\n\n"
                   "*(Angka ini estimasi PKB untuk wilayah Jakarta/Jawa Tengah ya, tergantung tahun kendaraan)*."
    },
    {
        "tag": "brio_kaki",
        "pola": ["velg brio", "ban brio", "ukuran ban", "ground clearance brio", "ceper"],
        "jawaban": "Spesifikasi kaki-kaki Honda Brio:\n\n"
                   "- **Ban Satya:** 175/65 R14.\n"
                   "- **Ban RS:** 185/55 R15.\n"
                   "- **Ground Clearance:** 165 mm. Cukup aman untuk polisi tidur perkotaan, tapi hati-hati kalau muatan penuh agar bagian bawah tidak gasruk."
    },
    {
        "tag": "brio_masalah",
        "pola": ["kelemahan brio", "penyakit brio", "kekurangan brio", "berisik", "peredam"],
        "jawaban": "Sebagai asisten jujur, ini beberapa poin yang sering dikeluhkan user Brio:\n\n"
                   "1. **Peredaman Kabin:** Suara ban dan mesin masih cukup terdengar ke dalam (road noise).\n"
                   "2. **Material Interior:** Dominan plastik keras.\n"
                   "3. **Lampu Belakang:** Desainnya simpel (bohlam biasa) belum LED di semua varian.\n\n"
                   "💡 *Tips: Banyak user menambah peredam tambahan di pintu untuk bikin kabin lebih senyap.*"
    },
    {
        "tag": "agya_gr_umum",
        "pola": ["apa itu agya gr", "kelebihan agya gr", "kenapa beli agya", "agya sport", "gr sport"],
        "jawaban": "Toyota Agya GR Sport adalah varian tertinggi dari Agya yang punya karakter berkendara lebih agresif.\n\n"
                   "- **Kelebihan:** Setelan suspensi dan setir (steering) yang lebih mantap, tampilan jauh lebih sporty dengan *bodykit* GR, dan sudah bukan LCGC lagi.\n"
                   "- **Target:** Buat kamu yang pengen mobil mungil tapi punya *feel* berkendara ala mobil balap harian."
    },
    {
        "tag": "agya_gr_mesin",
        "pola": ["mesin agya", "cc agya", "tenaga agya", "3 silinder", "performa agya gr"],
        "jawaban": "Dapur pacu Toyota Agya GR Sport menggunakan mesin baru:\n\n"
                   "- **Tipe:** 1.200cc 3-Silinder Dual VVT-i (Kode WA-VE).\n"
                   "- **Tenaga:** **88 PS** pada 6.000 rpm.\n"
                   "- **Torsi:** **113 Nm** pada 4.500 rpm.\n\n"
                   "Walaupun 3 silinder, torsinya lebih besar di putaran bawah dibanding Brio, jadi tarikan awal terasa lebih enteng!"
    },
    {
        "tag": "agya_vs_brio",
        "pola": ["agya vs brio", "pilih agya atau brio", "bagusan mana brio agya", "perbandingan agya brio"],
        "jawaban": "Pertempuran abadi! Ini bedanya:\n\n"
                   "1. **Mesin:** Brio (4-silinder) lebih halus/minim getaran. Agya (3-silinder) punya torsi awal lebih galak.\n"
                   "2. **Fitur:** Agya GR Sport menang telak di fitur (sudah ada *Wireless Charging*, layar 8 inch, dan panel instrumen digital).\n"
                   "3. **Handling:** Brio lebih lincah (*go-kart feel*), Agya GR Sport lebih stabil di kecepatan tinggi karena suspensi khusus GR."
    },
    {
        "tag": "agya_gr_fitur",
        "pola": ["fitur agya gr", "kelebihan fitur agya", "interior agya gr", "dashboard agya", "teknologi agya"],
        "jawaban": "Fitur di Agya GR Sport ini kelasnya sudah di atas LCGC:\n\n"
                   "- **Paddle Shift:** Bisa oper gigi dari setir (keren banget buat harga segini!).\n"
                   "- **Power Mode:** Tombol di setir buat bikin akselerasi lebih responsif saat mau nyalip.\n"
                   "- **Digital AC:** Tampilan AC sudah digital yang rapi dan modern.\n"
                   "- **GR Parts:** Jok, setir, hingga *scuff plate* semuanya berlogo GR Sport yang eksklusif."
    },
    {
        "tag": "agya_gr_kaki",
        "pola": ["ban agya gr", "velg agya gr", "suspensi agya gr", "empuk gak agya", "ground clearance agya"],
        "jawaban": "Kaki-kaki Agya GR Sport berbeda dengan Agya standar:\n\n"
                   "- **Tuning Khusus:** *Shock absorber* dan *coil spring* disetel lebih keras biar gak limbung pas belok tajam.\n"
                   "- **Ban:** Menggunakan profil 185/55 R15 dengan *velg machining alloy* yang sporty.\n"
                   "- **Radius Putar:** Sangat kecil (4,5 meter), paling jago buat putar balik di jalan sempit."
    },
    {
        "tag": "agya_gr_pajak",
        "pola": ["pajak agya gr", "biaya stnk agya", "pajak tahunan agya"],
        "jawaban": "Estimasi pajak tahunan Toyota Agya GR Sport (Non-LCGC):\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,2 jt - Rp 3,8 jt** per tahun.\n"
                   "*(Karena sudah tidak masuk skema LCGC, pajaknya sedikit lebih tinggi dibanding varian Agya E atau G)*."
    },
    {
        "tag": "avanza_umum",
        "pola": ["apa itu avanza", "kelebihan avanza", "mobil keluarga", "sejuta umat", "toyota avanza"],
        "jawaban": "Toyota Avanza adalah MPV legendaris yang dikenal sebagai 'Mobil Sejuta Umat'. 🚗\n\n"
                   "- **Kelebihan:** Kapasitas 7 penumpang yang luas, jaringan servis ada di setiap sudut Indonesia, dan harga jual kembali yang sangat kuat.\n"
                   "- **Platform Baru:** Generasi terbaru sekarang menggunakan platform **DNGA** (Daihatsu New Global Architecture) yang membuat kabin jauh lebih nyaman dan senyap dibanding model lama."
    },
    {
        "tag": "avanza_mesin",
        "pola": ["mesin avanza", "cc avanza", "tenaga avanza", "1300cc", "1500cc", "performa avanza"],
        "jawaban": "Avanza hadir dengan dua pilihan mesin yang bandel dan irit:\n\n"
                   "1. **1.3L (1NR-VE):** Tenaga **98 PS** dan Torsi **121 Nm**. (Irit buat harian).\n"
                   "2. **1.5L (2NR-VE):** Tenaga **106 PS** dan Torsi **137 Nm**. (Lebih bertenaga buat luar kota).\n\n"
                   "Kedua mesin ini sudah menggunakan teknologi **Dual VVT-i** yang membuat konsumsi BBM tetap efisien meski mobil diisi penuh penumpang."
    },
    {
        "tag": "avanza_fwd_vs_rwd",
        "pola": ["avanza fwd", "avanza rwd", "penggerak depan", "penggerak belakang", "nanjak avanza"],
        "jawaban": "Ini perubahan besar! Avanza terbaru sekarang menggunakan **FWD (Front Wheel Drive)**.\n\n"
                   "- **Kenapa FWD?** Agar kabin lebih luas (tidak ada gundukan transmisi di lantai), lebih irit BBM, dan lebih ringan.\n"
                   "- **Kuat Nanjak Gak?** Dengan sistem transmisi CVT baru dan kontrol traksi (HSA), Avanza tetap mampu melewati tanjakan umum. Namun, untuk tanjakan ekstrem yang licin, penggerak belakang (RWD) di model lama memang sedikit lebih unggul secara mekanis."
    },
    {
        "tag": "avanza_transmisi",
        "pola": ["transmisi avanza", "avanza matic", "cvt avanza", "manual avanza"],
        "jawaban": "Pilihan transmisi Toyota Avanza terbaru:\n\n"
                   "- **CVT (Continuously Variable Transmission):** Perpindahan gigi sangat halus dan responsif, menggantikan transmisi otomatis konvensional 4-speed yang lama.\n"
                   "- **Manual 5-Percepatan:** Masih tersedia buat kamu yang butuh durabilitas tinggi untuk operasional berat atau di daerah perbukitan."
    },
    {
        "tag": "avanza_fitur_tssa",
        "pola": ["fitur avanza", "keselamatan avanza", "tssa", "aman gak", "rem otomatis avanza", "blind spot"],
        "jawaban": "Avanza sekarang sangat canggih dengan fitur **Toyota Safety Sense (TSS)** pada varian tertinggi:\n\n"
                   "- **Pre-Collision Warning & Braking:** Bisa ngerem sendiri kalau ada risiko tabrakan.\n"
                   "- **Lane Departure Assist:** Ngasih peringatan kalau mobil keluar lajur.\n"
                   "- **Blind Spot Monitoring:** Lampu di spion nyala kalau ada kendaraan di titik buta.\n"
                   "- **6 Airbags:** Memberikan perlindungan maksimal untuk seluruh anggota keluarga."
    },
    {
        "tag": "avanza_sofa_mode",
        "pola": ["sofa mode", "kursi avanza", "long sofa", "tidur di mobil", "interior avanza"],
        "jawaban": "Fitur favorit keluarga: **Long Sofa Mode**! ✨\n\n"
                   "Kursi baris kedua dan pertama bisa direbahkan rata sehingga menjadi seperti tempat tidur (sofa). Sangat berguna untuk istirahat saat perjalanan jauh atau saat sedang menunggu di dalam mobil. Kabin jadi terasa sangat fleksibel dan luas!"
    },
    {
        "tag": "avanza_pajak",
        "pola": ["pajak avanza", "stnk avanza", "pajak tahunan avanza", "biaya pajak avanza"],
        "jawaban": "Estimasi pajak tahunan Toyota Avanza terbaru (wilayah Jakarta/Jawa):\n\n"
                   "- **Tipe 1.3:** Sekitar **Rp 3,2 jt - Rp 3,7 jt** per tahun.\n"
                   "- **Tipe 1.5:** Sekitar **Rp 3,8 jt - Rp 4,5 jt** per tahun.\n\n"
                   "*(Angka ini bisa berbeda tergantung tahun produksi dan tarif pajak progresif kamu)*."
    },
    {
        "tag": "xpander_umum",
        "pola": ["xpander", "mitsubishi xpander", "cross", "ultimate", "nyaman", "mpv mitsubishi"],
        "jawaban": "Mitsubishi Xpander adalah MPV yang mendobrak standar kenyamanan di kelasnya. 💎\n\n"
                   "- **Kelebihan Utama:** Suspensi paling empuk di kelasnya (berbasis teknologi Lancer), kedap suara kabin yang sangat baik, dan desain *Dynamic Shield* yang terlihat gagah.\n"
                   "- **Varian:** Ada tipe **Xpander Standard** dan **Xpander Cross** yang lebih tinggi (SUV look) dengan *ground clearance* mencapai 220 mm."
    },
    {
        "tag": "xpander_mesin",
        "pola": ["mesin xpander", "cc xpander", "tenaga xpander", "mivec", "performa xpander"],
        "jawaban": "Xpander mengandalkan mesin yang sudah teruji daya tahannya:\n\n"
                   "- **Tipe:** 1.5L MIVEC DOHC 16-Valve.\n"
                   "- **Tenaga:** **105 PS** pada 6.000 rpm.\n"
                   "- **Torsi:** **141 Nm** pada 4.000 rpm.\n\n"
                   "Mesin MIVEC ini dirancang untuk memberikan keseimbangan antara performa yang bertenaga dan efisiensi bahan bakar."
    },
    {
        "tag": "xpander_transmisi",
        "pola": ["transmisi xpander", "matic xpander", "cvt xpander", "manual xpander"],
        "jawaban": "Perubahan besar pada Xpander terbaru adalah transmisinya:\n\n"
                   "- **New CVT:** Menggantikan transmisi AT 4-percepatan lama. Hasilnya, akselerasi jadi jauh lebih halus dan konsumsi BBM lebih irit saat cruising di jalan tol.\n"
                   "- **Manual:** Tetap tersedia 5-percepatan untuk yang ingin kontrol penuh dan biaya perawatan jangka panjang yang lebih simpel."
    },
    {
        "tag": "xpander_fitur_ayc",
        "pola": ["ayc", "active yaw control", "fitur xpander", "rem parkir elektrik", "epb", "autohold"],
        "jawaban": "Xpander punya fitur 'sakti' dari Lancer Evolution, yaitu **Active Yaw Control (AYC)**!\n\n"
                   "- **AYC:** Membantu mobil tetap stabil saat bermanuver di tikungan tajam atau jalan licin dengan mengatur gaya pengereman pada roda depan secara otomatis.\n"
                   "- **Interior:** Sudah pakai **Electric Parking Brake (EPB)** dengan *Auto Hold*, jadi nggak perlu capek tarik rem tangan saat macet."
    },
    {
        "tag": "xpander_vs_avanza",
        "pola": ["xpander vs avanza", "bagusan xpander atau avanza", "pilih xpander atau avanza", "beda xpander avanza"],
        "jawaban": "Duel maut MPV! Ini perbandingannya:\n\n"
                   "1. **Kenyamanan:** Xpander menang di keempukan suspensi dan kekedapan kabin.\n"
                   "2. **Fitur Safety:** Avanza menang dengan paket TSS (Toyota Safety Sense)-nya.\n"
                   "3. **Purna Jual:** Keduanya sama-sama kuat, tapi jaringan servis Toyota memang lebih luas hingga ke pelosok daerah."
    },
    {
        "tag": "xpander_pajak",
        "pola": ["pajak xpander", "biaya stnk xpander", "pajak tahunan xpander"],
        "jawaban": "Estimasi pajak tahunan Mitsubishi Xpander (wilayah Jakarta/Jawa):\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,8 jt - Rp 4,8 jt** per tahun (tergantung tipe, tipe Ultimate/Cross paling tinggi).\n\n"
                   "*(Ingat, nilai pajak sangat dipengaruhi oleh tarif progresif kendaraan keberapa yang kamu miliki)*."
    },
    {
        "tag": "ertiga_umum",
        "pola": ["ertiga", "suzuki ertiga", "hybrid", "smart hybrid", "mpv suzuki", "amanah"],
        "jawaban": "Suzuki Ertiga Smart Hybrid adalah pelopor MPV keluarga yang menggunakan teknologi elektrifikasi terjangkau. 🔋\n\n"
                   "- **Kelebihan Utama:** Konsumsi BBM paling irit di kelasnya, suspensi sangat nyaman dan empuk, serta biaya perawatan yang terkenal murah (Amanah).\n"
                   "- **Teknologi:** Menggunakan sistem *Integrated Starter Generator* (ISG) yang membantu mesin saat akselerasi dan menghemat bensin."
    },
    {
        "tag": "ertiga_mesin_hybrid",
        "pola": ["mesin ertiga", "cara kerja hybrid ertiga", "isg suzuki", "lithium ion ertiga", "baterai ertiga"],
        "jawaban": "Mesin Ertiga Hybrid menggunakan unit K15B 1.500cc yang dipadukan dengan **Integrated Starter Generator (ISG)**:\n\n"
                   "- **Cara Kerja:** ISG menangkap energi saat perlambatan (deceleration) dan menyimpannya di baterai Lithium-ion. Energi ini dipakai lagi untuk fitur *Auto Start-Stop* dan membantu meringankan beban mesin saat gas awal.\n"
                   "- **Efek:** Akselerasi terasa lebih ringan dan bensin jauh lebih hemat terutama di kondisi *stop-and-go*."
    },
    {
        "tag": "ertiga_vs_rival",
        "pola": ["ertiga vs avanza", "ertiga vs xpander", "mending ertiga atau avanza", "bandingkan ertiga"],
        "jawaban": "Ini posisi Ertiga dibanding rivalnya:\n\n"
                   "1. **VS Avanza:** Ertiga jauh lebih nyaman suspensinya, tapi Avanza unggul di fitur keselamatan aktif (TSS).\n"
                   "2. **VS Xpander:** Keduanya sama-sama empuk, tapi Ertiga punya keunggulan di harga beli yang biasanya lebih kompetitif dan adanya teknologi Hybrid."
    },
    {
        "tag": "ertiga_cruise_control",
        "pola": ["fitur ertiga", "cruise control ertiga", "interior ertiga", "fitur baru ertiga"],
        "jawaban": "Fitur unggulan di Suzuki Ertiga Hybrid tipe SS:\n\n"
                   "- **Cruise Control:** Bisa jaga kecepatan stabil di jalan tol tanpa perlu injak pedal gas (sangat jarang ada di kelas MPV harga segini).\n"
                   "- **Guide Me Light:** Lampu depan tetap nyala beberapa saat setelah mesin mati untuk menerangi jalan kamu masuk ke rumah.\n"
                   "- **Interior:** Kabin didominasi warna hitam dengan panel kayu (*wood grain*) yang bikin kesan mewah."
    },
    {
        "tag": "ertiga_pajak",
        "pola": ["pajak ertiga", "stnk ertiga", "biaya pajak tahunan ertiga"],
        "jawaban": "Estimasi pajak tahunan Suzuki Ertiga Hybrid:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,4 jt - Rp 4,1 jt** per tahun.\n\n"
                   "*(Menariknya, meskipun Hybrid, pajak tahunannya tetap normal karena skemanya masih dianggap mobil bensin oleh pemerintah, belum dapat insentif 0% seperti mobil listrik murni)*."
    },
    {
        "tag": "stargazer_umum",
        "pola": ["stargazer", "hyundai stargazer", "mobil pesawat", "stargazer x", "mpv hyundai"],
        "jawaban": "Hyundai Stargazer adalah MPV futuristik yang menawarkan teknologi tercanggih di kelasnya. 🚀\n\n"
                   "- **Kelebihan Utama:** Fitur keamanan paling lengkap, desain lampu LED horizontal yang ikonik (Horizon DRL), dan adanya fitur Bluelink.\n"
                   "- **Kenyamanan:** Tersedia opsi *Captain Seat* (kursi baris kedua terpisah) yang bikin kabin terasa lebih mewah dan lega."
    },
    {
        "tag": "stargazer_mesin_ivt",
        "pola": ["mesin stargazer", "ivt stargazer", "tenaga stargazer", "performa stargazer", "cc stargazer"],
        "jawaban": "Dapur pacu Stargazer menggunakan mesin Smartstream:\n\n"
                   "- **Tipe:** 1.5L MPI dengan transmisi **IVT (Intelligent Variable Transmission)**.\n"
                   "- **Tenaga:** **115 PS** (Terbesar di kelas MPV 1.500cc!).\n"
                   "- **Torsi:** **144 Nm**.\n\n"
                   "Berbeda dengan CVT biasa, transmisi IVT Hyundai menggunakan rantai baja (*chain belt*), sehingga perpindahan gigi lebih responsif dan lebih kuat menahan beban."
    },
    {
        "tag": "stargazer_bluelink",
        "pola": ["bluelink", "aplikasi hp stargazer", "sos stargazer", "nyalain mesin pakai hp", "fitur bluelink"],
        "jawaban": "Fitur 'Sakti' Stargazer adalah **Hyundai BlueLink**! 📱\n\n"
                   "- **Remote Start:** Kamu bisa memanaskan mesin dan menyalakan AC hanya lewat aplikasi di HP sebelum masuk mobil.\n"
                   "- **Tombol SOS:** Di plafon mobil ada tombol SOS yang langsung menghubungkan kamu ke Call Center Hyundai jika ada darurat atau kecelakaan.\n"
                   "- **Auto Collision Notification:** Mobil otomatis lapor lokasi ke pusat bantuan jika airbag mengembang."
    },
    {
        "tag": "stargazer_smartsense",
        "pola": ["smartsense", "fitur safety stargazer", "rem otomatis stargazer", "lane keeping", "aman gak stargazer"],
        "jawaban": "Stargazer dibekali paket keselamatan **Hyundai SmartSense**:\n\n"
                   "- **Forward Collision-Avoidance Assist (FCA):** Ngerem sendiri kalau ada potensi tabrakan depan.\n"
                   "- **Lane Keeping Assist (LKA):** Setir bisa gerak sendiri biar mobil nggak keluar jalur.\n"
                   "- **Rear Cross-Traffic Assist:** Ngasih tahu kalau ada mobil lewat pas kamu lagi mundur dari parkiran."
    },
    {
        "tag": "stargazer_vs_rival",
        "pola": ["stargazer vs avanza", "stargazer vs xpander", "bagusan stargazer atau xpander", "pilih stargazer"],
        "jawaban": "Perbandingan Stargazer dengan kompetitor:\n\n"
                   "1. **VS Avanza:** Stargazer punya tenaga mesin lebih besar dan fitur aplikasi HP (Bluelink), tapi Avanza punya jaringan servis lebih merata.\n"
                   "2. **VS Xpander:** Stargazer lebih unggul di performa mesin dan fitur pintar, tapi Xpander masih lebih unggul di keempukan suspensinya."
    },
    {
        "tag": "stargazer_pajak",
        "pola": ["pajak stargazer", "biaya stnk stargazer", "pajak tahunan hyundai stargazer"],
        "jawaban": "Estimasi pajak tahunan Hyundai Stargazer:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,9 jt - Rp 4,7 jt** per tahun (tergantung tipe, tipe Prime paling mahal).\n\n"
                   "*(Nilai pajak ini relatif bersaing dengan Xpander dan Avanza tipe tertinggi)*."
    },
    {
        "tag": "rush_umum",
        "pola": ["rush", "toyota rush", "terios", "kembar", "suv toyota", "rush gr sport"],
        "jawaban": "Toyota Rush adalah SUV 7-seater yang terkenal sangat tangguh untuk segala medan di Indonesia. 🏔️\n\n"
                   "- **Kelebihan Utama:** Menggunakan penggerak roda belakang (RWD) yang kuat nanjak, *ground clearance* tinggi (220 mm), dan biaya perawatan yang sangat terjangkau.\n"
                   "- **Karakter:** Berbeda dengan Avanza yang sekarang lebih lembut, Rush tetap mempertahankan sasis semi-unibody yang lebih kokoh untuk beban berat."
    },
    {
        "tag": "rush_rwd_nanjak",
        "pola": ["nanjak rush", "rwd rush", "penggerak belakang rush", "kuat nanjak", "tanjakan curam"],
        "jawaban": "Inilah alasan kenapa Rush tetap laku keras: **Real Rear Wheel Drive (RWD)**! ⚙️\n\n"
                   "Saat mobil penuh penumpang dan melewati tanjakan curam, beban mobil akan pindah ke roda belakang. Karena roda belakang yang mendorong (RWD), traksi ban jadi lebih kuat dan tidak mudah selip dibandingkan mobil penggerak depan (FWD).\n\n"
                   "Sangat cocok untuk medan di Indonesia yang banyak perbukitan."
    },
    {
        "tag": "rush_mesin",
        "pola": ["mesin rush", "cc rush", "tenaga rush", "konsumsi bbm rush", "irit gak rush"],
        "jawaban": "Dapur pacu Toyota Rush mengandalkan mesin yang sudah teruji:\n\n"
                   "- **Tipe:** 1.5L 4-silinder Dual VVT-i (Kode 2NR-VE).\n"
                   "- **Tenaga:** **104 PS** dan Torsi **136 Nm**.\n"
                   "- **Konsumsi BBM:** Rata-rata **11-13 km/liter** di dalam kota dan bisa **15-16 km/liter** di jalan tol.\n\n"
                   "Meskipun bukan yang paling kencang, mesin ini dikenal sangat 'bandel' dan jarang ada masalah besar."
    },
    {
        "tag": "rush_gr_sport",
        "pola": ["rush gr sport", "fitur rush", "interior rush", "kelebihan rush gr", "aman gak rush"],
        "jawaban": "Varian tertinggi **Rush GR Sport** hadir dengan peningkatan fitur:\n\n"
                   "- **Safety:** Sudah dilengkapi 6 SRS Airbags dan Vehicle Stability Control (VSC).\n"
                   "- **New Bumper:** Tampilan eksterior lebih macho dengan *bodykit* GR Sport.\n"
                   "- **Fitur Kenyamanan:** Spion lipat otomatis, AC Digital, dan sistem hiburan layar sentuh yang bisa terkoneksi ke smartphone."
    },
    {
        "tag": "rush_vs_xpander_cross",
        "pola": ["rush vs xpander cross", "bagusan rush atau xpander", "pilih rush atau xpander cross"],
        "jawaban": "Pilih sesuai kebutuhan medannya:\n\n"
                   "1. **Pilih Toyota Rush:** Jika kamu sering lewat jalanan rusak, tanjakan curam, atau daerah pedalaman karena sistem RWD-nya lebih tangguh.\n"
                   "2. **Pilih Xpander Cross:** Jika kamu mengutamakan kenyamanan suspensi yang empuk dan kabin yang lebih mewah untuk penggunaan di dalam kota atau jalan tol."
    },
    {
        "tag": "rush_pajak",
        "pola": ["pajak rush", "stnk rush", "biaya pajak tahunan rush"],
        "jawaban": "Estimasi pajak tahunan Toyota Rush (wilayah Jakarta/Jawa):\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,5 jt - Rp 4,4 jt** per tahun.\n\n"
                   "*(Cukup kompetitif untuk kategori SUV 1.500cc)*."
    },
    {
        "tag": "brv_umum",
        "pola": ["brv", "honda brv", "br-v", "lsuv honda", "all new brv", "brv n7x"],
        "jawaban": "All New Honda BR-V adalah kombinasi antara kenyamanan MPV dan ketangguhan SUV. 🏆\n\n"
                   "- **Kelebihan Utama:** Memiliki fitur keselamatan Honda SENSING, mesin paling bertenaga di kelasnya (121 PS), dan kabin yang jauh lebih senyap dibanding generasi sebelumnya.\n"
                   "- **Karakter:** Cocok buat keluarga yang ingin mobil aman untuk perjalanan jauh dengan performa mesin yang responsif."
    },
    {
        "tag": "brv_mesin_performa",
        "pola": ["mesin brv", "tenaga brv", "performa brv", "cc brv", "brv kenceng gak"],
        "jawaban": "Honda BR-V memegang gelar mesin paling bertenaga di kelas LSUV 1.500cc:\n\n"
                   "- **Tipe:** 1.5L DOHC i-VTEC (Berbeda dengan mesin Brio yang masih SOHC).\n"
                   "- **Tenaga:** **121 PS** pada 6.600 rpm.\n"
                   "- **Torsi:** **145 Nm** pada 4.300 rpm.\n\n"
                   "Mesin DOHC ini memberikan nafas yang lebih panjang saat dipacu di jalan tol dibandingkan rival-rivalnya."
    },
    {
        "tag": "brv_honda_sensing",
        "pola": ["honda sensing", "fitur keselamatan brv", "rem otomatis honda", "acc brv", "aman gak brv"],
        "jawaban": "Fitur unggulan BR-V adalah **Honda SENSING** (pada tipe tertinggi):\n\n"
                   "- **Lead Car Departure Notification:** Ngasih tahu kalau mobil depan sudah jalan pas macet (biar nggak diklakson orang!).\n"
                   "- **Adaptive Cruise Control (ACC):** Bisa ngikutin kecepatan mobil depan secara otomatis.\n"
                   "- **Lane Keeping Assist:** Menjaga mobil tetap di tengah lajur.\n"
                   "- **CMBS:** Sistem rem otomatis jika terdeteksi potensi tabrakan."
    },
    {
        "tag": "brv_fitur_lanewatch",
        "pola": ["lanewatch", "kamera spion brv", "fitur brv", "interior brv", "remote engine start brv"],
        "jawaban": "Selain Honda SENSING, BR-V punya fitur unik:\n\n"
                   "- **Honda LaneWatch:** Kamera di spion kiri yang muncul di layar tengah saat kamu sein kiri. Sangat membantu melihat motor/titik buta (*blind spot*).\n"
                   "- **Remote Engine Start:** Bisa menyalakan mesin dan AC dari kunci remote sebelum kamu masuk ke mobil.\n"
                   "- **Walk-Away Auto Lock:** Pintu otomatis terkunci saat kamu berjalan menjauh dari mobil membawa kunci."
    },
    {
        "tag": "brv_vs_rush",
        "pola": ["brv vs rush", "bagusan brv atau rush", "pilih brv atau rush", "beda brv rush"],
        "jawaban": "Pilih sesuai prioritas kamu:\n\n"
                   "1. **Pilih Honda BR-V:** Jika kamu mengutamakan kenyamanan berkendara, performa mesin kencang, dan fitur keselamatan aktif (Honda SENSING).\n"
                   "2. **Pilih Toyota Rush:** Jika kamu sering melewati medan sangat berat/tanjakan ekstrem karena sistem penggerak roda belakangnya (RWD) lebih tangguh untuk disiksa."
    },
    {
        "tag": "brv_pajak",
        "pola": ["pajak brv", "stnk brv", "biaya pajak tahunan brv"],
        "jawaban": "Estimasi pajak tahunan All New Honda BR-V:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 4,2 jt - Rp 5,2 jt** per tahun (tergantung tipe, varian Prestige with Honda SENSING paling tinggi).\n\n"
                   "*(Pajaknya sedikit di atas Rush karena nilai jual kendaraannya yang juga lebih tinggi)*."
    },
     {
        "tag": "mobilio_umum",
        "pola": ["mobilio", "honda mobilio", "mpv honda", "mobilio bekas", "lmpv honda"],
        "jawaban": "Honda Mobilio dikenal sebagai MPV yang paling asyik dikendarai (*driver oriented*) di kelasnya. 🏎️\n\n"
                   "- **Kelebihan Utama:** Posisi berkendara rendah seperti sedan, mesin sangat responsif, dan konsumsi BBM yang sangat irit.\n"
                   "- **Status:** Saat ini Honda lebih fokus menjual Mobilio untuk pasar *fleet* (operasional perusahaan), namun unit bekasnya masih sangat diburu karena performanya yang legendaris."
    },
    {
        "tag": "mobilio_mesin_kencang",
        "pola": ["mesin mobilio", "tenaga mobilio", "performa mobilio", "vtec mobilio", "mobilio kenceng"],
        "jawaban": "Mobilio menggunakan mesin yang sama dengan kakaknya, BR-V generasi pertama:\n\n"
                   "- **Tipe:** 1.5L SOHC 4-Silinder i-VTEC.\n"
                   "- **Tenaga:** **118 PS** pada 6.600 rpm.\n"
                   "- **Torsi:** **145 Nm** pada 4.600 rpm.\n\n"
                   "Mesin ini adalah yang paling bertenaga di kelas Low MPV pada masanya, membuat Mobilio sangat mudah menyalip di jalan tol."
    },
    {
        "tag": "mobilio_vs_rival",
        "pola": ["mobilio vs avanza", "mobilio vs ertiga", "mending mobilio atau avanza", "kelebihan mobilio"],
        "jawaban": "Perbandingan Mobilio dengan kompetitor:\n\n"
                   "1. **VS Avanza:** Mobilio jauh lebih lincah dan stabil di kecepatan tinggi, tapi Avanza unggul di *ground clearance* yang lebih tinggi untuk jalan rusak.\n"
                   "2. **VS Ertiga:** Ertiga lebih nyaman suspensinya dan kabin lebih senyap, sedangkan Mobilio menang di performa mesin dan *image* sporty."
    },
    {
        "tag": "mobilio_kekurangan",
        "pola": ["kekurangan mobilio", "kelemahan mobilio", "penyakit mobilio", "ground clearance mobilio", "berisik mobilio"],
        "jawaban": "Sebagai asisten otomotif, ini beberapa poin yang perlu diperhatikan dari Mobilio:\n\n"
                   "1. **Ground Clearance Rendah:** Hanya 189 mm, paling rendah di kelasnya, sehingga rawan 'gasruk' kalau bawa muatan penuh lewat polisi tidur.\n"
                   "2. **Peredaman Kabin:** Suara dari luar (road noise) cukup masuk ke dalam kabin.\n"
                   "3. **Dashboard:** Desain interior generasi awal dianggap terlalu sederhana, meski sudah diperbaiki di versi *facelift*."
    },
    {
        "tag": "mobilio_pajak",
        "pola": ["pajak mobilio", "stnk mobilio", "biaya pajak tahunan mobilio"],
        "jawaban": "Estimasi pajak tahunan Honda Mobilio:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 2,8 jt - Rp 3,8 jt** per tahun (tergantung tahun dan tipe, tipe RS paling tinggi).\n\n"
                   "*(Termasuk MPV dengan pajak yang cukup ramah di kantong mahasiswa atau keluarga muda)*."
    },
    {
        "tag": "livina_umum",
        "pola": ["livina", "nissan livina", "all new livina", "livina terbaru", "mpv nissan"],
        "jawaban": "Nissan Livina adalah MPV yang menggabungkan ketangguhan basis Xpander dengan kenyamanan khas Nissan. 🛋️\n\n"
                   "- **Kelebihan Utama:** Kursi 'Zero Gravity' yang sangat empuk dan tidak bikin cepat lelah, desain eksterior V-Motion yang elegan, dan fitur hiburan yang lengkap.\n"
                   "- **Karakter:** Cocok buat kamu yang suka basis mesin Xpander tapi ingin tampilan yang lebih kalem, dewasa, dan tidak terlalu agresif."
    },
    {
        "tag": "livina_vs_xpander",
        "pola": ["bedanya livina dan xpander", "livina vs xpander", "bagusan livina atau xpander", "pilih livina atau xpander"],
        "jawaban": "Meskipun satu basis, ini perbedaan utamanya:\n\n"
                   "1. **Wajah (Grille):** Livina pakai bahasa desain V-Motion Nissan yang lebih elegan, Xpander pakai Dynamic Shield yang lebih gahar.\n"
                   "2. **Interior:** Livina pakai material kursi kulit premium (pada tipe VL) yang lebih lembut dibanding Xpander.\n"
                   "3. **Lampu:** Bentuk lampu DRL dan lampu utama Livina berbeda total dengan Xpander.\n\n"
                   "Secara teknis (mesin, transmisi, suspensi) keduanya identik, jadi ketersediaan suku cadang sangat aman!"
    },
    {
        "tag": "livina_mesin",
        "pola": ["mesin livina", "tenaga livina", "cc livina", "performa livina", "mivec livina"],
        "jawaban": "Mesin Nissan Livina sama dengan Xpander karena hasil kerjasama aliansi:\n\n"
                   "- **Tipe:** 1.5L 4-Silinder MIVEC.\n"
                   "- **Tenaga:** **104 PS** dan Torsi **141 Nm**.\n"
                   "- **Karakter:** Sangat efisien untuk penggunaan harian dan memiliki durabilitas yang sudah teruji di berbagai kondisi jalan Indonesia."
    },
    {
        "tag": "livina_kenyamanan",
        "pola": ["kursi livina", "nyaman gak livina", "interior livina VL", "kedap suara livina"],
        "jawaban": "Kenyamanan adalah 'jualan utama' Nissan Livina:\n\n"
                   "- **Zero Gravity Seat:** Desain kursi yang terinspirasi teknologi NASA, membantu mengurangi kelelahan punggung saat perjalanan jauh.\n"
                   "- **Kekedapan:** Nissan menambahkan beberapa material peredam ekstra sehingga kabin Livina terasa sedikit lebih senyap dibandingkan MPV sekelasnya."
    },
    {
        "tag": "livina_pajak",
        "pola": ["pajak livina", "stnk livina", "biaya pajak tahunan nissan livina"],
        "jawaban": "Estimasi pajak tahunan Nissan Livina:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,6 jt - Rp 4,5 jt** per tahun (tergantung tipe, varian VL paling tinggi).\n\n"
                   "*(Harganya hampir mirip dengan Xpander karena NJKB-nya berada di rentang yang sama)*."
    },
    {
        "tag": "jazz_umum",
        "pola": ["jazz", "honda jazz", "gk5", "jazz rs", "hatchback honda", "mobil gaul"],
        "jawaban": "Honda Jazz adalah ikon mobil anak muda yang sporty dan sangat praktis. 🏎️✨\n\n"
                   "- **Kelebihan Utama:** Mesin paling bertenaga di kelasnya, fitur *Ultra Seat* yang sangat fleksibel, dan desain yang tetap keren meski sudah berumur.\n"
                   "- **Status:** Produksi barunya sudah dihentikan dan diganti oleh Honda City Hatchback, tapi unit bekasnya (terutama model 2014-2021) harganya masih sangat tinggi karena banyak peminat."
    },
    {
        "tag": "jazz_ultra_seat",
        "pola": ["ultra seat", "kursi jazz", "lipat kursi jazz", "bagasi jazz", "magic seat"],
        "jawaban": "Fitur paling sakti di Honda Jazz adalah **Ultra Seat**! 🛋️🔄\n\n"
                   "Kamu bisa melipat kursi belakang dengan 4 mode unik:\n"
                   "1. **Utility Mode:** Kursi rata lantai untuk bawa barang besar (seperti sepeda).\n"
                   "2. **Tall Mode:** Dudukan kursi belakang dilipat ke atas untuk bawa barang tinggi (seperti tanaman hias/pot).\n"
                   "3. **Long Mode:** Kursi depan & belakang direbahkan untuk bawa barang panjang (seperti papan selancar).\n"
                   "4. **Refresh Mode:** Kursi depan direbahkan total jadi tempat tidur. Cocok buat istirahat di parkiran kampus!"
    },
    {
        "tag": "jazz_mesin_performa",
        "pola": ["mesin jazz", "tenaga jazz", "performa jazz", "jazz kenceng", "kecepatan jazz", "l15b"],
        "jawaban": "Performa mesin Honda Jazz (GK5) sering jadi standar di kelasnya:\n\n"
                   "- **Tipe:** 1.5L SOHC 4-Silinder i-VTEC.\n"
                   "- **Tenaga:** **120 PS** (Paling tinggi di masanya dibandingkan Yaris atau Mazda2).\n"
                   "- **Torsi:** **145 Nm**.\n\n"
                   "Mesin i-VTEC Honda sangat responsif di putaran atas, bikin Jazz enak banget buat diajak 'lari' di jalan tol."
    },
    {
        "tag": "jazz_vs_yaris",
        "pola": ["jazz vs yaris", "bagusan jazz atau yaris", "pilih jazz atau yaris", "mending jazz atau yaris"],
        "jawaban": "Duel abadi Hatchback! Ini perbandingannya:\n\n"
                   "1. **Honda Jazz:** Menang di tenaga mesin, kelegaan kabin, dan fleksibilitas kursi (Ultra Seat). Feel berkendaranya lebih sporty.\n"
                   "2. **Toyota Yaris:** Menang di kenyamanan suspensi yang lebih empuk, jumlah airbag lebih banyak (7 titik pada tipe tertinggi), dan radius putar yang lebih kecil."
    },
    {
        "tag": "jazz_pajak",
        "pola": ["pajak jazz", "stnk jazz", "biaya pajak tahunan honda jazz"],
        "jawaban": "Estimasi pajak tahunan Honda Jazz (GK5):\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,5 jt - Rp 4,5 jt** per tahun (tergantung tahun produksi dan tipe RS/S).\n\n"
                   "*(Harganya tetap stabil karena NJKB Honda Jazz tidak banyak turun meski sudah ada penggantinya)*."
    },
    {
        "tag": "yaris_umum",
        "pola": ["yaris", "toyota yaris", "yaris joker", "yaris lele", "hatchback toyota", "gr sport yaris"],
        "jawaban": "Toyota Yaris adalah hatchback andalan Toyota yang dikenal sangat nyaman dan memiliki fitur keselamatan paling lengkap di kelasnya. 🛡️✨\n\n"
                   "- **Kelebihan Utama:** Suspensi lebih empuk dibanding rivalnya, fitur keselamatan melimpah (7 Airbags), dan mesin 2NR-FE yang sangat bandel serta mudah perawatannya.\n"
                   "- **Varian Terbaru:** Sekarang hadir dengan varian **GR Sport** yang punya tampilan jauh lebih agresif dan handling yang telah ditingkatkan."
    },
    {
        "tag": "yaris_safety",
        "pola": ["safety yaris", "airbag yaris", "aman gak yaris", "fitur keselamatan yaris", "7 airbag"],
        "jawaban": "Toyota Yaris adalah juaranya fitur keselamatan di kelas hatchback! 🛡️\n\n"
                   "- **7 SRS Airbags:** Bahkan untuk tipe terendah sekalipun, Yaris sudah dibekali 7 titik airbag (Depan, Samping, Tirai, dan Lutut Pengemudi).\n"
                   "- **Fitur Lain:** Sudah dilengkapi Vehicle Stability Control (VSC), Hill Start Assist (HSA), dan pengereman ABS + EBD + BA sebagai standar.\n\n"
                   "Ini alasan kenapa Yaris sering dianggap sebagai mobil paling aman buat pengemudi pemula atau mahasiswa."
    },
    {
        "tag": "yaris_mesin",
        "pola": ["mesin yaris", "tenaga yaris", "cc yaris", "performa yaris", "2nr-fe"],
        "jawaban": "Dapur pacu Toyota Yaris menggunakan mesin yang sama dengan Avanza/Sienta namun dengan tuning berbeda:\n\n"
                   "- **Tipe:** 1.5L 4-Silinder Dual VVT-i (Kode 2NR-VE).\n"
                   "- **Tenaga:** **107 PS** dan Torsi **140 Nm**.\n"
                   "- **Karakter:** Meskipun tenaganya di bawah Honda Jazz, mesin ini unggul di durabilitas dan kehalusan suara mesin. Sangat minim getaran dan irit untuk penggunaan harian."
    },
    {
        "tag": "yaris_vs_jazz",
        "pola": ["yaris vs jazz", "bagusan yaris atau jazz", "pilih yaris atau jazz", "beda yaris jazz"],
        "jawaban": "Duel legendaris! Ini panduan pilihnya:\n\n"
                   "1. **Pilih Toyota Yaris:** Jika kamu mengutamakan kenyamanan suspensi yang lembut, fitur keselamatan (banyak airbag), dan biaya servis yang lebih murah.\n"
                   "2. **Pilih Honda Jazz:** Jika kamu mengutamakan performa mesin (lebih kencang), kelegaan kabin, dan fleksibilitas kursi (Ultra Seat)."
    },
    {
        "tag": "yaris_radius_putar",
        "pola": ["radius putar yaris", "yaris lincah gak", "putar balik yaris", "nyetir yaris"],
        "jawaban": "Salah satu kelebihan Toyota Yaris (terutama model terbaru) adalah radius putarnya yang kecil (hanya **5,1 meter**). Ini bikin Yaris sangat lincah buat putar balik di jalan sempit atau bermanuver di parkiran mall yang padat dibandingkan hatchback lain."
    },
    {
        "tag": "yajis_pajak",
        "pola": ["pajak yaris", "stnk yaris", "biaya pajak tahunan toyota yaris"],
        "jawaban": "Estimasi pajak tahunan Toyota Yaris (tipe Joker/GR Sport):\n\n"
                   "- **Pajak:** Berkisar antara **Rp 3,8 jt - Rp 4,8 jt** per tahun.\n\n"
                   "*(Nilai pajak ini cukup stabil dan bersaing ketat dengan Honda Jazz)*."
    },
    {
        "tag": "innova_reborn_umum",
        "pola": ["innova reborn", "kijang innova", "innova diesel", "innova bensin", "mobil badak", "reborn"],
        "jawaban": "Toyota Innova Reborn adalah MPV legendaris yang dikenal sangat tangguh dengan sasis *ladder frame*. 🛡️\n\n"
                   "- **Kelebihan Utama:** Daya tahan mesin luar biasa (terutama diesel), kabin sangat luas dan nyaman, serta nilai jual kembali yang sangat tinggi.\n"
                   "- **Status:** Meskipun sudah ada Innova Zenix, varian Reborn Diesel masih tetap diproduksi dan sangat diminati untuk operasional berat maupun harian karena ketangguhannya."
    },
    {
        "tag": "innova_reborn_mesin_diesel",
        "pola": ["mesin innova diesel", "2gd", "tenaga innova diesel", "torsi innova diesel", "irit gak innova diesel"],
        "jawaban": "Mesin Diesel Innova Reborn (kode 2GD-FTV) adalah favorit semua orang:\n\n"
                   "- **Tipe:** 2.4L VNT Turbo Intercooler.\n"
                   "- **Tenaga:** **149 PS**.\n"
                   "- **Torsi:** **360 Nm** (Gede banget, narik di tanjakan jadi enteng!).\n"
                   "- **Kelebihan:** Sangat responsif untuk akselerasi dan terkenal tahan disiksa jarak jauh."
    },
    {
        "tag": "innova_reborn_mesin_bensin",
        "pola": ["innova bensin irit gak", "mesin innova bensin", "1tr-fe", "konsumsi bbm innova bensin"],
        "jawaban": "Mesin Bensin Innova Reborn menggunakan unit 2.0L (kode 1TR-FE):\n\n"
                   "- **Karakter:** Suara mesin sangat halus dan minim getaran dibandingkan diesel.\n"
                   "- **Konsumsi BBM:** Terkenal agak 'boros' (sekitar 7-9 km/liter dalam kota). \n"
                   "- **Kelebihan:** Perawatannya sangat simpel dan murah dibandingkan versi diesel."
    },
    {
        "tag": "innova_reborn_vs_zenix",
        "pola": ["pilih reborn atau zenix", "bedanya reborn dan zenix", "reborn vs zenix", "zenix penggerak depan"],
        "jawaban": "Ini perbedaan krusialnya, Rayan:\n\n"
                   "1. **Sasis & Penggerak:** Reborn pakai *Ladder Frame* (RWD/Belakang), Zenix pakai *Monocoque* (FWD/Depan).\n"
                   "2. **Karakter:** Reborn lebih cocok untuk jalanan rusak dan beban berat. Zenix lebih ke arah kenyamanan dan efisiensi bahan bakar (Hybrid).\n"
                   "3. **Transmisi:** Reborn pakai transmisi AT konvensional yang bandel, Zenix pakai CVT."
    },
    {
        "tag": "innova_reborn_pajak",
        "pola": ["pajak innova reborn", "stnk innova reborn", "pajak tahunan innova diesel"],
        "jawaban": "Estimasi pajak tahunan Toyota Innova Reborn:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 4,5 jt - Rp 6,5 jt** per tahun (tergantung tahun produksi dan tipe G/V/Venturer).\n\n"
                   "*(Varian Diesel biasanya memiliki pajak yang sedikit lebih mahal dibanding bensin)*."
    },
    {
        "tag": "innova_zenix_umum",
        "pola": ["zenix", "innova zenix", "kijang innova zenix", "zenix hybrid", "zenix bensin", "mpv mewah"],
        "jawaban": "Toyota Innova Zenix adalah evolusi terbaru Kijang yang kini berubah menjadi MPV premium yang sangat nyaman. ✨\n\n"
                   "- **Kelebihan Utama:** Konsumsi BBM sangat irit (terutama tipe Hybrid), kabin jauh lebih luas, dan fitur keselamatan paling lengkap.\n"
                   "- **Platform Baru:** Menggunakan platform **TNGA-C** (sama dengan Voxy/Corolla), yang membuat bantingan suspensinya senyaman sedan mewah."
    },
    {
        "tag": "zenix_hybrid_system",
        "pola": ["mesin zenix", "cara kerja hybrid zenix", "zenix irit", "baterai zenix", "ev mode zenix"],
        "jawaban": "Innova Zenix Hybrid menggunakan teknologi Hybrid Generasi ke-5 Toyota:\n\n"
                   "- **Mesin:** 2.0L M20A-FXS dikombinasikan dengan motor listrik.\n"
                   "- **Konsumsi BBM:** Bisa tembus **20-23 km/liter** (lebih irit dari Brio!).\n"
                   "- **EV Mode:** Di kecepatan rendah, mobil bisa berjalan hanya menggunakan listrik tanpa suara mesin sama sekali."
    },
    {
        "tag": "zenix_fitur_mewah",
        "pola": ["fitur zenix", "panoramic zenix", "ottoman zenix", "interior zenix", "captain seat zenix"],
        "jawaban": "Zenix tipe Q Hybrid punya fitur kelas sultan:\n\n"
                   "- **Panoramic Retractable Roof:** Atap kaca besar yang bisa dibuka.\n"
                   "- **Captain Seat with Ottoman:** Kursi baris kedua punya sandaran kaki elektrik (seperti kursi pesawat First Class).\n"
                   "- **Dual Rear Seat Entertainment:** Ada dua layar monitor di belakang jok depan untuk penumpang baris kedua."
    },
    {
        "tag": "zenix_fwd_pro_kontra",
        "pola": ["zenix fwd", "zenix nanjak", "zenix penggerak depan", "kenapa zenix fwd"],
        "jawaban": "Banyak yang debat soal Zenix jadi FWD (Penggerak Depan):\n\n"
                   "- **Kenapa FWD?** Agar lantai mobil rata (tidak ada gundukan), kabin lebih senyap, dan bobot mobil lebih ringan sehingga lebih irit.\n"
                   "- **Nanjak:** Berkat transmisi **10-Speed Direct Shift CVT** dan *Hill Start Assist*, Zenix tetap mampu melibas tanjakan aspal dengan baik, meski karakternya berbeda dengan Reborn RWD."
    },
    {
        "tag": "zenix_tss",
        "pola": ["tss zenix", "safety zenix", "radar zenix", "aman gak zenix"],
        "jawaban": "Zenix dibekali **Toyota Safety Sense (TSS) 3.0**:\n\n"
                   "- **Adaptive Cruise Control:** Bisa menjaga jarak otomatis hingga mobil berhenti total.\n"
                   "- **Lane Tracing Assist:** Membantu menjaga mobil tetap di tengah lajur secara aktif.\n"
                   "- **Automatic High Beam:** Lampu jauh otomatis mati jika ada mobil dari lawan arah agar tidak menyilaukan."
    },
    {
        "tag": "zenix_pajak",
        "pola": ["pajak zenix", "stnk zenix", "biaya pajak tahunan innova zenix"],
        "jawaban": "Estimasi pajak tahunan Toyota Innova Zenix:\n\n"
                   "- **Tipe G/V Bensin:** Sekitar **Rp 6 jt - Rp 8 jt**.\n"
                   "- **Tipe Q Hybrid:** Sekitar **Rp 9 jt - Rp 11 jt** per tahun.\n\n"
                   "*(Pajaknya cukup tinggi karena NJKB mobil ini masuk kategori mobil mewah/premium)*."
    },
    {
        "tag": "fortuner_umum",
        "pola": ["fortuner", "toyota fortuner", "fortuner gr sport", "mobil gagah", "suv toyota", "fortuner 2.8"],
        "jawaban": "Toyota Fortuner adalah SUV High-Frame yang menjadi simbol kegagahan dan ketangguhan di Indonesia. 🏔️💪\n\n"
                   "- **Kelebihan Utama:** Ground clearance tinggi (cocok buat banjir/jalan rusak), sasis ladder frame yang sangat kuat, dan mesin diesel 2.8L yang sangat bertenaga.\n"
                   "- **Karakter:** Mobil ini dirancang untuk kamu yang ingin tampil berwibawa sekaligus butuh kendaraan yang siap 'disiksa' di berbagai medan jalan."
    },
    {
        "tag": "fortuner_mesin_2800",
        "pola": ["mesin fortuner", "2.8", "1gd", "tenaga fortuner", "torsi fortuner", "fortuner kenceng"],
        "jawaban": "Varian terbaru Fortuner menggunakan mesin 'Monster' (kode 1GD-FTV):\n\n"
                   "- **Kapasitas:** 2.800cc Diesel Turbo VNT.\n"
                   "- **Tenaga:** **203.9 PS**.\n"
                   "- **Torsi:** **500 Nm** (Torsi badak! Tarikan awalnya sangat menjambak).\n\n"
                   "Mesin 1GD ini jauh lebih bertenaga dibandingkan mesin 2.4L (2GD) yang dipakai di Fortuner lama atau Innova Reborn."
    },
    {
        "tag": "fortuner_suspensi_gr",
        "pola": ["suspensi fortuner", "gr sport", "handling fortuner", "limbung gak", "kenyamanan fortuner"],
        "jawaban": "Di varian **GR Sport**, Toyota melakukan tuning khusus pada kaki-kaki:\n\n"
                   "- **New Shock Absorber:** Karakter suspensinya dibuat sedikit lebih kaku untuk mengurangi gejala limbung (body roll) yang sering dikeluhkan pada SUV tinggi.\n"
                   "- **Handling:** Menjadi lebih stabil saat bermanuver di kecepatan tinggi tanpa menghilangkan ketangguhannya di jalan berlubang."
    },
    {
        "tag": "fortuner_vs_pajero",
        "pola": ["fortuner vs pajero", "bagusan fortuner atau pajero", "pilih fortuner atau pajero", "beda fortuner pajero"],
        "jawaban": "Duel abadi SUV Ladder Frame! Ini perbandingannya:\n\n"
                   "1. **Toyota Fortuner:** Menang di torsi mesin (500 Nm), jaringan servis yang sangat luas, dan nilai jual kembali (resale value) yang sedikit lebih kuat.\n"
                   "2. **Mitsubishi Pajero Sport:** Menang di kenyamanan suspensi (lebih empuk), fitur sunroof, dan transmisi 8-percepatan yang lebih halus."
    },
    {
        "tag": "fortuner_fitur_keamanan",
        "pola": ["fitur fortuner", "tss fortuner", "blind spot fortuner", "keamanan fortuner", "kamera 360"],
        "jawaban": "Fortuner terbaru sudah dilengkapi fitur modern:\n\n"
                   "- **Panoramic View Monitor:** Kamera 360 derajat untuk memudahkan parkir mobil sebesar ini.\n"
                   "- **Blind Spot Detection:** Peringatan jika ada mobil di titik buta.\n"
                   "- **Power Back Door with Kick Sensor:** Buka bagasi tinggal ayunkan kaki di bawah bumper belakang."
    },
    {
        "tag": "fortuner_pajak",
        "pola": ["pajak fortuner", "stnk fortuner", "biaya pajak tahunan toyota fortuner"],
        "jawaban": "Estimasi pajak tahunan Toyota Fortuner:\n\n"
                   "- **Pajak:** Berkisar antara **Rp 8 jt - Rp 11 jt** per tahun (tergantung tipe dan tahun).\n\n"
                   "*(Wajar pajak cukup tinggi karena harga unitnya sudah di atas 600-700 juta rupiah)*."
    },
    {
        "tag": "pajero_umum",
        "pola": ["pajero", "pajero sport", "mitsubishi pajero", "dakar", "exceed", "suv mitsubishi", "mobil gagah"],
        "jawaban": "Mitsubishi Pajero Sport adalah SUV ladder-frame yang terkenal dengan kenyamanan dan fitur mewahnya. 💎⛰️\n\n"
                   "- **Kelebihan Utama:** Suspensi paling nyaman di kelasnya, transmisi 8-percepatan yang halus, dan sudah dilengkapi fitur *Sunroof*.\n"
                   "- **Karakter:** Cocok buat kamu yang ingin mobil tangguh untuk *off-road* ringan tapi tetap ingin merasa mewah di dalam kabin."
    },
    {
        "tag": "pajero_mesin_mivec",
        "pola": ["mesin pajero", "4n15", "tenaga pajero", "torsi pajero", "dakar ultimate", "performa pajero"],
        "jawaban": "Pajero Sport (tipe Dakar) menggunakan mesin legendaris 4N15:\n\n"
                   "- **Tipe:** 2.4L MIVEC Turbocharged Intercooled.\n"
                   "- **Tenaga:** **181 PS** pada 3.500 rpm.\n"
                   "- **Torsi:** **430 Nm** pada 2.500 rpm.\n\n"
                   "Meskipun torsinya di bawah Fortuner 2.8, mesin MIVEC ini dikenal sangat halus dan punya penyaluran tenaga yang merata berkat transmisi 8-percepatannya."
    },
    {
        "tag": "pajero_transmisi_8speed",
        "pola": ["transmisi pajero", "matic pajero", "gigi pajero", "8 speed", "halus gak"],
        "jawaban": "Salah satu senjata utama Pajero Sport adalah **Transmisi Otomatis 8-Percepatan**.\n\n"
                   "- **Kelebihan:** Perpindahan gigi sangat halus dan menjaga putaran mesin tetap optimal, sehingga konsumsi BBM lebih efisien saat diajak lari kencang di jalan tol.\n"
                   "- **Paddle Shift:** Ada tuas di balik setir untuk pindah gigi manual, memberikan sensasi berkendara yang lebih sporty."
    },
    {
        "tag": "pajero_fitur_mewah",
        "pola": ["fitur pajero", "sunroof pajero", "dashboard pajero", "interior pajero", "rem tangan elektrik pajero"],
        "jawaban": "Pajero Sport punya interior yang terasa lebih 'mahal':\n\n"
                   "- **Sunroof:** Satu-satunya di kelasnya yang punya lubang kaca di atap untuk menikmati pemandangan.\n"
                   "- **Electric Parking Brake:** Sudah pakai rem tangan elektrik dengan *Auto Hold*.\n"
                   "- **8-inch Color LCD Meter:** Panel instrumen digital yang bisa diubah-ubah tampilannya sesuai keinginan kamu."
    },
    {
        "tag": "pajero_vs_fortuner",
        "pola": ["pajero vs fortuner", "bagusan pajero atau fortuner", "pilih pajero atau fortuner", "beda pajero fortuner"],
        "jawaban": "Ini ringkasan duelnya:\n\n"
                   "1. **Pilih Pajero Sport:** Jika kamu mengejar kenyamanan (suspensi empuk), fitur kabin yang lebih mewah (sunroof), dan transmisi yang lebih halus.\n"
                   "2. **Pilih Toyota Fortuner:** Jika kamu mengejar tenaga mesin yang lebih besar (torsi 500 Nm) dan kemudahan mencari *sparepart* hingga ke pelosok desa."
    },
    {
        "tag": "pajero_pajak",
        "pola": ["pajak pajero", "stnk pajero", "biaya pajak tahunan pajero sport"],
        "jawaban": "Estimasi pajak tahunan Mitsubishi Pajero Sport:\n\n"
                   "- **Tipe Dakar:** Berkisar antara **Rp 9 jt - Rp 12 jt** per tahun.\n"
                   "- **Tipe Exceed:** Sekitar **Rp 6 jt - Rp 8 jt** per tahun.\n\n"
                   "*(Pajak tipe Dakar lebih mahal karena fitur keselamatannya jauh lebih lengkap dan harga barunya lebih tinggi)*."
    },
    {
        "tag": "crv_umum",
        "pola": ["crv", "honda crv", "cr-v", "all new crv", "suv mewah honda", "crv rs"],
        "jawaban": "Honda CR-V adalah SUV premium yang menggabungkan kenyamanan sedan dengan ketangguhan sebuah SUV. 💎🏙️\n\n"
                   "- **Kelebihan Utama:** Handling paling presisi di kelasnya, fitur keselamatan Honda SENSING paling lengkap, dan kini tersedia varian RS e:HEV (Hybrid) yang sangat kencang sekaligus irit.\n"
                   "- **Karakter:** Cocok buat kamu yang mencari mobil dengan citra mewah, nyaman untuk disetir sendiri, dan punya teknologi tercanggih dari Honda."
    },
    {
        "tag": "crv_hybrid_ehev",
        "pola": ["mesin crv", "crv hybrid", "ehev", "tenaga crv", "torsi crv", "crv turbo", "mesin cr-v"],
        "jawaban": "Generasi terbaru CR-V punya dua pilihan mesin hebat:\n\n"
                   "- **2.0L RS e:HEV (Hybrid):** Tenaga kombinasi **207 PS** dan Torsi **335 Nm**. Sangat irit dan tarikannya instan seperti mobil listrik!\n"
                   "- **1.5L VTEC Turbo:** Tenaga **190 PS** dan Torsi **240 Nm**. Tetap bertenaga dengan kapasitas mesin lebih kecil namun dibantu Turbocharger.\n\n"
                   "Varian Hybrid bahkan menggunakan teknologi mesin yang bisa mengisi daya baterai sendiri secara sangat efisien."
    },
    {
        "tag": "crv_honda_connect",
        "pola": ["honda connect", "fitur crv", "aplikasi hp crv", "lacak mobil crv", "fitur canggih crv"],
        "jawaban": "CR-V terbaru dibekali fitur **Honda CONNECT**! 📱🌐\n\n"
                   "- **Digital Key:** Kamu bisa mengunci dan membuka pintu mobil hanya lewat Smartphone.\n"
                   "- **Geofencing:** Memberi notifikasi ke HP jika mobil keluar dari radius jalan yang kamu tentukan.\n"
                   "- **Find My Car:** Membantu menemukan lokasi parkir mobil secara presisi lewat GPS di aplikasi."
    },
    {
        "tag": "crv_interior_audio",
        "pola": ["interior crv", "audio crv", "bose crv", "speaker crv", "kenyamanan crv", "panoramic crv"],
        "jawaban": "Interior CR-V sudah sekelas mobil mewah Eropa:\n\n"
                   "- **Bose Premium Audio:** Dilengkapi 12 speaker Bose (pada tipe RS) yang suaranya sangat jernih.\n"
                   "- **Panoramic Sunroof:** Atap kaca besar yang memberikan kesan luas dan mewah di dalam kabin.\n"
                   "- **Head-Up Display (HUD):** Menampilkan informasi kecepatan di kaca depan agar pengemudi tetap fokus ke jalan."
    },
    {
        "tag": "crv_vs_zenix",
        "pola": ["crv vs zenix", "bagusan crv atau zenix", "pilih crv atau zenix", "beda crv zenix"],
        "jawaban": "Duel SUV vs MPV Premium! Ini bedanya:\n\n"
                   "1. **Pilih Honda CR-V:** Jika kamu lebih suka menyetir sendiri (*driver oriented*), ingin fitur safety paling update, dan butuh audio kualitas tinggi.\n"
                   "2. **Pilih Toyota Zenix:** Jika kamu lebih sering duduk di belakang dengan sopir, karena Zenix punya *Captain Seat* dengan sandaran kaki (Ottoman) yang tidak ada di CR-V."
    },
    {
        "tag": "crv_pajak",
        "pola": ["pajak crv", "stnk crv", "biaya pajak tahunan honda crv"],
        "jawaban": "Estimasi pajak tahunan All New Honda CR-V:\n\n"
                   "- **Tipe Turbo:** Sekitar **Rp 8 jt - Rp 10 jt**.\n"
                   "- **Tipe RS Hybrid:** Bisa mencapai **Rp 11 jt - Rp 13 jt** per tahun.\n\n"
                   "*(Wajar cukup tinggi karena harga barunya sekarang sudah menyentuh angka 700-800 jutaan)*."
    },
    {
        "tag": "alphard_umum",
        "pola": ["alphard", "toyota alphard", "mobil sultan", "vellfire", "mpv mewah", "mobil artis"],
        "jawaban": "Toyota Alphard adalah simbol kemewahan dan kenyamanan tingkat tinggi di Indonesia. 🏰✨\n\n"
                   "- **Kelebihan Utama:** Kenyamanan kursi baris kedua yang tak tertandingi, privasi tingkat tinggi, dan fitur pintu geser elektrik (Power Sliding Door) yang sangat memudahkan akses keluar masuk.\n"
                   "- **Varian:** Sekarang hadir dengan generasi terbaru yang memiliki pilihan mesin Hybrid dan fitur jauh lebih canggih dari model sebelumnya."
    },
    {
        "tag": "alphard_interior_ottoman",
        "pola": ["interior alphard", "kursi alphard", "kenyamanan alphard", "pijat alphard", "captain seat alphard"],
        "jawaban": "Interior Alphard dirancang layaknya kabin pesawat First Class:\n\n"
                   "- **Executive Admiral Seat:** Kursi baris kedua yang sangat lebar dengan sandaran kaki (Ottoman), pemanas, pendingin, hingga fitur pijat.\n"
                   "- **Rear Control Panel:** Ada layar sentuh mini di samping kursi untuk mengatur AC, lampu kabin (Ambience Light), dan tirai jendela secara otomatis.\n"
                   "- **Peredaman:** Kabin Alphard dikenal sangat senyap, bahkan suara hujan atau bising jalanan hampir tidak terdengar di dalam."
    },
    {
        "tag": "alphard_mesin_hybrid",
        "pola": ["mesin alphard", "tenaga alphard", "alphard hybrid", "cc alphard", "alphard irit gak"],
        "jawaban": "Alphard terbaru kini mengandalkan teknologi ramah lingkungan:\n\n"
                   "- **Tipe Hybrid:** Menggunakan mesin 2.5L berkode A25A-FXS yang dipadukan dengan motor listrik. Sangat halus dan jauh lebih irit bensin dibanding generasi lama.\n"
                   "- **Transmisi:** Menggunakan CVT yang sangat halus, sehingga perpindahan tenaga tidak terasa sama sekali oleh penumpang di belakang."
    },
    {
        "tag": "alphard_fitur_pintu",
        "pola": ["fitur alphard", "pintu alphard", "step alphard", "aman gak alphard", "tss alphard"],
        "jawaban": "Banyak fitur cerdas untuk memanjakan penumpangnya:\n\n"
                   "- **Universal Steps:** Ada pijakan kaki otomatis yang keluar saat pintu geser dibuka, memudahkan anak-anak atau lansia naik ke mobil.\n"
                   "- **Dual Panoramic Roof:** Atap kaca ganda kiri dan kanan yang bisa dibuka tirainya secara terpisah.\n"
                   "- **Safety:** Dilengkapi Toyota Safety Sense (TSS) 3.0 paling lengkap, termasuk parkir otomatis (Remote Park)."
    },
    {
        "tag": "alphard_vs_vellfire",
        "pola": ["bedanya alphard dan vellfire", "pilih alphard atau vellfire", "alphard vs vellfire"],
        "jawaban": "Dua saudara kembar dengan aura berbeda:\n\n"
                   "1. **Toyota Alphard:** Lebih fokus ke arah elegan dan mewah (Luxury). Cocok buat pengusaha atau pejabat.\n"
                   "2. **Toyota Vellfire:** Punya tampilan lebih sporty dan agresif dengan aksen krom gelap. Cocok buat kamu yang ingin tampil mewah tapi tetap terlihat berjiwa muda."
    },
    {
        "tag": "alphard_pajak",
        "pola": ["pajak alphard", "stnk alphard", "biaya pajak tahunan toyota alphard"],
        "jawaban": "Estimasi pajak tahunan Toyota Alphard (generasi terbaru):\n\n"
                   "- **Pajak:** Berkisar antara **Rp 18 jt - Rp 25 jt** per tahun.\n\n"
                   "*(Pajak ini sebanding dengan harga unitnya yang sudah menyentuh angka 1,3 hingga 1,6 Miliar Rupiah)*."
    },
    {
        "tag": "aion_umum",
        "pola": ["aion", "gac aion", "aion y plus", "hyptec ht", "mobil listrik aion", "aion indonesia"],
        "jawaban": "Aion adalah merek mobil listrik premium dari GAC yang menawarkan jarak tempuh jauh dan teknologi baterai sangat aman. ⚡🔋\n\n"
                   "- **Model Utama:** Ada **Aion Y Plus** yang kabinnya luas banget, dan **Hyptec HT** yang punya pintu belakang model sayap (Gullwing).\n"
                   "- **Kelebihan:** Menggunakan Magazine Battery yang tahan ledakan dan desain interior yang sangat minimalis namun mewah."
    },
    {
        "tag": "aion_y_plus_kabin",
        "pola": ["aion y plus", "kelebihan aion y", "interior aion y", "kasur aion", "luas aion y"],
        "jawaban": "Aion Y Plus sering disebut 'Apartemen Berjalan' karena kabinnya yang luar biasa luas:\n\n"
                   "- **Kursi Rata:** Kursi depan bisa direbahkan total rata dengan kursi belakang, sehingga tercipta ruang seperti kasur untuk santai atau menonton film.\n"
                   "- **Lantai Rata:** Tidak ada gundukan sama sekali, memberikan ruang kaki (legroom) yang sangat lega untuk penumpang belakang.\n"
                   "- **Jarak Tempuh:** Bisa menempuh hingga **490 km** (NEDC) dalam sekali cas penuh."
    },
    {
        "tag": "hyptec_ht_gullwing",
        "pola": ["hyptec ht", "pintu sayap", "gullwing", "pintu hyptec", "aion paling mewah"],
        "jawaban": "Hyptec HT adalah SUV listrik mewah dari Aion yang sangat ikonik:\n\n"
                   "- **Gullwing Doors:** Pintu belakang terbuka ke atas seperti sayap burung (mirip Tesla Model X), memudahkan akses di ruang sempit dan terlihat sangat sultan.\n"
                   "- **Performa:** Punya tenaga sekitar 340 PS dan bisa akselerasi 0-100 km/jam dalam waktu singkat.\n"
                   "- **Kenyamanan:** Kursi belakang bisa direbahkan hingga 143 derajat, lengkap dengan sandaran kaki elektrik."
    },
    {
        "tag": "aion_magazine_battery",
        "pola": ["baterai aion", "magazine battery", "aman gak baterai aion", "teknologi baterai aion"],
        "jawaban": "Aion punya teknologi keamanan baterai bernama **Magazine Battery**: \n\n"
                   "- **Anti Meledak:** Sudah lulus uji tembak peluru dan uji tusuk paku ekstrem tanpa mengeluarkan api atau asap.\n"
                   "- **Proteksi:** Memiliki pelindung panas tingkat tinggi dan sistem pemutus arus otomatis jika terdeteksi suhu tidak normal."
    },
    {
        "tag": "aion_vs_byd",
        "pola": ["aion vs byd", "bagusan aion atau byd", "pilih aion atau byd", "aion lawan byd"],
        "jawaban": "Perbandingan dua raksasa EV baru:\n\n"
                   "1. **Pilih Aion:** Jika kamu mengutamakan kelegaan kabin yang luar biasa (Y Plus) atau ingin tampil beda dengan desain pintu unik (Hyptec HT).\n"
                   "2. **Pilih BYD:** Jika kamu mengejar performa berkendara yang lebih sporty (Atto 3/Seal) dan reputasi global yang sudah sangat besar."
    },
    {
        "tag": "aion_pajak",
        "pola": ["pajak aion", "stnk aion", "biaya pajak tahunan aion"],
        "jawaban": "Sama seperti mobil listrik murni (CBU/CKD) lainnya di Indonesia:\n\n"
                   "- **Pajak Tahunan (PKB):** Hanya bayar sekitar **Rp 0 - Rp 800 ribuan** saja karena insentif pemerintah untuk kendaraan listrik.\n"
                   "- **BBNKB:** Rp 0 (Gratis biaya balik nama kendaraan baru)."
    },
    {
        "tag": "byd_umum",
        "pola": ["byd", "build your dreams", "byd indonesia", "mobil listrik byd", "byd seal", "byd atto 3", "byd dolphin"],
        "jawaban": "BYD adalah produsen mobil listrik terbesar di dunia yang kini hadir di Indonesia dengan teknologi baterai revolusioner. ⚡🚗\n\n"
                   "- **Model Utama:** BYD Dolphin (City Hatchback), BYD Atto 3 (Family SUV), dan BYD Seal (Sport Sedan).\n"
                   "- **Kelebihan:** Menggunakan Blade Battery yang sangat aman, efisiensi energi yang tinggi, dan fitur teknologi kabin yang sangat modern."
    },
    {
        "tag": "byd_blade_battery",
        "pola": ["blade battery", "baterai byd", "aman gak byd", "teknologi baterai byd", "keunggulan byd"],
        "jawaban": "Senjata utama BYD adalah **Blade Battery**: \n\n"
                   "- **Sangat Aman:** Sudah lulus 'Nail Penetration Test' (ditusuk paku ekstrem tidak meledak atau berasap).\n"
                   "- **Awet:** Memiliki siklus hidup yang sangat panjang hingga bisa menempuh ratusan ribu kilometer tanpa penurunan kualitas yang drastis.\n"
                   "- **Desain:** Bentuknya tipis seperti bilah pisau (blade), sehingga menghemat ruang dan bikin struktur mobil lebih kokoh."
    },
    {
        "tag": "byd_seal_performa",
        "pola": ["byd seal", "seal performance", "kecepatan seal", "0-100 seal", "lawan ionic 6"],
        "jawaban": "BYD Seal adalah 'bintang' di kelas sedan listrik:\n\n"
                   "- **Akselerasi:** Tipe Performance bisa lari 0-100 km/jam hanya dalam **3.8 detik**! 🏎️💨\n"
                   "- **Jarak Tempuh:** Bisa menempuh hingga **580 - 650 km** dalam sekali cas penuh.\n"
                   "- **Teknologi CTB:** *Cell-to-Body technology* yang menyatukan baterai dengan sasis mobil, bikin mobil sangat stabil saat tikungan tajam."
    },
    {
        "tag": "byd_interior_rotating",
        "pola": ["layar byd", "interior byd", "rotating screen", "layar putar", "fitur dalam byd"],
        "jawaban": "Ciri khas interior BYD yang bikin orang takjub adalah **Intelligent Rotating Touchscreen**:\n\n"
                   "- **Layar Putar:** Layar utama di dasbor bisa berputar otomatis dari posisi tidur (Landscape) ke posisi berdiri (Portrait) hanya dengan satu tombol.\n"
                   "- **Entertainment:** Sudah mendukung Apple CarPlay, Android Auto, dan sistem suara berkualitas tinggi yang bikin kabin terasa seperti bioskop berjalan."
    },
    {
        "tag": "byd_v2l",
        "pola": ["v2l byd", "genset berjalan", "colokan listrik byd", "cas laptop di mobil"],
        "jawaban": "Semua model BYD di Indonesia sudah dilengkapi fitur **V2L (Vehicle-to-Load)**:\n\n"
                   "- **Genset Berjalan:** Kamu bisa mencolokkan peralatan listrik rumah tangga (seperti rice cooker, laptop, atau kopi maker) langsung ke mobil.\n"
                   "- **Sangat Berguna:** Sangat membantu saat kamu sedang camping atau saat terjadi mati lampu di rumah."
    },
    {
        "tag": "byd_pajak",
        "pola": ["pajak byd", "stnk byd", "biaya pajak tahunan byd seal", "pajak atto 3"],
        "jawaban": "Karena BYD adalah mobil listrik murni (EV):\n\n"
                   "- **Pajak Tahunan:** Sangat murah, hanya sekitar **Rp 0 - Rp 900 ribuan** (tergantung daerah).\n"
                   "- **Bebas Ganjil Genap:** Kamu bebas lewat jalan protokol Jakarta kapan saja tanpa takut ditilang!"
    },
    {
        "tag": "denza_umum",
        "pola": ["denza", "byd denza", "denza d9", "mpv mewah listrik", "denza indonesia"],
        "jawaban": "Denza adalah brand mewah kolaborasi antara BYD dan Mercedes-Benz. 💎⚡\n\n"
                   "- **Model Utama:** Denza D9, sebuah MPV mewah berukuran besar yang menjadi pesaing kuat Toyota Alphard.\n"
                   "- **Keunggulan:** Menggabungkan teknologi baterai canggih dari BYD dengan sentuhan kemewahan interior khas mobil Eropa."
    },
    {
        "tag": "denza_d9_interior",
        "pola": ["interior denza", "kemewahan denza", "kursi denza d9", "denza vs alphard"],
        "jawaban": "Interior Denza D9 dirancang untuk kenyamanan maksimal (VIP): \n\n"
                   "- **Layar di Mana-mana:** Ada layar di dasbor, layar besar untuk penumpang belakang, bahkan ada layar kecil di sandaran tangan kursi baris kedua untuk kontrol kursi.\n"
                   "- **Kursi Pijat:** Kursi baris kedua memiliki fitur pijat, pemanas, pendingin, dan bisa direbahkan hampir rata.\n"
                   "- **Kulkas:** Dilengkapi kulkas sungguhan yang bisa mendinginkan minuman hingga suhu yang sangat rendah."
    },
    {
        "tag": "denza_teknologi_e_platform",
        "pola": ["mesin denza", "baterai denza", "jarak tempuh denza", "denza ev", "denza d9 hybrid"],
        "jawaban": "Denza D9 hadir dengan teknologi tercanggih dari BYD:\n\n"
                   "- **Versi EV:** Menggunakan e-platform 3.0 dengan Blade Battery yang sangat aman, jarak tempuhnya bisa tembus **600+ km**.\n"
                   "- **Versi DM-i (Hybrid):** Menggunakan sistem Plug-in Hybrid yang sangat irit dan bisa menempuh jarak total lebih dari 1.000 km jika baterai dan bensin penuh."
    },
    {
        "tag": "denza_pajak",
        "pola": ["pajak denza", "stnk denza", "biaya pajak tahunan denza d9"],
        "jawaban": "Untuk varian Denza D9 Full Elektrik (EV):\n\n"
                   "- **Pajak Tahunan:** Sangat murah (di bawah Rp 1 juta) karena mendapatkan insentif mobil listrik murni.\n"
                   "- **Bebas Ganjil Genap:** Meski bodinya sebesar Alphard, mobil ini bebas melenggang di jalanan protokol Jakarta kapan saja!"
    },
    {
        "tag": "wuling_umum",
        "pola": ["wuling", "wuling indonesia", "air ev", "binguo", "cloud ev", "alvez", "almaz", "mobil listrik wuling"],
        "jawaban": "Wuling adalah pelopor mobil listrik (EV) terjangkau di Indonesia yang memiliki ekosistem servis sangat luas. 🔌🇮🇩\n\n"
                   "- **Model EV:** Air EV (Compact), Binguo EV (Hatchback Retro), dan Cloud EV (Medium Hatchback).\n"
                   "- **Model Bensin:** Almaz (SUV Turbo/Hybrid) dan Alvez (Compact SUV).\n"
                   "- **Kelebihan:** Harga sangat kompetitif, fitur teknologi melimpah (WIND), dan biaya operasional yang sangat rendah."
    },
    {
        "tag": "wuling_air_ev",
        "pola": ["air ev", "wuling kecil", "kelebihan air ev", "jarak tempuh air ev", "cas air ev"],
        "jawaban": "Wuling Air EV adalah mobil listrik paling praktis untuk penggunaan kota besar: \n\n"
                   "- **Dimensi:** Mungil, sangat mudah parkir dan selap-selip di gang sempit.\n"
                   "- **Jarak Tempuh:** Tipe Standard Range (200 km) dan Long Range (300 km).\n"
                   "- **Easy Charging:** Bisa dicas langsung di rumah dengan daya minimal 2.200 VA saja (pakai colokan kaki tiga biasa)."
    },
    {
        "tag": "wuling_binguo_cloud",
        "pola": ["binguo ev", "cloud ev", "beda binguo dan cloud", "wuling binguo", "wuling cloud"],
        "jawaban": "Dua jagoan baru Wuling untuk kenyamanan ekstra:\n\n"
                   "- **Binguo EV:** Desain ikonik ala Eropa klasik (retro) dengan jarak tempuh hingga 410 km.\n"
                   "- **Cloud EV:** Fokus pada kenyamanan maksimal dengan kursi *Sofa Mode* yang bisa direbahkan hingga 135 derajat dan kabin yang jauh lebih lega."
    },
    {
        "tag": "wuling_wind",
        "pola": ["wind", "halo wuling", "perintah suara", "fitur wuling", "buka jendela pakai suara"],
        "jawaban": "Fitur andalan Wuling adalah **WIND (Wuling Indonesian Command)**: \n\n"
                   "- **Bahasa Indonesia:** Kamu bisa mengontrol fitur mobil lewat suara dalam Bahasa Indonesia. Contoh: 'Halo Wuling, buka jendela' atau 'Halo Wuling, nyalakan AC'.\n"
                   "- **Fungsional:** Memudahkan pengemudi agar tetap fokus ke jalan tanpa harus memegang tombol."
    },
    {
        "tag": "wuling_almaz_hybrid",
        "pola": ["almaz hybrid", "almaz rs", "mesin almaz", "kelebihan almaz", "suv wuling"],
        "jawaban": "Wuling Almaz adalah SUV canggih dengan fitur ADAS lengkap:\n\n"
                   "- **Almaz Hybrid:** Menggabungkan mesin bensin dan motor listrik untuk performa kencang tapi tetap irit.\n"
                   "- **Fitur:** Layar *head unit* vertikal raksasa, *panoramic sunroof*, dan sistem keamanan aktif (ngerem sendiri kalau ada bahaya)."
    },
    {
        "tag": "wuling_pajak",
        "pola": ["pajak wuling", "stnk air ev", "pajak binguo", "biaya pajak tahunan wuling"],
        "jawaban": "Untuk varian mobil listrik (Air EV, Binguo, Cloud):\n\n"
                   "- **Pajak Tahunan:** Sangat murah, berkisar antara **Rp 300 ribu - Rp 800 ribuan** saja.\n"
                   "- **Insentif:** Mendapatkan potongan PPN dari 11% menjadi hanya 1% (untuk unit yang sudah CKD/rakitan lokal)."
    },
    
]