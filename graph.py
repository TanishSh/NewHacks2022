import matplotlib.pyplot as plt
import csv
from firebase_admin import credentials, initialize_app, storage

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


# Init firebase with your credentials
cred = credentials.Certificate("./google.json")
initialize_app(cred, {'storageBucket': 'ecaff-367805.appspot.com'})

# Put your local file path 
fileName = "./graph.jpg"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)