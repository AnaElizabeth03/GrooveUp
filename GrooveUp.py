import cv2
from cvzone.HandTrackingModule import HandDetector
import pygame
import os
import time

# Init Pygame and mixer
pygame.init()
pygame.mixer.init()

# Load songs
music_folder = "music"
playlist = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
current_song = 0
volume = 0.5
last_action_time = time.time()
delay = 2

# Init webcam and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
last_gesture = -1

pygame.mixer.music.load(os.path.join(music_folder, playlist[current_song]))
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()

while True:
    success, frame = cap.read()
    hands, frame = detector.findHands(frame)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        gesture = fingers.count(1)
        current_time = time.time()

        if current_time - last_action_time > delay:
            last_action_time = current_time
            last_gesture = gesture

            if gesture == 0:
                volume = max(0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)
                print("Volume Down")
            elif gesture == 1:
                pygame.mixer.music.unpause()
                print("Play")
            elif gesture == 2:
                pygame.mixer.music.pause()
                print("Pause")
            elif gesture == 3:
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music_folder, playlist[current_song]))
                pygame.mixer.music.play()
                print("Next Song")
            elif gesture == 4:
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music_folder, playlist[current_song]))
                pygame.mixer.music.play()
                print("Previous Song")
            elif gesture == 5:
                volume = min(1, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
                print("Volume Up")

    # Instruction overlay
    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (300, 200), (0, 0, 0), -1)
    alpha = 0.5
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    instructions = [
        "0 fingers: Volume Down",
        "1 finger : Play",
        "2 fingers: Pause",
        "3 fingers: Next Song",
        "4 fingers: Previous Song",
        "5 fingers: Volume Up"
    ]

    for i, text in enumerate(instructions):
        y = 40 + i * 25
        cv2.putText(frame, text, (20 + 1, y + 1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.putText(frame, text, (20, y),     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Hand Music Controller", frame)
    if cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
