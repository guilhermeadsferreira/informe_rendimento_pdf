from jinja2 import Environment, FileSystemLoader
from informe.constants import *
from generate_pdf import generate_pdf_by_html


def handle_generate_balance():
    env = Environment(loader=FileSystemLoader('./informe'))
    template = env.get_template('./template.html')
    html_string = template.render(holder_name=holder_name, holder_document=holder_document,
                                  account_branch=account_branch, account_number=account_number,
                                  reference_year=reference_year, balances=balances)
    with open('./informe/output.html', 'w') as file:
        file.write(html_string)
    with open('./informe/styles.css', 'r', encoding='utf-8') as css:
        css_string = css.read()
    pdf_output_path = './informe/informe.pdf'
    generate_pdf_by_html(html_string, css_string, pdf_output_path)