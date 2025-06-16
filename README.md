# GrooveUp
# 🎵 Hand Gesture Music Controller

Control your music player using only your hand gestures via your webcam.  
Built with Python, OpenCV, and Pygame, using real-time hand detection with [cvzone](https://github.com/cvzone/cvzone).

---

## ✋ How It Works

The system uses your webcam to detect how many fingers you're holding up, and maps each gesture to a music control action.

| Gesture           | Action           |
|-------------------|------------------|
| 0 fingers ✊      | Volume Down      |
| 1 finger ☝️       | Play             |
| 2 fingers ✌️      | Pause            |
| 3 fingers 🤟      | Next Song        |
| 4 fingers 🖖     | Previous Song    |
| 5 fingers 🖐️     | Volume Up        |

---

## 📦 Requirements

- Python 3.7+
- Webcam

### Python libraries:

```bash
pip install opencv-python cvzone pygame
