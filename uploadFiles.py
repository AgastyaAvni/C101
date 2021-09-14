import os
from posixpath import realpath
import dropbox
import dropbox.files 

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def uploadFile(self,fileFrom,fileTo):

        dbx=dropbox.Dropbox(self.accessToken)

       for root,dirs,files in os.walk(file_from):

           for filename in files:

               local_path = os.path.join(root,filename)

               relative_path=os.path.relpath(local_path,file_from)
               dropbox_path=os.path
    
    def main():
    accessToken='5mZ0KbVgiCoAAAAAAAAAAemvr1dtLjYWqnAXqglwAeaO-C1MnFDTwnflY_AfVEPg'
    transferData=TransferData(accessToken)
    fileFrom=input('PLease enter the file path to transfer - ')
    fileTo=input('Please enter the file path to dropbox - ')
    transferData.uploadFile(fileFrom,fileTo)
    print('File has been moved')
main()


    





