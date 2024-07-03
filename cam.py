import cv2
import numpy as np

# Ouvrir le flux vidéo depuis la caméra par défaut (généralement la caméra intégrée de l'ordinateur)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra")
    exit()

while True:
    # Lire une image de la caméra
    ret, frame = cap.read()
    
    if not ret:
        print("Erreur: Impossible de lire l'image de la caméra")
        break
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Trouver les bords avec Canny
    edged = cv2.Canny(gray, 30, 200)
    
    # Trouver les contours
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Dessiner tous les contours sur l'image originale
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    
    # Afficher les résultats
    cv2.imshow('Canny Edges After Contouring', edged)
    cv2.imshow('Contours', frame)
    
    # Attendre 1 milliseconde et vérifier si l'utilisateur appuie sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
