import pytesseract
from tools.db_tool import insert_invoice
from tools.image_processing import preprocess_invoice_image


def extract_invoice_data(image_path: str) -> dict:
    """
    Process an invoice image, extract all text as raw_text, 
    and store it in the database.
    """
    image = preprocess_invoice_image(image_path)
    text = pytesseract.image_to_string(image, lang="eng+ara")
    # Review Text 
    print("OCR text:\n", text)   

    data = {
        "raw_text": text
    }

    insert_invoice(data) 
    return data