# Workflow Proyek Riset (Colab + Lokal)

---

## Skenario 1: Kerja di Google Colab (Coding & Analisis)

### 1. Warming Up
Pastikan Google Drive sinkron dengan GitHub. Jalankan ini di sel paling atas:
```python
# =================================================================
# Warming up + Setup
# =================================================================
from google.colab import drive
import os

drive.mount('/content/drive')

repo_path = '/content/drive/My Drive/mini-research-bdc2025/'
os.chdir(repo_path)
!git pull


# --- UBAH PATH INI SESUAI LOKASI NOTEBOOK ---
notebook_folder = '01_data_exploration/'

working_dir = os.path.join(repo_path, notebook_folder)
os.chdir(working_dir)

print(f"\n✅ Setup Selesai. Anda sekarang bekerja di folder:")
!pwd
```

### 2. Proses Kerja
Ngoding dan analisis seperti biasa. File output (`.csv`, `.png`) akan tersimpan di Google Drive.

### 3. Cooling Down

**A. Simpan Notebook (.ipynb):**
* Gunakan menu: `File` -> `Save a copy in GitHub`.
* Ingat untuk ketik path lengkap di `File path`.

**B. Simpan File Hasil Generate (.csv, .png, dll):**
* Jalankan skrip ini di sel paling bawah untuk upload semua file output.
```python
# Sel Pendinginan
from getpass import getpass
username = "Frynnn-69" # Ganti jika perlu
repository = "mini-research-bdc2025"
personal_access_token = getpass('Masukkan Personal Access Token (PAT) Anda: ')

%cd /content/drive/My Drive/mini-research-bdc2025/
!git add .
!git commit -m "Menambahkan output dari sesi Colab"
remote_url = f"https://{username}:{personal_access_token}@[github.com/](https://github.com/){username}/{repository}.git"
!git push "{remote_url}"
```

---

## Skenario 2: Kerja di Editor Lokal (Menulis .md)

### 1.
```bash
git pull --rebase
```
Lakukan rebase sebelum otak atik-atik file.
