from jinja2 import Environment, FileSystemLoader
from constants import *


def generate_html():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('new_template.html')
    output_html = template.render(holder_name=holder_name, holder_document=holder_document,
                                  account_branch=account_branch, account_number=account_number,
                                  reference_year=reference_year, balances=balances)

    with open('output.html', 'w') as file:
        file.write(output_html)

    print(output_html)
    return output_html
