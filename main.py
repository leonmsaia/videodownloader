import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Style
import threading
from yt_dlp import YoutubeDL

class VideoDownloaderWinamp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader - z1gg1")
        self.root.geometry("600x400")
        self.root.configure(bg="#2b2b2b")
        self.root.resizable(False, False)

        # 🎨 Winamp-style colors
        self.color_bg = "#2b2b2b"
        self.color_fg = "#00ff00"
        self.color_input_bg = "#3c3c3c"
        self.color_input_fg = "#00ff00"
        self.color_button_bg = "#4d4d4d"
        self.color_button_fg = "#00ff00"
        self.progress_color = "#00ff00"

        # 🎛️ ProgressBar style
        style = Style(self.root)
        style.theme_use("clam")
        style.configure("TProgressbar", thickness=20, troughcolor="#1e1e1e", background=self.progress_color)

        # === MAIN CENTERED CONTAINER ===
        self.frame = tk.Frame(self.root, bg=self.color_bg)
        self.frame.pack(expand=True)

        # === VIDEO LINK ===
        self._add_label("Video Link:")
        self.url_entry = self._add_input()
        self._add_help("(Supports YouTube, Vimeo, OK.ru)")

        # === DOWNLOAD FOLDER ===
        self._add_label("Download Folder:")
        self.folder_entry = self._add_input()
        self._add_button("Select Folder", self.select_folder)

        # === PROGRESS BAR ===
        self.progress = Progressbar(self.frame, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
        self.progress.pack(pady=20)

        # === DOWNLOAD BUTTON ===
        self._add_button("Download Video", self.start_download)

        # === CREDITS ===
        tk.Label(self.frame, text="Developed by z1gg1 - enjoy it", fg="#aaaaaa", bg=self.color_bg, font=("Courier", 8)).pack(pady=15)

    def _add_label(self, text):
        tk.Label(self.frame, text=text, fg=self.color_fg, bg=self.color_bg, font=("Courier", 10)).pack(pady=(10, 0))

    def _add_input(self):
        entry = tk.Entry(self.frame, width=60, bg=self.color_input_bg, fg=self.color_input_fg,
                         insertbackground=self.color_input_fg, relief="sunken", bd=2,
                         font=("Courier", 10))
        entry.pack(pady=3)
        return entry

    def _add_button(self, text, command):
        tk.Button(self.frame, text=text, command=command, width=25,
                  bg=self.color_button_bg, fg=self.color_button_fg,
                  activebackground="#5c5c5c", relief="raised", bd=2,
                  font=("Courier", 10, "bold")).pack(pady=5)

    def _add_help(self, text):
        tk.Label(self.frame, text=text, fg="#aaaaaa", bg=self.color_bg, font=("Courier", 8)).pack(pady=(0, 8))

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)

    def update_progress(self, d):
        if d['status'] == 'downloading':
            try:
                downloaded = d.get('downloaded_bytes', 0)
                total = d.get('total_bytes') or d.get('total_bytes_estimate')
                if downloaded and total:
                    percent = downloaded / total * 100
                    self.progress["value"] = percent
                    self.root.update_idletasks()
            except Exception as e:
                print("Progress error:", e)

    def download_video(self):
        url = self.url_entry.get()
        folder = self.folder_entry.get()

        if not url or not folder:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'progress_hooks': [self.update_progress],
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.progress["value"] = 100
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def start_download(self):
        self.progress["value"] = 0
        thread = threading.Thread(target=self.download_video)
        thread.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderWinamp(root)
    root.mainloop()
