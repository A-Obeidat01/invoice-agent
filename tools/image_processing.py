import cv2
import numpy as np
from PIL import Image

def preprocess_invoice_image(image_path: str) -> Image.Image:
    """
    يحسن صورة الفاتورة قبل OCR:
    - أبيض وأسود
    - إزالة الضوضاء
    - تحسين التباين
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=30)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)
    pil_img = Image.fromarray(enhanced)
    return pil_img