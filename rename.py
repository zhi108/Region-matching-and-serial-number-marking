import os


def rename_pdf_to_input():
    # 获取当前目录中的所有文件
    files = os.listdir('.')

    # 查找第一个 PDF 文件
    for file in files:
        if file.endswith('.pdf') | file.endswith('.PDF'):
            # 重命名 PDF 文件为 input.pdf
            os.rename(file, 'input.pdf')
            print(f"文件 {file} 已重命名为 input.pdf")
            return

    print("当前目录中没有找到 PDF 文件")


if __name__ == "__main__":
    rename_pdf_to_input()
