from builtins import print

from auth import authenticate
from docs import append_entry, get_docs_services, get_next_number
from dotenv import load_dotenv

import os

creds = authenticate()
service = get_docs_services(creds)

load_dotenv()

document_id = DOCUMENT_ID = os.getenv("DOCUMENT_ID")


number = get_next_number(service, document_id)


while True:
    title = input("Title : ")
    original_url = input("Original Url: ")
    shorts_url = input("Shorts Url : ")

    stm = f"Inserting data number : {number}"
    print(stm)
    append_entry(service, DOCUMENT_ID, number, title, shorts_url, original_url)
    number = number + 1
