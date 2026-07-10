<<<<<<< HEAD
title = input("Enter the title : ")
shorts_link = input("Enter Shorts Link: ")
original_link = input("Enter Original Link : ")


print(title, shorts_link, original_link)
=======
from auth import authenticate
from docs import append_entry, get_docs_services
from dotenv import load_dotenv

import os

creds = authenticate()
service = get_docs_services(creds)

load_dotenv()

document_id = DOCUMENT_ID = os.getenv("DOCUMENT_ID")
print(document_id)


number = input("Enter Number : ")
title = input("Title : ")
original_url = input("Original Url: ")
shorts_url = input("Shorts Url : ")

append_entry(service, DOCUMENT_ID, number, title, shorts_url, original_url)
>>>>>>> 1c27f46 (writng to docs)
