import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui
from config import pTime, wCam, hCam, frameR, smoothening, plocX, plocY, clocX, clocY, wScr, hScr, flag

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.8)
mpDraw = mp.solutions.drawing_utils

while True:
    try:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        for hand in results.multi_handedness:
            handType = hand.classification[0].label
            if handType == "Left":
                lmList = []
                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        for id, lm in enumerate(handLms.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            lmList.append([id, cx, cy])
                        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                    x1 = lmList[8][1]
                    y1 = lmList[8][2]
                    if lmList[8][2] < lmList[4][2] + 10 and lmList[12][2] < lmList[4][2] and lmList[8][2] < lmList[12][2] and flag == 1:
                        cv2.circle(img, (x1, y1), 3, (255, 255, 255), cv2.FILLED)
                        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                        pyautogui.click(wScr - clocX, clocY)
                        flag = 0
                    elif lmList[8][2] < lmList[4][2] + 10 and lmList[12][2] < lmList[4][2] and lmList[8][2] > lmList[12][2]:
                        cv2.circle(img, (x1, y1), 3, (255, 0, 255), cv2.FILLED)
                        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                        clocX = plocX + (x3 - plocX) / smoothening
                        clocY = plocY + (y3 - plocY) / smoothening
                        pyautogui.moveTo(wScr - clocX, clocY)
                        plocX, plocY = clocX, clocY
                        flag = 1
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
    except:
        pass
