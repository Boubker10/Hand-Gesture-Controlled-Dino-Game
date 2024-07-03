import cv2
import mediapipe as mp
import pyautogui


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


def control_dino(hand_landmarks):
    for hand_landmark in hand_landmarks:
        for id, lm in enumerate(hand_landmark.landmark):
       
            if id == 8:
                if lm.y < 0.5:
                    pyautogui.press('space')
                    return

# Capture vidéo
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erreur: Impossible de lire l'image de la caméra")
        break
    
    frame = cv2.flip(frame, 1)  
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            control_dino(results.multi_hand_landmarks)
    
    cv2.imshow('Hand Detection', image)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
