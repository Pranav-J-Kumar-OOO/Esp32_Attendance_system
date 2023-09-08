import face_recognition
import cv2
import numpy as np
import blynk_ as blynk
from datetime import datetime
import gspread

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H-%M-%S")

sa = gspread.service_account(filename="C:\Project\App\plated-axon-293209-d2d83023f657.json")
print("------------------------------------------------------------------------------------")
print("Make sure you have added 'googlesheetattendance@plated-axon-293209.iam.gserviceaccount.com' to your google spreadsheet")
print("------------------------------------------------------------------------------------")
imgLink = input("The link of the image please. Enter '0' or digit of your webcam for using the webcam: ")
print("------------------------------------------------------------------------------------")
gsName = input("Name of the google spreadsheet: ")
sh = sa.open(gsName)
title = f"{current_date}, {current_time}"
wks = sh.add_worksheet(title=title, rows="100", cols="100")

wks.update("A1", "Roll No")
wks.format('A1', {'textFormat': {'bold': True}})

wks.update("B1", "Name")
wks.format('B1', {'textFormat': {'bold': True}})

wks.update("C1", "Present/Late/Absent")
wks.format('C1', {'textFormat': {'bold': True}})

wks.update("D1", "Time")
wks.format('D1', {'textFormat': {'bold': True}})

print("------------------------------------------------------------------------------------")
print("Processing images and worksheet, this may take a while....")
print("------------------------------------------------------------------------------------")

#GSpread functions
def writeRoll(Cell_coodinates, String):
    wks.update(f"A" + str(Cell_coodinates), str(String))

def writeName(Cell_coodinates, String):
    wks.update(f"B" + str(Cell_coodinates), str(String))

def writePAL(Cell_coodinates, String):
    wks.update(f"C" + str(Cell_coodinates), str(String))

def writeTime(Cell_coodinates, String):
    wks.update(f"D" + str(Cell_coodinates), str(String))

if imgLink != "0":
    video_capture = cv2.VideoCapture(imgLink)
else:
    video_capture = cv2.VideoCapture(str(imgLink))
#video_capture = cv2.VideoCapture("http://192.168.129.160/mjpeg/1")
#video_capture = cv2.VideoCapture(0)

pjk_img = face_recognition.load_image_file("./Backup/known_images/pjk.jpg")
pjk_encode = face_recognition.face_encodings(pjk_img)[0]

jay_img = face_recognition.load_image_file("./Backup/known_images/jay.jpg")
jay_encode = face_recognition.face_encodings(jay_img)[0]

# nishanth_img = face_recognition.load_image_file("./known_images/nishanth.png")
# nishanth_encode = face_recognition.face_encodings(nishanth_img)[0]

known_face_encoding = [pjk_encode, jay_encode]#, nishanth_encode]
known_face_names = ["Pranav J Kumar", "Jay Shyamalan"]#, "Nishanth Krishna"]
known_face_id = [1,2]#,3]

absenties = known_face_names.copy()
absentiesId = known_face_id.copy()

face_locations = []
face_encodings = []
face_names = []
s = True
rowList = 2

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H-%M-%S")
blynk.write(0, 0)

result = None
resultId = None

while True:
    _,frame = video_capture.read()
    large_frame = cv2.resize(frame,(0,0),fx = 0.25,fy =0.25)
    rgb_small_frame = large_frame[:,:,::-1]

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            result = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                result = known_face_names[best_match_index]
                resultId = known_face_id[best_match_index]

            face_names.append(result)
            if result in known_face_names and result in absenties:
                if int(now.strftime("%H")) < 8:
                    blynk.write(0, resultId)
                    absenties.remove(result)
                    absentiesId.remove(resultId)
                    print(absenties)
                    current_time = now.strftime("%H-%M-%S")
                    # Here we add the admition number is first that is the resultId variable, the name in second that is the result variable, present in third, time in fourth coloumn
                    writeRoll(rowList, resultId);writeName(rowList, result);writePAL(rowList, "Present");writeTime(rowList, current_time)
                    rowList += 1

                else:
                    blynk.write(0, resultId)
                    absenties.remove(result)
                    absentiesId.remove(resultId)
                    print(absenties)
                    # Here we add the id that is the resultId variable,the name in second that is the result variable, late in third, time in fourth coloumn
                    writeRoll(rowList, resultId);writeName(rowList, result);writePAL(rowList, "Late");writeTime(rowList, current_time)
                    rowList += 1

    cv2.imshow("Attendance system", frame)
    if cv2.waitKey(1) & 0xFF == ord('q') or absenties == [] or cv2.getWindowProperty("Attendance system", cv2.WND_PROP_VISIBLE) < 1 :#or int(now.strftime("%H")) > 9 : 
        #add all the absenties to the sheets
        if(absenties != []):
            for i in range(len(absenties)):
                writeRoll(i+3, absentiesId[i]);writeName(i+3, absenties[i]);writePAL(i+3, "Absent");writeTime(i+3, current_time)
        print("------------------------------------------------------------------------------------")
        break