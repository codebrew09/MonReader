import easyocr

# Load model once when Flask starts
reader = easyocr.Reader(['en'])

def extract_text(image_path):

    result = reader.readtext(image_path)

    extracted_text = "\n".join(
        item[1] for item in result
    )

    return extracted_text