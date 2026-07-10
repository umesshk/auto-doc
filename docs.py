from googleapiclient.discovery import build


def get_docs_services(credentials):
    service = build(
        "docs",
        "v1",
        credentials=credentials,
    )

    return service


def append_entry(service, document_id, number, title, shorts_url, original_url):

    text = f"{number} {title}\n\tShorts : {shorts_url}\n\tOriginal: {original_url}\n\n"

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
