# Mr. Incredible Meme Soundboard App
![telegram-cloud-document-2-5404789087259333404](https://github.com/user-attachments/assets/bcbcbc03-0215-473a-8852-eb4b3c7476b1)
This Python-based soundboard application plays different Mr. Incredible meme sounds. It uses Tkinter for the graphical interface and Pygame for audio playback.

## Features

- **Sound Buttons:** 16 unique buttons, each playing a different sound.
- **Background Image:** Attractive UI with a themed background.
- **Interactive UI:** Simple button-based interface for easy interaction.

## Prerequisites

- **Python 3.x**
- Required library:
  ```bash
  pip install pygame
  ```
- **Directory Structure:**
  ```
  project_directory/
  ├─ assets/
  │   ├─ back1.png (Background image)
  │   ├─ button_X.png (Button images for each sound)
  │   └─ sound_X.mp3 (Audio files for each button)
  └─ app.py (Main application file)
  ```

## How to Run

1. Clone or download the repository.
2. Ensure the `assets/` directory contains the required image and audio assets.
3. Run the program:
   ```bash
   python app.py
   ```

## Usage

- Click any of the 16 buttons to play the corresponding sound.
- Ensure your audio system is enabled for proper playback.

## Notes

- Verify image dimensions and file paths if any UI issues occur.
- Ensure all `.mp3` files are present in the `assets/` directory.

