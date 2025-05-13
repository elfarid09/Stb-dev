import pyautogui as pag
import time
import pyperclip

# List aksi klik otomatis
actions = [
    (109, 451, 2),  # install
    (589, 495, 2),  # install again
    (722, 429, 1),  # ok
    (708, 22, 7),   # 3 bars
    (83, 170, 2),   # security
    (465, 68, 2),   # enable
    (798, 386, 2),  # scroll bar
    (415, 224, 2),  # set pass
    (291, 250, 2),  # first fill
    (310, 338, 2),  # second fill
    (631, 427, 2),  # ok
    (95, 22, 2),    # change tab
    (165, 168, 2),  # right click (field 1)
    (199, 178, 2),  # select all
    (138, 167, 2),  # right click (field 2)
    (163, 182, 2)   # copy
]

# Tunggu sebelum mulai, beri waktu user pindah ke RustDesk
print("[*] Menunggu 3 detik sebelum mulai...")
time.sleep(3)

# Jalankan klik otomatis
for x, y, duration in actions:
    if (x, y) in [(165, 168), (138, 167)]:
        pag.rightClick(x, y, duration=duration)
    else:
        pag.click(x, y, duration=duration)

    if (x, y) in [(291, 250), (310, 338)]:
        # Isi password
        text_to_type = "Safelfar1"
        pag.keyDown('D')
        pag.typewrite(text_to_type)

# Fungsi untuk menyimpan echo ke .bat file
def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}\n')

# Ambil ID dari clipboard dan simpan ke batch
def run_rustdesk_command():
    print("[*] Menunggu clipboard ID dari RustDesk...")
    max_attempts = 20
    attempt = 0
    clipboard_text = ''

    while not clipboard_text.strip() and attempt < max_attempts:
        clipboard_text = pyperclip.paste()
        attempt += 1
        print(f"    Percobaan ke-{attempt} membaca clipboard...")
        time.sleep(1)

    if clipboard_text.strip():
        print(f"[+] RustDesk ID ditemukan: {clipboard_text}")
        save_echo_to_batch('show.bat', f'RustDesk ID: {clipboard_text}')
        save_echo_to_batch('show.bat', 'Password : Safelfar1')
    else:
        print("[!] Gagal mengambil ID dari clipboard.")

# Eksekusi
if __name__ == "__main__":
    run_rustdesk_command()

print("[✓] Selesai. Login credentials disimpan di show.bat.")
