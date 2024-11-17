# Hand Gesture Controlled Mouse

This project was built during the COVID-19 period and was initially developed to explore hand gesture recognition for controlling a computer mouse. The project uses a webcam to capture hand movements, processes the data using `mediapipe`, and simulates mouse movements and clicks using `pyautogui`. I found the project on my computer and decided to upload it now for public access.

## Features

- **Hand Gesture Detection**: Uses `mediapipe` to detect hand landmarks and track the position of the hand.
- **Mouse Control**: The cursor moves based on the position of the hand and performs a click when the appropriate gesture is made.
- **Smooth Movement**: Implements smoothing of the cursor's movement for more precise control.
- **Left Hand Detection**: The system works only with the left hand.

