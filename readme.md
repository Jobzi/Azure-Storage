# Stream files from Azure Storage
In this quickstart, you learn to manage blobs by using Python. Blobs are objects that can hold large amounts of text or binary data, including images, documents, streaming media, and archive data. You'll upload, download, and list blobs, and you'll create and delete containers.
## Prerequisites
- An Azure account with an active subscription. Create an account for free.
- An Azure Storage account. Create a storage account.
- Python.
- Azure Storage SDK for Python.
  
````bash
pip install azure-storage-blob==2.1.0
````

## Copy your credentials from the Azure portal
The sample application needs to authorize access to your storage account. Provide your storage account credentials to the application in the form of a connection string. To view your storage account credentials:

1. In to the Azure portal go to your storage account.
2. In the Settings section of the storage account overview, select Access keys to display your account access keys and connection string.
3. Note the name of your storage account, which you'll need for authorization.
4. Find the Key value under key1, and select Copy to copy the account key.
![key information](https://docs.microsoft.com/en-us/azure/includes/media/storage-copy-account-key-portal/portal-account-key.png)
  Azure Documentation [Azure](https://docs.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-python-legacy)