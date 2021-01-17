# AutoNotes

## Will convert your lecture into notes in real time
### The app has to do several functions:
- Record lecturer
- Screenshot presentation
- both convert to text
### It's very useful during lectures, conferences and many other meetings .

### You need to install:
  1. run setup.sh
  2. download <https://github.com/UB-Mannheim/tesseract/wiki> and you have to add path to ./client/screen_to_text/ImgToText.py file:
    ```pytesseract.pytesseract.tesseract_cmd = r'<YourPath>\Tesseract-OCR\tesseract.exe' ```
  3. run AutoNotes
### Or you can:
  1. go to ./client/dist
  2. run main.exe
