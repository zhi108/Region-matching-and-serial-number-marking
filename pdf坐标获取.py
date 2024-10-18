import fitz  # PyMuPDF
import cv2
import numpy as np


def pdf_to_image(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    return img


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"点击坐标：({x}, {y})")


image = pdf_to_image("input.pdf")
cv2.imshow("PDF Page", image)
cv2.setMouseCallback("PDF Page", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
