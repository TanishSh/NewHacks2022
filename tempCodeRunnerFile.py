cred = credentials.Certificate("./google.json")
initialize_app(cred, {'storageBucket': 'gs://ecaff-367805.appspot.com/.'})

# Put your local file path 
fileName = "./graph.jpg"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)