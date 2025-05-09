# Scanner.py

import cv2
from pyzbar.pyzbar import decode
import time

def start_scanner():
    used_codes = []
    cap = cv2.VideoCapture(0)
    #cap.set(3, 640)
    #cap.set(4, 480)

    print("Starting barcode scanner. Press 'q' to quit.")

    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Failed to read from camera.")
                break

            for code in decode(frame):
                code_data = code.data.decode('utf-8')
                if code_data not in used_codes:
                    print(f"Scanned: {code_data}")
                    used_codes.append(code_data)
                    time.sleep(1)
                else:
                    print("Already scanned")
                    time.sleep(1)

            cv2.imshow('Testing-code-scan', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Camera released and windows closed.")
