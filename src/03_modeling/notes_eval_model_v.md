# 🔬 Log Eksperimen: v3 - Baseline + Augmentasi RAVDESS

> Dokumen ini mencatat hipotesis, hasil, dan pembelajaran dari eksperimen versi 3.

---

### **Ringkasan Eksperimen**

| Kategori | Deskripsi |
| :--- | :--- |
| **🎯 Hipotesis** | Menambahkan data eksternal dari RAVDESS untuk menyeimbangkan distribusi kelas akan meningkatkan F1 Macro Score secara signifikan. |
| **🧠 Model** | `facebook/wav2vec2-base` |
| **💾 Dataset** | `datatrain_augmented.csv` (Data BDC + RAVDESS) |
| **🔧 Perubahan Kunci** | Augmentasi data untuk mengatasi *imbalance*. |
| **STATUS** | **(Gagal)** |

---

### **📊 Hasil Kunci**

| Metrik | Skor | Observasi Penting |
| :--- | :--- | :--- |
| **F1 Macro Score** | **~0.03** | Skor anjlok drastis. |
| **Perilaku Model** | **Mode Collapse** | Model menjadi "malas" dan cenderung menebak hampir semua input sebagai `Sadness`. |

---

### **💡 Analisis & Pembelajaran**

1.  **Kesalahan Kritis pada Labeling 😵**
    * Ditemukan bahwa pemetaan `label2id` pada semua eksperimen sebelumnya (v1, v2, awal v3) dibuat secara dinamis dan **tidak sesuai dengan aturan lomba**. Ini membuat semua metrik F1 sebelumnya tidak valid. Kesalahan ini telah diperbaiki secara permanen di akhir notebook v3.

2.  **Filtering RAVDESS Kurang Teliti 🔍**
    * Disadari bahwa proses filtering data RAVDESS hanya berdasarkan emosi. **Kesalahan:** Belum memfilter berdasarkan **modalitas (`03 = audio-only`)** dan **kanal vokal (`01 = speech`)**, yang berpotensi memasukkan data "noise" (seperti lagu atau data yang tidak relevan) ke dalam set pelatihan.

---

### **🚀 Langkah Selanjutnya (Rencana untuk v4)**

* **[Prioritas Utama]** Memperbaiki *data pipeline* untuk memfilter RAVDESS dengan benar (berdasarkan modalitas & kanal vokal).
* Melatih ulang model *baseline* di atas dataset *augmented* yang kualitasnya sudah ditingkatkan.
* Mulai eksperimen *hyperparameter tuning* (contoh: `learning_rate` yang lebih rendah untuk mencegah *mode collapse*).
