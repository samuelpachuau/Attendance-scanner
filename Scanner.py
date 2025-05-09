import cv2
from pyzbar.pyzbar import decode
import time
from tkinter import *
from PIL import Image, ImageTk

scanwindow = None
video_label = None

def scanner_window():
    global scanwindow, video_label
    scanwindow = Toplevel()
    scanwindow.geometry("1000x700")
    scanwindow.title("Scanner - SCANNER")
    scanwindow.config(bg='#113136')

    video_label = Label(scanwindow)
    video_label.place(x=180,y=60)

    scanwindow.after(100, start_scanner)

def start_scanner():
    global video_label
    used_codes = []
    cap = cv2.VideoCapture(0)

    def update_frame():
        success, frame = cap.read()
        if not success:
            print("Failed to read from camera.")
            cap.release()
            return

        # Barcode detection
        for code in decode(frame):
            code_data = code.data.decode('utf-8')
            if code_data not in used_codes:
                print(f"Scanned: {code_data}")
                used_codes.append(code_data)
                time.sleep(1)
            else:
                print("Already scanned")
                time.sleep(1)

        # Convert frame to ImageTk format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk  # Prevent garbage collection
        video_label.configure(image=imgtk)

        # Call again to update next frame
        scanwindow.after(10, update_frame)

    update_frame()
