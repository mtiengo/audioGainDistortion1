import numpy as np
import soundfile as sf
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import ttk
import pygame
import io  # For in-memory file handling

def add_distortion_in_memory(input_file, threshold=0.3, gain=1.5, harshness=2.0):
    # Read the audio file
    audio_data, sample_rate = sf.read(input_file)

    # Adjust the threshold based on the harshness
    effective_threshold = threshold / harshness

    # Apply distortion: clip the audio signal based on the adjusted threshold
    distorted_audio = np.clip(audio_data, -effective_threshold, effective_threshold)

    # Apply gain to amplify the distorted signal
    distorted_audio *= gain * harshness

    # Ensure audio is within the acceptable range [-1, 1]
    distorted_audio = np.clip(distorted_audio, -1, 1)

    # Save to an in-memory buffer
    buffer = io.BytesIO()
    sf.write(buffer, distorted_audio, sample_rate, format='WAV')
    buffer.seek(0)  # Reset buffer to the beginning for playback

    return buffer

def process_audio(input_file):
    threshold = threshold_slider.get()
    gain = gain_slider.get()
    harshness = harshness_slider.get()
    
    output_file = filedialog.asksaveasfilename(defaultextension=".wav", 
        filetypes=[("WAV files", "*.wav")])
    if output_file:
        add_distortion(input_file, output_file, threshold, gain, harshness)
        messagebox.showinfo("Success", f"Distortion applied! File saved as: {output_file}")

def load_file():
    global input_file
    input_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if input_file:
        file_label.config(text=f"{input_file} loaded. Adjust parameters and confirm.")

def play_audio_with_effects():
    if not input_file:
        messagebox.showwarning("Warning", "No audio file loaded.")
        return

    # Get current parameter values
    threshold = threshold_slider.get()
    gain = gain_slider.get()
    harshness = harshness_slider.get()

    # Process audio with current parameters
    try:
        buffer = add_distortion_in_memory(input_file, threshold, gain, harshness)
        pygame.mixer.init()
        pygame.mixer.music.load(buffer, 'wav')
        pygame.mixer.music.play()
        messagebox.showinfo("Playback", "Playing distorted audio. Close this dialog to stop playback.")
        pygame.mixer.music.stop()
    except Exception as e:
        messagebox.showerror("Error", f"Audio playback failed: {e}")

def on_drop(event):
    global input_file
    input_file = event.data.strip("{}")
    file_label.config(text=f"{input_file} loaded. Adjust parameters and confirm.")

# Create the main window
root = TkinterDnD.Tk()
root.title("Audio Gain & Distortion Application")

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

file_label = tk.Label(root, text="Drag and drop an audio file here or click to load")
file_label.pack(pady=10)

load_button = tk.Button(root, text="Load Audio File", command=load_file)
load_button.pack(pady=10)

play_button = tk.Button(root, text="Preview Audio with Effects", command=play_audio_with_effects)
play_button.pack(pady=10)

threshold_label = tk.Label(root, text="Threshold:")
threshold_label.pack(pady=5)
threshold_slider = tk.Scale(root, from_=0.1, to=1.0, resolution=0.01, orient='horizontal')
threshold_slider.pack(pady=5)
threshold_slider.set(0.3)

gain_label = tk.Label(root, text="Gain:")
gain_label.pack(pady=5)
gain_slider = tk.Scale(root, from_=1.0, to=15.0, resolution=0.1, orient='horizontal')
gain_slider.pack(pady=5)
gain_slider.set(1.5)

harshness_label = tk.Label(root, text="Harshness:")
harshness_label.pack(pady=5)
harshness_slider = tk.Scale(root, from_=1.0, to=20.0, resolution=0.1, orient='horizontal')
harshness_slider.pack(pady=5)
harshness_slider.set(2.0)

confirm_button = tk.Button(root, text="Confirm & Export", command=lambda: process_audio(input_file))
confirm_button.pack(pady=10)

root.mainloop()
