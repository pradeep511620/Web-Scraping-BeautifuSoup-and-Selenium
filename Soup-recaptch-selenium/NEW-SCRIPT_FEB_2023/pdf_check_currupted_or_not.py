import requests
from io import BytesIO
from PyPDF2 import PdfReader

url = "https://cdn.raptorsupplies.com/pub/media/catalog/product/datasheet/guardian-equipment-g1950pcc.pdf"

response = requests.get(url)

if response.status_code == 200:
    content = response.content
    try:
        if not content:
            raise ValueError("Empty content")

        content = BytesIO(content)

        pdf_reader = PdfReader(content)

        if len(pdf_reader.pages) > 0:
            print("PDF file is valid and accessible.")
        else:
            print("PDF file is not valid or empty.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Failed to load PDF document.")
