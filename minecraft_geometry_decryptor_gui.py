# Minecraft Geometry Decryptor GUI

import tkinter as tk
from tkinter import filedialog, messagebox
import decryption_logic  # This will be your decryption logic module

class MinecraftGeometryDecryptorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Minecraft Geometry Decryptor")

        self.label = tk.Label(master, text="Select a geometry file to decrypt:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_file)
        self.decrypt_button.pack()

        self.selected_file = None

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(title="Select a file", filetypes=[("Geometry Files", "*.geometry")])

    def decrypt_file(self):
        if not self.selected_file:
            messagebox.showwarning("Warning", "Please select a file first!")
            return
        try:
            decrypted_data = decryption_logic.decrypt(self.selected_file)  # Assume decrypt() is the function used for decryption
            output_file = self.selected_file.replace('.geometry', '_decrypted.geometry')
            with open(output_file, 'w') as f:
                f.write(decrypted_data)
            messagebox.showinfo("Success", f"File decrypted successfully! Saved as: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = MinecraftGeometryDecryptorGUI(root)
    root.mainloop()