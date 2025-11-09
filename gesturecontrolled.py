import cv2
import mediapipe as mp
import time
import numpy as NotImplemented

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

filters = [
    None,
    'GRAYSCALE',
    'SEPIA',
    'NEGATIVE',
    'BLUR'
]
current_filter = 0
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not acces the webcam.")
    exit()



last_action_time = 0
debounce_time = 1
def apply_filter(frame, filter_type):
    if filter_type =='GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'SEPTA':
        sepia_filter = np.array([[0.272, 0.53, 0.31],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, sepia_filter)
        sepia_frame = np.clip(sepia_frame, 0, 255)
        return sepia_frame.astype(np.unit8)
    elif filter_type == 'NEGATIVE':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame
while True:
    sucess, img = cap.read()
    if not success:
        print("Failed to read frame from webcam.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[mp_hands.Handlandmark.THUMb_tip]
            index_tip = hand_landmarks.landmark[mp_hands.Handlandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.Handlandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.Handlandmark.RING_FINGER_TIP]
            pinky_ip = hand_landmarks.landmark[mp_hands.Handlandmark.PINKY_FINGER_TIP]

            frame_height, frame_width, _=img.shape

            thumb_x, thumb_y = int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)
            index_x, index_y = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
            middle_x, middle_y = int(middle_tip.x * frame_width), int(middle_tip.y * frame_height)
            ring_x, ring_y = int(ring_tip.x * frame_width), int(ring_tip.y * frame_height)
            pinky_x, pinky_y = int(pinky_tip.x * frame_width), int(pinky_tip.y * frame_height)

            cv2.circle(img, (thumb_x, thumb_y), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (middle_x, middle_y), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)




            
            
            
            
            


            

         
            