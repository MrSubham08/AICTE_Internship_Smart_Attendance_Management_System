import tkinter as tk
import cv2
import os

# Main window setup
window = tk.Tk()
window.title("Simple Attendance System")
window.geometry('600x400')
window.configure(background='lightgrey')

# Function to capture and save images
def take_img():
    enrollment = txt.get()
    name = txt2.get()
    if enrollment == '' or name == '':
        Notification.configure(text="Enrollment & Name required!", bg="red", fg="white")
    else:
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        sampleNum = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            
            # Add text overlay to display the name on the video feed
            cv2.putText(img, f"Name: {name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
            for (x, y, w, h) in faces:
                sampleNum += 1
                # Save the captured face image
                cv2.imwrite("TrainingImage/" + name + "." + enrollment + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            cv2.imshow('Capturing Images', img)
            # Break the loop when 'q' is pressed or required number of samples are captured
            if cv2.waitKey(4) & 0xFF == ord('q') or sampleNum >= 1:
                break
            
        cam.release()
        cv2.destroyAllWindows()
        Notification.configure(text="Image Captured and Saved for Enrollment: " + enrollment + " Name: " + name, bg="green", fg="white")
