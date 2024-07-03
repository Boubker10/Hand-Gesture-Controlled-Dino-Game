import cv2
import numpy as np
import math
import pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils


def control_dino(hand_landmarks, frame):
    for hand_landmark in hand_landmarks:
        for id, lm in enumerate(hand_landmark.landmark):
            if id == 8:
                if lm.y < 0.5:
                    pyautogui.press('space')
                    return
    

    skin_mask = detect_skin(frame)
    blurred = cv2.GaussianBlur(skin_mask, (5, 5), 0)
    contours, hierarchy = cv2.findContours(blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    try:
        contour = max(contours, key=lambda x: cv2.contourArea(x))
        
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
        hull = cv2.convexHull(contour)
        
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
        cv2.drawContours(frame, [hull], -1, (0, 0, 255), 2)

        hull = cv2.convexHull(contour, returnPoints=False)
        defects = cv2.convexityDefects(contour, hull)
    
        count_defects = 0
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])
                
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                
                angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
            
                if angle <= 90:
                    count_defects += 1
                    cv2.circle(frame, far, 1, [0, 0, 255], -1)
                    cv2.line(frame, start, end, [0, 255, 0], 2)
            
            if count_defects >= 4:
                pyautogui.press('space')
                cv2.putText(frame, "JUMP", (115, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    except ValueError:
        print("Aucun contour trouvé")


def detect_skin(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    return mask


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
        control_dino(results.multi_hand_landmarks, frame)
    
    cv2.imshow('Hand Detection', image)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
