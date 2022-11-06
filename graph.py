import matplotlib.pyplot as plt
import csv
from firebase_admin import credentials, initialize_app, storage
# import firebase_admin
# from google.cloud import storage
# import os
# import datetime

time = []
bpm = []

with open('filtered_bpm.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		time.append(float(row[1]))
		bpm.append(float(row[2]))

plt.scatter(time, bpm, color = 'g', marker=".")
plt.xticks(rotation = 25)
plt.xlabel('Time (mms)')
plt.ylabel('Heart Rate (bpm)')
plt.title('Analyzing Health conditions, Mood, and Sleeping Patterns from Heart Beats', fontsize = 17)
#plt.show()
plt.savefig("graph.jpg")
plt.savefig("ecaff/src/graph1.jpg")


# Init firebase with your credentials
cred = credentials.Certificate("ecaff-367805-abc72a115b3d.json")
initialize_app(cred, {'storageBucket': 'ecaff-367805.appspot.com'})

# Put your local file path 
fileName = "graph.jpg"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./google.json"
# firebase = firebase.FirebaseApplication('ecaff-367805.appspot.com')
# client = storage.Client()
# bucket = client.get_bucket('ecaff-367805.appspot.com')
# # posting to firebase storage
# imageBlob = bucket.blob("/")
# # imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
# imagePath = "<graph.>/image.png"
# imageBlob = bucket.blob("<image_name>")
# imageBlob.upload_from_filename(imagePath)



# # Fetch the service account key JSON file contents
# cred = credentials.Certificate("./google.json")

# # Initialize the app with a service account, granting admin privileges
# app = firebase_admin.initialize_app(cred, {
#     'storageBucket': 'ecaff-367805.appspot.com',
# }, name='storage')

# bucket = storage.bucket(app=app)
# blob = bucket.blob("/")

# print(blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'))