import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog

# Declare global variables
img = None
password = ""
msg = ""
c = {}

def encrypt_image():
    global img, msg, password
    msg = entry_message.get()
    password = entry_password.get()

    d = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")

def decrypt_image():
    global img, msg, password, c
    message = ""
    n = 0
    m = 0
    z = 0

    pas = entry_decrypt_password.get()
    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        label_decryption_message.config(text="Decryption message: " + message)
    else:
        label_decryption_message.config(text="Key not valid")

def browse_image():
    global img
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)

# Create main window
root = tk.Tk()
root.title("Image Encryption and Decryption")

# Widgets
label_message = tk.Label(root, text="Enter secret message:")
entry_message = tk.Entry(root)
-
label_password = tk.Label(root, text="Enter a passcode:")
entry_password = tk.Entry(root, show="*")

button_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_image)

label_decrypt_password = tk.Label(root, text="Enter passcode for Decryption:")
entry_decrypt_password = tk.Entry(root, show="*")

button_decrypt = tk.Button(root, text="Decrypt Image", command=decrypt_image)

button_browse = tk.Button(root, text="Browse Image", command=browse_image)

label_decryption_message = tk.Label(root, text="Decryption message:")

# Layout
label_message.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_message.grid(row=0, column=1, padx=10, pady=5)

label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_encrypt.grid(row=2, column=0, columnspan=2, pady=10)

label_decrypt_password.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_decrypt_password.grid(row=3, column=1, padx=10, pady=5)

button_decrypt.grid(row=4, column=0, columnspan=2, pady=10)

button_browse.grid(row=5, column=0, columnspan=2, pady=10)

label_decryption_message.grid(row=6, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()