from generate_html import generate_html
from generate_pdf import *


if __name__ == '__main__':
    html = generate_html()
    generate_pdf_with_weasy(html)
