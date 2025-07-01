# 🕵️ Image Steganography App

A Python-based desktop application that allows you to securely hide (and retrieve) text messages inside images using **Least Significant Bit (LSB) encoding**, with optional AES encryption for added privacy.

---

## ✨ Features

- ✅ Hide text inside images
- ✅ Retrieve hidden text from images
- 🔐 Optional AES encryption and decryption using `cryptography`
- 🖼️ Supports `.png`, `.jpeg`, `.jpg` images
- 🖱️ User-friendly GUI built with Tkinter

---

## 🧠 How It Works

The app uses **LSB steganography** to alter the last bit of each RGB pixel component in the image. This slight modification allows the image to retain its original appearance while secretly storing a message.

If encryption is enabled, the message is **encrypted using AES (Fernet)** before being embedded into the image. During decoding, the user is prompted for the decryption key to view the original message.

---

## 🗂️ Project Structure

