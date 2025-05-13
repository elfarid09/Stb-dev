import pyautogui as pag
import time
import pyperclip

# Langkah klik otomatis
actions = [
    (109, 451, 2),  # install
    (589, 495, 2),  # install again
    (722, 429, 1),  # ok
    (708, 22, 7),   # 3 bars
    (83, 170, 2),   # secu
    (465, 68, 2),   # enable
    (798, 386, 2),  # scroll bar
    (415, 224, 2),  # set pass
    (291, 250, 2),  # first fill
    (310, 338, 2),  # second fill
    (631, 427, 2),  # ok
    (95, 22, 2),    # change tab
    (165, 168, 2),  # rightclick
    (199, 178, 2),  # select all
    (138, 167, 2),  # right click
    (163, 182 ,2)   # copy
]

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'\necho {echo_text}\n')

def run_rustdesk_command():
    print("[*] Menunggu clipboard ID dari RustDesk...")
    for i in range(20):
        clipboard_text = pyperclip.paste().strip()
        print(f"    Percobaan ke-{i+1} membaca clipboard...")
        if clipboard_text and clipboard_text.replace(".", "").isdigit():
            break
        time.sleep(1)
    else:
        print("[!] Gagal mengambil ID dari clipboard.")
        clipboard_text = "UNKNOWN"

    save_echo_to_batch('show.bat', f'RustDesk ID: {clipboard_text}')
    save_echo_to_batch('show.bat', 'Password : Safelfar1')

# Delay awal untuk kasih waktu buka program target
print("[*] Menunggu 3 detik sebelum mulai...")
time.sleep(3)

# Jalankan aksi klik otomatis
for x, y, duration in actions:
    if (x, y) in [(165, 168), (138, 167)]:
        pag.rightClick(x, y, duration=duration)
    else:
        pag.click(x, y, duration=duration)
    if (x, y) in [(291, 250), (310, 338)]:
        pag.keyDown('D')  # biar huruf pertama besar
        pag.typewrite("Safelfar1")

# Tunggu RustDesk menampilkan ID
time.sleep(3)
run_rustdesk_command()

print("[✓] Selesai. Login credentials disimpan di show.bat.")
