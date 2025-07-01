
import tkinter as tk
from tkinter import filedialog, messagebox
from steganography import encode_image, decode_image
from crypto_utils import generate_key, encrypt_text, decrypt_text

class StegoApp:
    def __init__(self, root):
        self.root = root
        root.title("Image Steganography App")

        self.file_path = None
        self.key = None

        # Input file
        self.choose_button = tk.Button(root, text="Choose Image", command=self.load_image)
        self.choose_button.pack()

        # Text to encode
        self.text_box = tk.Text(root, height=5)
        self.text_box.pack()

        # Encrypt checkbox
        self.encrypt_var = tk.IntVar()
        self.encrypt_check = tk.Checkbutton(root, text="Encrypt Message", variable=self.encrypt_var)
        self.encrypt_check.pack()

        # Save path
        self.output_button = tk.Button(root, text="Save Encoded Image", command=self.encode_image)
        self.output_button.pack()

        # Decode button
        self.decode_button = tk.Button(root, text="Decode Message", command=self.decode_image)
        self.decode_button.pack()

    def load_image(self):
        self.file_path = filedialog.askopenfilename()

    def encode_image(self):
        text = self.text_box.get("1.0", tk.END).strip()
        if self.encrypt_var.get():
            self.key = generate_key()
            text = encrypt_text(text, self.key).decode()
            messagebox.showinfo("Key", f"Save this key to decrypt:\n\n{self.key.decode()}")

        output_path = filedialog.asksaveasfilename(defaultextension=".png")
        if encode_image(self.file_path, text, output_path):
            messagebox.showinfo("Success", "Message encoded and image saved.")

    def decode_image(self):
        decoded = decode_image(self.file_path)
        if decoded.startswith("gAAAA"):  # Fernet signature
            key = tk.simpledialog.askstring("Key Needed", "Enter the decryption key:")
            try:
                decoded = decrypt_text(decoded.encode(), key.encode())
            except Exception:
                messagebox.showerror("Error", "Invalid decryption key.")
                return
        messagebox.showinfo("Decoded Message", decoded)