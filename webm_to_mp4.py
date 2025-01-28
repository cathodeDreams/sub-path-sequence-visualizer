import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
from pathlib import Path

class WebmToMp4Converter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("WEBM to MP4 Converter for X.com")
        self.geometry("600x400")
        self.configure(bg="#f0f0f0")

        style = ttk.Style()
        style.theme_use('clam')

        # Main frame
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="WEBM to MP4 Converter",
            font=('Segoe UI', 16, 'bold')
        )
        title_label.pack(pady=10)

        # Input file selection
        self.input_frame = ttk.LabelFrame(main_frame, text="Input WEBM File", padding="10")
        self.input_frame.pack(fill=tk.X, pady=5)

        self.input_path = tk.StringVar()
        self.input_entry = ttk.Entry(self.input_frame, textvariable=self.input_path)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.browse_btn = ttk.Button(
            self.input_frame,
            text="Browse",
            command=self.browse_input
        )
        self.browse_btn.pack(side=tk.RIGHT)

        # Output directory selection
        self.output_frame = ttk.LabelFrame(main_frame, text="Output Directory", padding="10")
        self.output_frame.pack(fill=tk.X, pady=5)

        self.output_path = tk.StringVar()
        self.output_entry = ttk.Entry(self.output_frame, textvariable=self.output_path)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.output_btn = ttk.Button(
            self.output_frame,
            text="Browse",
            command=self.browse_output
        )
        self.output_btn.pack(side=tk.RIGHT)

        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            main_frame,
            variable=self.progress_var,
            maximum=100
        )
        self.progress.pack(fill=tk.X, pady=20)

        # Convert button
        self.convert_btn = ttk.Button(
            main_frame,
            text="Convert to MP4",
            command=self.convert_video,
            style='Accent.TButton'
        )
        self.convert_btn.pack(pady=10)

        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            font=('Segoe UI', 10)
        )
        self.status_label.pack(pady=5)

    def browse_input(self):
        filename = filedialog.askopenfilename(
            title="Select WEBM file",
            filetypes=[("WEBM files", "*.webm")]
        )
        if filename:
            self.input_path.set(filename)
            # Auto-set output directory to same as input
            self.output_path.set(str(Path(filename).parent))

    def browse_output(self):
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_path.set(directory)

    def convert_video(self):
        input_file = self.input_path.get()
        output_dir = self.output_path.get()

        if not input_file or not output_dir:
            messagebox.showerror("Error", "Please select input file and output directory")
            return

        input_path = Path(input_file)
        output_path = Path(output_dir) / f"{input_path.stem}_x.mp4"

        try:
            self.status_var.set("Converting...")
            self.progress_var.set(0)
            self.update()

            # FFmpeg command optimized for X.com compatibility
            command = [
                'ffmpeg', '-i', str(input_path),
                '-c:v', 'libx264', '-preset', 'slow',
                '-crf', '23',  # High quality, visually lossless
                '-c:a', 'aac', '-b:a', '128k',
                '-movflags', '+faststart',  # Enable streaming
                '-y',  # Overwrite output file if it exists
                str(output_path)
            ]

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            _, stderr = process.communicate()

            if process.returncode == 0:
                self.progress_var.set(100)
                self.status_var.set("Conversion completed successfully!")
                messagebox.showinfo("Success", f"Video converted successfully!\nSaved to: {output_path}")
            else:
                raise subprocess.CalledProcessError(process.returncode, command, stderr)

        except FileNotFoundError:
            messagebox.showerror("Error", "FFmpeg not found. Please install FFmpeg and add it to your system PATH.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Conversion failed")

        self.progress_var.set(0)

if __name__ == "__main__":
    app = WebmToMp4Converter()
    app.mainloop() 