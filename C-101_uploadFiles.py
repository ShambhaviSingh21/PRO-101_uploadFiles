import os
import dropbox


class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, source, destination):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(source):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, source)
                dropbox_path = os.path.join(destination, relative_path)
                   
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJPCdOh8sbfBx73KEEf_dY33tUv3t7aDncCc3MgWNJIu5XZXq9DH5eA0D9G74XQAPDkjxceiKsnMlvw71kUsIEkqcXLW63qMtWQkgjULqzcgekKvVkn5WjKzemfAWWLgx5IZq_o'
    transferData = TransferData(access_token)

    source = str(input("Enter the folder path to transfer : -"))
    destination = input("enter the full path to upload to dropbox:- ") 

    transferData.upload_file(source,destination)
    print("file has been moved !!!")

main()