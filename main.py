import firebase_admin
from firebase_admin import credentials, storage
import sys
import os
import time
cred = credentials.Certificate("./info.json") ## add your cred file here
firebase_admin.initialize_app(cred, {
    'storageBucket': '<your bucket link>.appspot.com'
})

arg = sys.argv[1]


def init() :
    ## Input for file name and global access code
    filename = input("Enter the filename:")
    globalaccesscode = int(input("Enter the global access code:"))

    ## Create the file data.txt to store the give info above
    with open("data.txt", "w") as file:
        file.write(filename + "\n")
        file.write(str(globalaccesscode))
    
    local_file_path = "./"+filename
    destination_blob_name = str(globalaccesscode)+"/"+filename

    ##init the bucket to upload the given file
    try:
        bucket = storage.bucket()
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file_path)
        print("File uploaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if(arg=='Sender'):
    init()



if(arg=='Receiver'):
    globalaccesscode = int(input("Enter the global access code:"))
    filename = input("Enter the filename which the sender has kept:")
    
    with open("data.txt", "w") as file:
        file.write(filename + "\n")
        file.write(str(globalaccesscode))
        
    local_file_path = filename
    source_blob_name = str(globalaccesscode)+"/"+filename

    ## init for downloading the file
    try:
        bucket = storage.bucket()
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(local_file_path)
        print("File downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



if(arg=='push'):
    try:
        try:
            ## open the file and read if fail then run init function
            with open("data.txt", "r") as file:
                lines = []

                ## run a loop and store the values into lines
                for line in file:
                    cleaned_line = line.strip()
                    lines.append(cleaned_line)
            local_file_path = "./" + lines[0]
            destination_blob_name = str(lines[1]) + "/" + lines[0]

            ## upload the file
            try:
                bucket = storage.bucket()
                blob = bucket.blob(destination_blob_name)
                blob.upload_from_filename(local_file_path)
                print("File uploaded successfully.")
            except Exception as e:
                print(f"An error occurred: {e}")
        except:
            print("You have not initialised, Please Initially it now!")
            init()
            
     except:
        print("You have not initialised, Please Initially it now!")
        init()



if(arg=='get'):
    try:

        ## open the file
        with open("data.txt", "r") as file:
            lines = []
            for line in file:
                cleaned_line = line.strip()
                lines.append(cleaned_line)

        local_file_path = "./" + lines[0]
        destination_blob_name = str(lines[1]) + "/" + lines[0]
        
        try:
            bucket = storage.bucket()
            blob = bucket.blob(destination_blob_name)
            blob.download_to_filename(local_file_path)
            print("File downloaded successfully.")

            ## run the code after download
            os.system("clang++ "+ local_file_path + " -o output")
            time.sleep(2)
            os.system("./output")

        
        except Exception as e:
            print(f"An error occurred: {e}")
    except:
        print("You have not initialised, Please Initially it now!")
        init()
