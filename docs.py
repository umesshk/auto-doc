from builtins import len, print

import re
from googleapiclient.discovery import build


def get_docs_services(credentials):
    service = build(
        "docs",
        "v1",
        credentials=credentials,
    )

    return service


def append_entry(service, document_id, number, title, shorts_url, original_url):

    text = (
        f"\n{number} {title}\n\tShorts : {shorts_url}\n\tOriginal: {original_url}\n\n"
    )

    requests = [
        {
            "insertText": {
                "endOfSegmentLocation": {},
                "text": text,
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=document_id,
        body={"requests": requests},
    ).execute()


def get_next_number(service, document_id):
    document = get_doc_data(service, document_id)
    data = extract_text(document)
    numbers = re.findall(r"^\s*(\d+)", data, re.RegexFlag.MULTILINE)

    numbers = [int(num) for num in numbers]

    if not numbers:
        return 1

    return numbers[-1] + 1


def get_doc_data(service, document_id):
    return service.documents().get(documentId=document_id).execute()


def extract_text(document):

    text = ""

    for item in document["body"]["content"]:
        if "paragraph" in item:
            paragraph = item["paragraph"]

            for element in paragraph["elements"]:
                if "textRun" in element:
                    text += element["textRun"]["content"]

    return text
