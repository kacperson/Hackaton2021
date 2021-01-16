try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
<<<<<<< HEAD

pytesseract.image_to_string(Image.open("test.png"))
=======
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
>>>>>>> 6ef5953c6074fa38dd6bb039423e82e45b5ae00d
def ocr_core(filename):

    text = pytesseract.image_to_string(Image.open(filename))
    
    return text
