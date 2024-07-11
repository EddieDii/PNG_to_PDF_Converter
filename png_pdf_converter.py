import os
import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
from PIL import Image

class PngtoPdfConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG to PDF Converter")
        self.create_widgets()
    
    def create_widgets(self):
        self.select_file_button = tk.Button(self.root, text="Select PNG File", command=self.select_file,padx=20, pady=10)
        self.select_file_button.pack(pady=20)

        self.file_listbox = Listbox(self.root, width=50, height=10)
        self.file_listbox.pack(pady=20)

        self.convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf,padx=20, pady=10)
        self.convert_button.pack(pady=20)
    
    def select_file(self):
        self.png_files = filedialog.askopenfilenames(filetypes=[("PNG files", "*.png")])
        if self.png_files:
            self.file_listbox.delete(0, tk.END)
            for file in self.png_files:
                self.file_listbox.insert(tk.END, file.split('/')[-1])

    def convert_to_pdf(self):
        if not hasattr(self, "png_files") or not self.png_files:
            messagebox.showerror("Error", "No PNG files selected.")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not output_file:
            return
        
        try:
            image_list = []
            for png_file in self.png_files:
                image = Image.open(png_file).convert('RGB')
                image_list.append(image)
            
            if image_list:
                image_list[0].save(output_file, save_all=True, append_images=image_list[1:])
                messagebox.showinfo("Success", "PDF file created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error converting to PDF: {str(e)}")

def main():
    root = tk.Tk()
    app = PngtoPdfConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()