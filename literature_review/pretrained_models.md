# List of Pre-trained Model Candidates for Fine-Tuning

This document contains a list of pre-trained models that have the potential to be fine-tuned on multimodal emotion classification tasks.

---

### Modalitas Visual (Video/Gambar)

| Nama Model          | Fitur Utama                                      | Tautan (Paper/Hugging Face)      | Catatan                                      |
| ------------------- | ------------------------------------------------ | -------------------------------- | -------------------------------------------- |
| **Timesformer** | Arsitektur Transformer, bagus untuk relasi waktu | [Link ke paper/model]            | SOTA untuk klasifikasi video. Mungkin berat. |
| **Vision Transformer (ViT)** | Populer untuk gambar, bisa diadaptasi ke video | [Link ke paper/model]            |                                              |
| *[Nama Model Lain]* |                                                  |                                  |                                              |


---

### Modalitas Audio (Suara)

| Nama Model          | Fitur Utama                                         | Tautan (Paper/Hugging Face) | Catatan                                                     |
| ------------------- | --------------------------------------------------- | --------------------------- | ----------------------------------------------------------- |
| **Wav2Vec 2.0** | Belajar dari audio mentah (*raw*), sangat *powerful*. | [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) | **Pilihan Utama.** Model ini adalah standar industri untuk berbagai tugas audio. Tidak perlu mengubah audio menjadi gambar spektrogram. Sangat cocok untuk menangkap nuansa intonasi dan gaya bicara. |
| **HuBERT** | Mirip Wav2Vec 2.0, performa sangat kompetitif.      | [facebook/hubert-large-ls960-ft](https://huggingface.co/facebook/hubert-large-ls960-ft) | **Alternatif Kuat.** Jika karena suatu alasan Wav2Vec 2.0 sulit diimplementasikan, HuBERT adalah pilihan kedua yang sepadan. |
| *[Nama Model Lain]* |                                                     |                             |                                                             |


---

### Modalitas Teks (dari Transkrip Audio)

| Nama Model          | Fitur Utama                                       | Tautan (Paper/Hugging Face) | Catatan                                      |
| ------------------- | ------------------------------------------------- | --------------------------- | -------------------------------------------- |
| **IndoBERT** | Dibuat khusus untuk Bahasa Indonesia              | [indobenchmark/indobert-base-p1](https://huggingface.co/indobenchmark/indobert-base-p1) | Pilihan utama jika transkrip audio berbahasa Indonesia. |
| **BERT-base-multilingual** | Mendukung banyak bahasa, termasuk Indonesia | [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) | Alternatif jika ada bahasa campuran.         |
| *[Nama Model Lain]* |                                                   |                             |                                              |

---
