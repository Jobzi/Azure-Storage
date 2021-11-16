import os
import json
from azure.storage.blob.blockblobservice import BlockBlobService

ACCOUNT_KEY ="rAxaHDPa2yj06KShV7f+Pe6esNX/Bub6t+9LXtyksBAF6OxQGcJVDGbIudfjOxtcCe83wEbm2v+9t3ApJNUwUg=="

class FileStream:
    account_name = "storagefiles2"
    container_name = "ioetfiles"

    def __init__(self,account_name:str = account_name,container_name:str = container_name):
        self.account_name = account_name
        self.container_name = container_name
        self.blob_service = BlockBlobService(account_name=self.account_name, account_key=ACCOUNT_KEY)

    def get_file_stream(self, filename:str):
        import tempfile 
        try:
            local_file = tempfile.NamedTemporaryFile()
            self.blob_service.get_blob_to_stream(self.container_name, filename, stream=local_file)

            local_file.seek(0)
            return local_file
        except Exception as e:
            print(e)
            return None 
                
#fs = FileStream()
#result = fs.get_file_stream("activity.json")
#
#print(json.load(result))