import cv2
import mysql.connector

def face_recog():
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y: y + h, x: x + w])
            confidence = int((100 * (1 - predict / 300)))

            conn = mysql.connector.connect(host="localhost", user="root", password="hpndjain", database="face_recognizer_2")
            my_cursor = conn.cursor()

            my_cursor.execute("Select Name from student where Student_id=" + str(id))
            n = my_cursor.fetchone()
            n = "+".join(n)

            my_cursor.execute("Select Roll from student where Student_id=" + str(id))
            r = my_cursor.fetchone()
            r = "+".join(r)

            my_cursor.execute("Select Dep from student where Student_id=" + str(id))
            d = my_cursor.fetchone()
            d = "+".join(d)

            if confidence > 77:
                cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Deartment:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            coord = [x, y, w, h]  # Move this line outside the loop

        return coord

    def recognize(img, clf, faceCascade):
        coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
        return img

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")
    video_cap = cv2.VideoCapture(0)

    while True:
        ret, img = video_cap.read()
        img = recognize(img, clf, faceCascade)
        cv2.imshow("Welcome to face recognition", img)

        if cv2.waitKey(1) == 13:  # Press Enter key to exit the loop
            break

    video_cap.release()
    cv2.destroyAllWindows()

# Call the function to start face recognition
face_recog()
