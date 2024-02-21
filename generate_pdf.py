from pyppeteer import launch
from time import sleep
import asyncio
import pdfkit
from xhtml2pdf import pisa
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

output_pdf = './output.pdf'


def generate_pdf_with_pdf_kit(output_html):
    try:
        pdfkit.from_string(output_html)
    except Exception as e:
        print("handle_use_pdf_kit:", e)


async def create_pdf_with_pyppeteer(output_html):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setContent(output_html)
    sleep(10)
    await page.pdf({'path': output_pdf, 'format': 'A4'})
    await browser.close()


def generate_pdf_with_pyppeteer(output_html):
    asyncio.get_event_loop().run_until_complete(create_pdf_with_pyppeteer(output_html))

def generate_pdf_with_weasy(html_string):
    font_config = FontConfiguration()
    html = HTML(string='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h3>Teste</h3>
        </body>
        </html>
    ''')
    css = CSS(string='''
            @font-face {
                font-family: MyRightToLeftFont;
                src: url("./fonts/Nunito-Regular.ttf");
                font-weight: normal;
              }
        
              @font-face {
                font-family: MyRightToLeftFont;
                src: url("./fonts/Nunito-Bold.ttf");
                font-weight: bold;
              }
              
      h3 {
        color: #00a786;
        font-family: MyRightToLeftFont;
        font-weight: bold;
      }
    ''', font_config=font_config)
    html.write_pdf(
        '/tmp/example.pdf', stylesheets=[css],
        font_config=font_config)

def generate_pdf_with_pisa(html_string):
    with open(output_pdf, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
    return not pisa_status.err

