import cv2
import numpy as np
import mysql.connector
import time
import threading

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0 );
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer/trainningData.yml")
font=cv2.FONT_HERSHEY_COMPLEX_SMALL,10,1,0,4

def getProfile(id):
    conn=mysql.connector.connect(host='localhost',
												  database='facebase',
												  user='root',
												  password='')
    cmd="SELECT * FROM People WHERE ID="+str(id)
    mycursor = conn.cursor()
    mycursor.execute(cmd)
    profile=None
    for row in mycursor:
        profile=row
    conn.close()
    return profile

attendance = 0
while True:
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    if(len(faces)!=0):
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            a = id,conf              
            profile=getProfile(id)
            if(profile!=None):
                connection=mysql.connector.connect(host='localhost',
                                                                                                              database='facebase',
                                                                                                              user='root',
                                                                                                              password='')
             
                query = "UPDATE People SET Attendance ='present' WHERE ID="+str(id)
                noti = "UPDATE People SET Notify=0 WHERE ID="+str(id)
                newcursor = connection.cursor()           
                newcursor.execute(query)
                newcursor.execute(noti)
                connection.commit()
                connection.close()               
                cv2.putText(img,"Name : "+str(profile[1]),(x,y+h+20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2);
                cv2.putText(img,"Age : "+str(profile[2]),(x,y+h+45),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2);
                cv2.putText(img,"Gender : "+str(profile[3]),(x,y+h+70),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2);
            
            def attendance3():
                conn3=mysql.connector.connect(host='localhost',
                                                                                                              database='facebase',
                                                                                                              user='root',
                                                                                                              password='')

                cmd3="SELECT * FROM people"
                mycursor3 = conn3.cursor()
                mycursor3.execute(cmd3)
                ID3=None
                attendanceCount=None
                for row in mycursor3:
                    ID3=row[0]
                    attendanceCount=row[4]
                    
                    if(row[4]==1 and a):
                        print("i am attended and i am in class",ID3)
                        connection1=mysql.connector.connect(host='localhost',
                                                                                                                  database='facebase',
                                                                                                                  user='root',
                                                                                                                  password='')

                        querynotify1 = "UPDATE People SET Attendance='Present' WHERE ID="+str(id)
                        newcursor1 = connection1.cursor()
                        newcursor1.execute(querynotify1)
                        connection1.commit()
                        connection1.close()
                return ID3,attendanceCount
            attendance3()
    else:
        def attendance3():
            conn3=mysql.connector.connect(host='localhost',
                                                                                                          database='facebase',
                                                                                                          user='root',
                                                                                                          password='')

            cmd3="SELECT * FROM People"
            mycursor3 = conn3.cursor()
            mycursor3.execute(cmd3)
            ID3=None
            attendanceCount=None
            for row in mycursor3:
                ID3=row[0]
                attendanceCount=row[4]
                if(row[4]!=0 and len(faces)==0):                 
                    print ("i came to class and i left within 20min",ID3)
                    
                else:
                    print("i did not come to school", ID3)                  
            return ID3,attendanceCount
            conn3.close()        
        attendance3()    
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
