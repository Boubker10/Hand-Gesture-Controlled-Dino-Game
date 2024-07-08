# Hand Gesture Controlled Dino Game

## Overview

This project demonstrates a real-time hand gesture recognition system to control the Dino game in Google Chrome using a webcam, OpenCV for computer vision tasks, and pyautogui for simulating keyboard actions. The main objective is to detect hand movements and gestures to make the Dino jump, providing an engaging and interactive way to play the game.



![capture](https://github.com/Boubker10/Hand-Gesture-Controlled-Dino-Game/assets/116897761/5c91ca92-2a73-40b3-a933-9d6cd60f7426)


https://github.com/Boubker10/Hand-Gesture-Controlled-Dino-Game/assets/116897761/0eb3e948-990e-405b-a63e-6b6ea15760e5



## Features

- **Real-time Hand Detection**: Utilizes OpenCV to capture video from the webcam and process the frames to detect hand gestures.
- **Simulated Keyboard Input**: Employs pyautogui to simulate keyboard inputs, enabling the Dino to jump when a specific gesture is detected.
- **Real-time Feedback**: Displays processed video frames with detected contours and convex hulls, providing visual feedback of the detection process.

## How It Works

1. **Capture Video**: The system captures video frames from the webcam.
2. **Pre-process Frames**: Converts the frames to HSV color space and applies a skin color mask to isolate hands.
3. **Find Contours**: Detects contours in the binary mask of the hand.
4. **Analyze Gestures**: Computes the convex hull and convexity defects of the largest contour to recognize hand gestures.
5. **Simulate Actions**: Triggers a keyboard event (e.g., pressing the space bar) when the gesture conditions are met, making the Dino jump in the game.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Boubker10/Hand-Gesture-Controlled-Dino-Game.git
    ```

2. **Create and Activate Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python dino.py
    ```

## Dependencies

- OpenCV
- numpy
- pyautogui
- math

## Usage

1. Ensure your webcam is properly connected and recognized by your computer.
2. Open Google Chrome and navigate to the Dino game (turn off your internet connection to access the game).
3. Run the application using the provided script.
4. Use hand gestures in front of the webcam to make the Dino jump.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
