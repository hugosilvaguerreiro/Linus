import face_recognition
import time
import cv2
import pickle
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's ry any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
#obama_image = face_recognition.load_image_file("obama.jpg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
#biden_image = face_recognition.load_image_file("biden.jpg")
#biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
#known_face_encodings = [
#    obama_face_encoding,
#    biden_face_encoding
#]
users =  {}

known_face_encodings=[]
known_face_names=[]
#known_face_names = [
 #   "Barack Obama",
 #   "Joe Biden"
#]
def getFaceEncoding():
    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    return face_encodings

#loads user faces from memory
def loadKnownFaces(FILENAME=".users_rep.p"):
    return pickle.load( open(FILENAME, "rb" ) )

def saveKnownFaces(knownFaces, FILENAME=".users_rep.p" ):
    pickle.dump( knownFaces, open( FILENAME, "wb" ) )

def userExists(name, knownFaces=None):
    if(knownFaces == None):
        knownFaces = loadKnownFaces()
    return name in knownFaces

#deletes an user
def deleteKnownFace(name):
    knownFaces = loadKnownFaces()
    if(userExists(name, knownFaces)):
        knownFaces.pop(name, None)
        saveKnownFaces(knownFaces)
        return True
    return False

#adds new user
def addKnownFace(faceEncoding, name):
    knownFaces = loadKnownFaces()
    if(not userExists(name, knownFaces)):
        knownFaces[name] = faceEncoding
        saveKnownFaces(knownFaces)
    return False
def getAllUsers():
    knownFaces = loadKnownFaces()
    for name in knownFaces:
        print(name)

#returns user Name
def getFaceUserName(nrTries = 10):
    knownFaces = loadKnownFaces()
    face_encoding = []
    for i in range(0, nrTries):
        face = getFaceEncoding()
        if(face != []):
            face_encoding += face
    for name in knownFaces:
        for face_encod in face_encoding:
            matches = face_recognition.compare_faces(knownFaces[name], face_encod)
            valid = 0
            for i in matches:
                if i == True:
                    valid += 1
            if(valid > len(matches)/2):
                print(matches)
                print(name)
                return
            valid = 0
    return None


#assume there is only one face in the frame
def train_face(name, nrOfTrainLoops = 10):
    # Grab a single frame of video
    face_encodings = []
    result = []
    for i in range(0 ,nrOfTrainLoops):
        print("recognizing..")
        face_encodings = getFaceEncoding()
        if(face_encodings == []):
            print("Error, did not recognize")
            continue
        result.append(face_encodings[0])
        print("recognized\n turn your head a bit")
        time.sleep(1)
    addKnownFace(result, name)

def main():
    exit = False
    while(not exit):
        print("\n\n\n")
        print("choose your option:")
        print("1. Register face")
        print("2. Get face name")
        print("3. Delete face")
        print("4. User Exists")
        print("5. List all users")
        print("6. exit")
        option = eval(input())
        if(option == 1):
            print("what is your name?")
            name = input()
            train_face(name)
        if(option == 2):
            getFaceUserName()
        if(option == 3):
            print("what is your name?")
            name = input()
            deleteKnownFace(name)
        if(option == 4):
            print("what is the name?")
            name = input()
            print(userExists(name))
        if(option==5):
            getAllUsers()           
        if(option == 6):
            exit = True


def main2():
    process_this_frame = True
    face_locations = []
    face_encodings = []
 
    face_names = []
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    print(name)

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        # for (top, right, bottom, left), name in zip(face_locations, face_names):
        #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        #     top *= 4
        #     right *= 4
        #     bottom *= 4
        #     left *= 4

        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #     # Draw a label with a name below the face
        #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # # Display the resulting image
        # cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()
#train_face("Hugo")
#train_face("Matilde")
main()