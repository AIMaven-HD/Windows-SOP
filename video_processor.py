import os
import stat
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import messagebox

import imageio_ffmpeg
from tkinterdnd2 import DND_FILES, TkinterDnD


def normalize_dropped_path(path):
    """Normalize drag-and-drop paths across Windows/macOS/Linux Tk variants."""
    cleaned = path.strip()
    if cleaned.startswith("{") and cleaned.endswith("}"):
        cleaned = cleaned[1:-1]
    return os.path.normpath(cleaned)


def resolve_ffmpeg_path():
    """Resolve ffmpeg path for source runs and PyInstaller-frozen builds."""
    if getattr(sys, "frozen", False):
        bundle_dir = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
        bundled_ffmpeg = os.path.join(bundle_dir, "ffmpeg.exe")
        if os.path.exists(bundled_ffmpeg):
            return bundled_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


class VideoProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SOP Video Cutter (720p + 15min)")
        self.root.geometry("600x400")

        try:
            self.ffmpeg_path = resolve_ffmpeg_path()
            if os.name != "nt":
                st = os.stat(self.ffmpeg_path)
                os.chmod(self.ffmpeg_path, st.st_mode | stat.S_IEXEC)
            status_text = "System Ready"
            status_color = "green"
        except Exception as e:
            self.ffmpeg_path = None
            status_text = f"Error: Engine not found ({str(e)})"
            status_color = "red"

        self.label = tk.Label(
            root,
            text="Drag & Drop Video Here\n(Auto-converts to 720p & Splits into 15 min chunks)",
            bg="lightgray",
            font=("Arial", 14),
        )
        self.label.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)
        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind("<<Drop>>", self.drop)

        self.status_label = tk.Label(
            root,
            text=status_text,
            fg=status_color,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def drop(self, event):
        files = [normalize_dropped_path(path) for path in self.root.tk.splitlist(event.data)]
        if not self.ffmpeg_path:
            messagebox.showerror("Error", "Video engine (FFmpeg) not found.")
            return

        threading.Thread(target=self.start_processing, args=(files,), daemon=True).start()

    def start_processing(self, files):
        self.root.after(
            0,
            lambda: self.status_label.config(
                text="Processing... This may take a while. Do not close.", fg="blue"
            ),
        )
        for f in files:
            self.process_video(f)
        self.root.after(0, lambda: self.status_label.config(text="Done! Ready for more.", fg="green"))

    def process_video(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Dropped file was not found: {file_path}")

            directory = os.path.dirname(file_path)
            filename = os.path.basename(file_path)
            name, _ = os.path.splitext(filename)

            output_pattern = os.path.join(directory, f"{name}_part%03d.mp4")

            cmd = [
                self.ffmpeg_path,
                "-y",
                "-i",
                file_path,
                "-vf",
                "scale=-2:720",
                "-c:v",
                "libx264",
                "-preset",
                "fast",
                "-crf",
                "23",
                "-c:a",
                "aac",
                "-f",
                "segment",
                "-segment_time",
                "900",
                "-reset_timestamps",
                "1",
                output_pattern,
            ]

            startupinfo = None
            if os.name == "nt":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            subprocess.run(cmd, check=True, startupinfo=startupinfo)
            self.root.after(0, lambda: messagebox.showinfo("Success", f"Finished: {filename}"))

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Failed: {str(e)}"))


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = VideoProcessorApp(root)
    root.mainloop()
