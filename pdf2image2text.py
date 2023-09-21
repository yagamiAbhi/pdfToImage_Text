from pdf2image import convert_from_path
from PIL import Image
import pytesseract


def to_image(pdf_file):
    images = convert_from_path(pdf_file, poppler_path=r'C:\poppler-23.08.0\Library\bin')
    save_image(images)
    return images


def save_image(images):
    for i, image in enumerate(images):
        image.save(f"page{i + 1}.png", "PNG")


def to_text(pdf_file):
    images = to_image(pdf_file)
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        print(f"Page {i + 1} Text:")
        print(text)
        save_text(text)


def save_text(text):
    file_path = "output.txt"
    with open(file_path, 'a') as file:
        file.write(text)
        print("String saved to", file_path)


to_text("sample.pdf")
