try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.image_to_string(Image.open("test.png"))
def ocr_core(filename):

    text = pytesseract.image_to_string(Image.open(filename))
    
    return text

#print(ocr_core("test.png"))