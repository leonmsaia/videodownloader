# 🎶 Winamp-style Video Downloader

A retro-styled GUI application built with Python and `tkinter`, inspired by Winamp aesthetics from the 90s/2000s.  
Download videos from **YouTube**, **Vimeo**, and **OK.ru** in the highest available quality.

---

## 🚀 Features

- 🖼️ Retro UI: Inspired by the original Winamp interface  
- 📥 Video downloading from YouTube, Vimeo, and OK.ru  
- 🎚️ Progress bar to track download status  
- 💾 Folder selector to choose the download location  
- 🔊 Optional retro click sound for buttons  
- 🎨 Custom color and font styling with Courier  
- 🔒 No ads, no tracking, just pure functionality

---

## 🛠 Requirements

- Python 3.8 or newer
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 How to Run (Uncompiled)

```bash
python main.py
```

---

## 🛠 How to Compile into an .EXE (Windows)

```bash
pip install pyinstaller
```

Then run:

```bash
pyinstaller --onefile --windowed main.py ^
  --add-data "click_retro.wav;." ^
  --add-data "background_texture.png;."
```

> Use `:` instead of `;` on Linux/macOS.

---

## 📁 Resource Path Helper (for PyInstaller)

```python
import sys, os
def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
```

---

## 📄 License

MIT License.  
Developed by **z1gg1** with love for retro vibes 💚
