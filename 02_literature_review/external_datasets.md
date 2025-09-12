# External Dataset Candidate List

This document contains a list of public datasets that could potentially be used to augment and balance the BDC 2025 training data.

---

### Dataset #1: RAVDESS (Ryerson Audio-Visual Database of Emotional Speech and Song)

* **Tautan:** [https://zenodo.org/records/1188976](https://zenodo.org/records/1188976)
* **Modalitas:** Video, Audio.
* **Label Emosi Asli:** Neutral, Calm, Happy, Sad, Angry, Fearful, Disgust, Surprised.
* **Potensi Pemetaan ke 8 Kelas BDC:**
    * `Happy` -> `Joy`
    * `Sad` -> `Sadness`
    * `Angry` -> `Anger`
    * `Fearful` -> `Fear`
    * `Surprised` -> `Surprise`
    * `Neutral` -> `Neutral`
    * *(Label `Calm` dan `Disgust` mungkin tidak bisa dipetakan ke 8 kelas utama kita, jadi bisa diabaikan).*
* **Aksesibilitas:** Sangat mudah. Bisa langsung diunduh dari situs web Zenodo. Ukuran total cukup besar (~24 GB).
* **Catatan/Kelebihan & Kekurangan:**
    * **(+) Kelebihan:** Kualitas audio dan video sangat tinggi dan bersih. Direkam di lingkungan studio. Ada 24 aktor profesional (12 pria, 12 wanita) sehingga datanya beragam dari sisi subjek. Label emosinya sangat jelas.
    * **(-) Kekurangan:** Emosi yang ditampilkan adalah hasil akting (acted emotions). Ekspresinya cenderung teatrikal dan lebih jelas dibandingkan emosi natural di video media sosial. Ini bisa menjadi bias jika tidak ditangani dengan baik.

---

### Dataset #2: CREMA-D (Crowd-sourced Emotional Multimodal Actors Dataset)

* **Tautan:** [https://github.com/CheyneyComputerScience/CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D)
* **Modalitas:** Video, Audio.
* **Label Emosi Asli:** Happy, Sad, Anger, Fear, Disgust, dan Neutral.
* **Potensi Pemetaan ke 8 Kelas BDC:**
    * `Happy` -> `Joy`
    * `Sad` -> `Sadness`
    * `Anger` -> `Anger`
    * `Fear` -> `Fear`
    * `Neutral` -> `Neutral`
    * *(Dataset ini tidak memiliki kelas `Surprise`, `Proud`, dan `Trust` secara eksplisit).*
* **Aksesibilitas:** Cukup mudah. Biasanya tersedia melalui Kaggle atau repositori GitHub resminya.
* **Catatan/Kelebihan & Kekurangan:**
    * **(+) Kelebihan:** Sangat beragam. Terdiri dari 7,442 klip dari 91 aktor dengan latar belakang etnis yang beragam. Ini sangat bagus untuk generalisasi model.
    * **(-) Kekurangan:** Sama seperti RAVDESS, ini adalah *acted emotions*. Selain itu, cakupan kelas emosinya lebih sedikit, yang berarti kita tidak bisa menambah data untuk semua kelas yang kita butuhkan (terutama `Surprise`).

---

### Dataset #3: IEMOCAP (Interactive Emotional Dyadic Motion Capture database)

* **Tautan:** [https://sail.usc.edu/iemocap/](https://sail.usc.edu/iemocap/)
* **Modalitas:** Video, Audio, Teks (transkrip).
* **Label Emosi Asli:** Anger, Happiness, Sadness, Neutrality, Excitement, Fear, Surprise, Frustration, Disgust, Other.
* **Potensi Pemetaan ke 8 Kelas BDC:**
    * `Happiness` atau `Excitement` -> `Joy`
    * `Sadness` -> `Sadness`
    * `Anger` atau `Frustration` -> `Anger`
    * `Fear` -> `Fear`
    * `Surprise` -> `Surprise`
    * `Neutrality` -> `Neutral`
    * *(`Trust` dan `Proud` masih belum terwakili).*
* **Aksesibilitas:** Lebih sulit. Memerlukan pengisian formulir lisensi dan persetujuan dari pemilik dataset (USC). Prosesnya bisa memakan waktu beberapa hari.
* **Catatan/Kelebihan & Kekurangan:**
    * **(+) Kelebihan:** Dianggap sebagai salah satu dataset "standar emas". Emosinya lebih naturalistik karena direkam dari sesi interaksi antara dua aktor (improvisasi dan skrip), bukan hanya mengucapkan kalimat ke kamera. Sangat kaya karena menyertakan transkrip teks.
    * **(-) Kekurangan:** Proses untuk mendapatkan datanya tidak instan. Labelnya bisa tumpang tindih (misal: `Happiness` dan `Excitement`), sehingga butuh pra-pemrosesan yang lebih hati-hati.

---

### **Discussion and Next**

* **Rekomendasi Awal:** **RAVDESS** adalah kandidat terbaik untuk memulai. Aksesnya paling mudah dan labelnya paling cocok dengan 6 dari 8 kelas kita. Ini bisa menjadi "suntikan data" pertama yang sangat baik untuk menyeimbangkan kelas-kelas minoritas seperti `Fear`, `Sadness`, dan `Neutral`.
* **Strategi Jangka Menengah:** Sambil tim Anda mulai bereksperimen dengan RAVDESS, Anda bisa memulai proses untuk mendapatkan akses ke **IEMOCAP**. Jika berhasil didapat, dataset ini sangat berharga karena sifatnya yang lebih natural dan adanya modalitas teks.
* **Tantangan:** Perhatikan bahwa tidak ada dataset di atas yang secara eksplisit memiliki label untuk **`Proud` (Bangga)** dan **`Trust` (Percaya)**. Ini adalah dua emosi yang lebih kompleks dan kontekstual. Ini menguatkan pentingnya **analisis kualitatif** Anda terhadap data asli dari panitia untuk benar-benar memahami bagaimana kedua emosi ini diekspresikan. Mungkin kita perlu mencari data untuk kedua kelas ini secara spesifik nanti.
