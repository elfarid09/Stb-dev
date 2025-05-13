import pyautogui as pag
import time
import pyperclip


# Define the coordinates and use the `actions` list
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
    (163, 182, 2)   # copy
]


# Wait for a few seconds to give time to focus on the target application
time.sleep(2)

# Perform the actions in the specified order
for x, y, duration in actions:
    if (x, y) == (165, 168) or (x, y) == (138, 167):
        # For right-click coordinates, perform right-click
        pag.rightClick(x, y, duration=duration)
    else:
        pag.click(x, y, duration=duration)
    if (x, y) in [(291, 250), (310, 338)]:
        # For "first fill" and "second fill" coordinates, type the desired text
        pag.keyDown('D')  # Press the "D" key
        text_to_type = "Safelfar1"
        pag.typewrite(text_to_type)


# Function to save echo to batch file
def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}\n')


# Function to run RustDesk command
def run_rustdesk_command():
    # Wait until clipboard contains the RustDesk ID
    clipboard_text = ''
    while not clipboard_text.strip():  # Keep checking until clipboard is not empty
        clipboard_text = pyperclip.paste()  # Get clipboard text
        time.sleep(0.5)  # Sleep for a short time before checking again

    # Debugging: Print the clipboard text to verify if it is being copied correctly
    print(f"Clipboard contains: {clipboard_text}")

    password_echo = 'Password : Safelfar1'  

    # Save the ID and password to batch file
    save_echo_to_batch('show.bat', f'RustDesk ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)


if __name__ == "__main__":
    run_rustdesk_command()

print("Done, Log in credentials are below")
