import pandas as pd
import requests
from tqdm.auto import tqdm
import time

# -- Konfigurasi --
input_filename = '/Users/azuka/Documents/BELAJAR/mini-research-bdc2025/01_data_exploration/datatrain_cleaned.csv'
output_filename = '01_data_exploration/datatrain_final.csv'
timeout_seconds = 10

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    df = pd.read_csv(input_filename)
    print(f"Berhasil memuat {len(df)} baris dari '{input_filename}'")
except FileNotFoundError:
    print(f"Error: File '{input_filename}' tidak ditemukan.")
    exit()

# -- URL Check --
def is_url_accessible(url):
    try:
        url = str(url).strip()
        # Menggunakan requests.get() dan stream=True sedikit lebih andal untuk beberapa situs
        # dan tetap efisien karena tidak membaca kontennya.
        response = requests.get(url, headers=headers, timeout=timeout_seconds, stream=True)

        if 200 <= response.status_code < 300:
            return True
        else:
            return False
    except requests.RequestException:
        return False

# -- Validation --
def check_with_delay(url):
    result = is_url_accessible(url)
    time.sleep(0.1)
    return result

tqdm.pandas(desc="Mengecek URL")
df['is_accessible'] = df['video'].progress_apply(check_with_delay)
print("Validasi URL selesai.")

# -- Report --
valid_count = df['is_accessible'].sum()
invalid_count = len(df) - valid_count
print("\n--- Report Validation ---")
print(f"Total URL diperiksa: {len(df)}")
print(f"URL yang Valid      : {valid_count}")
print(f"URL yang Tidak Valid: {invalid_count}")
print("------------------------\n")

# -- Save Final Dataset --
df_final = df[df['is_accessible'] == True].copy()
df_final = df_final.drop(columns=['is_accessible'])

df_final.to_csv(output_filename, index=False)
print(f"Dataset final dengan {len(df_final)} baris data valid telah disimpan sebagai '{output_filename}'")
