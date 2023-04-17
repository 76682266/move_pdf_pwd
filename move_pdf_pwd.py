import os
import sys
from PyPDF2 import PdfReader, PdfWriter
#author ChatGPT3.5

class PDFManager:
    def __init__(self, filename, password=None):
        """
        初始化PDFManager类，传入要处理的文件名和文件密码（如果有）
        """
        self.filename = filename
        self.password = password

    def remove_password(self):
        """
        解密PDF文件并将其另存为原文件名加上后缀"_nopasswd"的新文件
        """
        # 打开PDF文件
        with open(self.filename, 'rb') as f:
            pdf_reader = PdfReader(f)

            # 检查是否加密
            if pdf_reader.is_encrypted:
                # 设置密码
                pdf_reader.decrypt(self.password)

            # 创建PdfWriter对象
            pdf_writer = PdfWriter()

            # 复制每一页到PdfWriter对象中
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # 另存为新文件
            new_filename = os.path.splitext(self.filename)[0] + '_nopasswd.pdf'
            with open(new_filename, 'wb') as f:
                pdf_writer.write(f)

            print(f'文件"{self.filename}"已成功解密并另存为"{new_filename}"')

if __name__ == '__main__':
    # 获取命令行参数
    if len(sys.argv) < 3:
        print("用法: python a.py filename password")
        sys.exit(1)

    # 获取文件名和密码
    filename = sys.argv[1]
    password = sys.argv[2]

    # 检查文件是否存在
    if not os.path.exists(filename):
        print(f'文件"{filename}"不存在')
        sys.exit(1)

    # 创建PDFManager对象并解密文件
    pdf_manager = PDFManager(filename, password)
    pdf_manager.remove_password()
