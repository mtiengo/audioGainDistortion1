# Audio Gain & Distortion Application

This application allows users to apply distortion effects to audio files through a simple and intuitive interface. Users can adjust parameters such as threshold, gain, and harshness using sliders and process audio files with a click of a button.

## Features

- Drag and drop support for audio file loading.
- Adjustable parameters:
  - **Threshold**: Controls the clipping level for distortion.
  - **Gain**: Amplifies the audio signal.
  - **Harshness**: Adjusts the distortion effect's intensity.
- Save the processed audio as a new WAV file.
- Simple and user-friendly interface built with Tkinter.
- Preview audio with added effects

## Requirements

- Python 3.9 or higher
- Required libraries:
  - NumPy
  - SoundFile
  - Tkinter
  - tkinterdnd2
  - pygame

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/audio-distortion-app.git
   cd audio-distortion-app
2. Install the required packages:
   pip install numpy soundfile tkinterdnd2 pygame

## Usage

1. Run the application
2. Load an audio file by dragging and dropping it into the application window or using the "Load Audio File" button.
3. Adjust the parameters (Threshold, Gain, Harshness) using the sliders.
4. Click "Preview Audio With Effects" to preview the file with added effects.
5. Click the "Confirm & Export" button to export the audio file.
6. Choose a location to save the processed file.

## License

This project is licensed under the UnLicense. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## Acknowledgments

- NumPy - For numerical operations.
- SoundFile - For audio file reading and writing.
- Tkinter - For GUI development.
- tkinterdnd2 - For drag-and-drop functionality.
- pygame - For sound playback
