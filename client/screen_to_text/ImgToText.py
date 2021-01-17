try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    dic = pytesseract.image_to_string(Image.open("./" + filename))
    text = ""
    for i in dic:
        text = text + i
    return text
