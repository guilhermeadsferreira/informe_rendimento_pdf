from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def generate_pdf_by_html(html_string, css_string, pdf_output_path):
    font_config = FontConfiguration()
    html = HTML(string=html_string)
    css = CSS(string=css_string, font_config=font_config)
    html.write_pdf(
        pdf_output_path,
        stylesheets=[css],
        font_config=font_config
    )
