import mediapipe as mp
import cv2
import pyautogui

mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Define the rectangle within the monitor area
monitor_width, monitor_height = pyautogui.size()

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = mp_hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_x = hand_landmarks.landmark[8].x * monitor_width
                index_finger_y = hand_landmarks.landmark[8].y * monitor_height

                if futuristic_effect:
                    cv2.circle(frame, (int(index_finger_x), int(index_finger_y)), 15, (255, 0, 0), -1)

                pyautogui.moveTo(int(index_finger_x), int(index_finger_y))

                # Simulate left click if hand is closed
                if results.multi_handedness[0].classification[0].label == 'Right' and results.multi_hand_landmarks[0].landmark[4].y > results.multi_hand_landmarks[0].landmark[3].y:
                    pyautogui.click()

        cv2.imshow('Hand Control', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
