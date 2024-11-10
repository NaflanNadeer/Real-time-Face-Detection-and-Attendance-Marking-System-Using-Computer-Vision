Real-Time Face Detection and Attendance Marking System Using Computer Vision
This project is a facial recognition-based attendance management system that automates the attendance process by capturing and identifying student faces in real-time through a webcam. Built with Python, OpenCV, and MySQL, it updates each recognized student's attendance status in a database.

Project Structure
* dataset creator.py: Captures face images of students and stores them in a dataset, along with their details in a MySQL database.

* trainer.py: Trains a facial recognition model using the captured images with the LBPH algorithm and saves the trained model.

* detector.py: Detects and recognizes student faces in real-time and updates their attendance status in the database.

* haarcascade_frontalface_default.xml: A pre-trained model file for face detection using OpenCV.

* people.sql: SQL script to set up the MySQL database table (People) for storing student information.

* Folders:
  dataSet: Folder where the captured face images are saved.
  recognizer: Folder where the trained model file is saved.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setup Instructions
Database Setup:

1. Ensure you have MySQL installed and running.
2. Create a database (e.g., facebase).
3. Run people.sql to set up the required table for storing student information.
Folder Structure:

Create the following folders in the project directory:

1. dataSet - for storing captured face images.
2. recognizer - for storing the trained model file.
3. Install Dependencies:
4. Install the necessary Python libraries. #pip install


Usage:

* Dataset Creator: Run dataset creator.py to capture and store images of each student. You will be prompted to enter the student’s ID, name, age, and gender.
* Trainer: Run trainer.py to train the facial recognition model using the images stored in dataSet. The trained model will be saved in the recognizer folder as trainningData.yml.
* Detector: Run detector.py to start the real-time attendance system. The system will use the webcam feed to detect and recognize students and mark their attendance in the database.


Requirements

1. Python 3.x
2. OpenCV for image processing and facial recognition
3. MySQL for storing and updating attendance data


Note:
Ensure your MySQL database connection details (host, user, password) match your setup in each script.
