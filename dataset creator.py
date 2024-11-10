import cv2
import numpy as np
import mysql.connector

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture (0);

def insertorUpdate(Id,Name,Age,Gender):
	conn=mysql.connector.connect(host='localhost',
												  database='facebase',
												  user='root',
												  password='')
	cmd="SELECT * FROM people WHERE ID ="+str(Id)

	mycursor = conn.cursor()
	mycursor.execute(cmd)
	isRecordExist=0
	for row in mycursor:
		isRecordExist=1
	if(isRecordExist==1):
		cmd = "UPDATE people SET Name=" + str(Name) + "WHERE ID=" + str(Id)
		cmd2 = "UPDATE people SET Age=" + str(Age) + "WHERE ID=" + str(Id)
		cmd3 = "UPDATE people SET Gender=" + str(Gender) + "WHERE ID=" + str(Id)
	else:
		cmd = "INSERT INTO people(ID,Name,Age,Gender) Values(" +  str(Id) + "," + str(Name) + "," + str(Age) + "," + str(
			Gender) + ")"
		cmd2 = ""
		cmd3 = ""
		mycursor.execute(cmd)
		mycursor.execute(cmd2)
		mycursor.execute(cmd3)
		conn.commit()
		conn.close()


id=input('enter user id: ')
name=input('enter user name: ')
age=input('enter user age: ')
gender=input('enter user gender: ')
insertorUpdate(id,name,age,gender)
SampleNum = 0;
while (True):
		ret, img = cam.read();
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces = faceDetect.detectMultiScale(gray,1.3,5);
		for(x,y,w,h) in faces:
				SampleNum=SampleNum+1;
				cv2.imwrite("dataSet/User."+str(id)+"."+str(SampleNum)+".jpg",gray[y:y+h,x:x+w])
				cv2.rectangle(img, (x,y) , (x+w,y+h) , (0,0,255),2)
				cv2.waitKey(100);
		cv2.imshow("Face",img);
		cv2.waitKey(1);
		if(SampleNum>200):
				break
cam.release()
cv2.destroyAllWindows()
