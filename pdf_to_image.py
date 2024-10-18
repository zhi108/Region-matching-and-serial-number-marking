import fitz  # PyMuPDF
import numpy as np
import cv2


def pdf_region_to_image(pdf_path, output_image_path, rect, zoom):
    # 打开PDF文件
    doc = fitz.open(pdf_path)
    # 获取第一页
    page = doc.load_page(0)
    # 设置缩放矩阵以提高分辨率
    mat = fitz.Matrix(zoom, zoom)
    # 获取指定区域的像素图
    pix = page.get_pixmap(matrix=mat, clip=rect)
    # 将像素图转换为图像
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

    # 检查img数组的形状和内容
    print(f"img shape: {img.shape}")
    print(f"img dtype: {img.dtype}")

    # 保存图像
    if img.size > 0:
        cv2.imwrite(output_image_path, img)
    else:
        print("Error: img array is empty.")


def main():
    # rect参数为指定区域的矩形，格式为(x0, y0, x1, y1)
    pdf_region_to_image("input.pdf", "output.png", fitz.Rect(44, 12, 361, 396), 8)
