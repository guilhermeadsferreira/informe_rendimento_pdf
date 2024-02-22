from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from enum import Enum
import locale
from generate_pdf import generate_pdf_by_html


# Define an enumeration class
class cash_flow(Enum):
    CASH_IN = 'cash_in'
    CASH_OUT = 'cash_out'
    NONE = 'none'

def format_brazilian_date(date):
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    formatted_date = date.strftime('%d/%m/%Y')
    return formatted_date

def format_brazilian_datetime(date):
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    formatted_date = date.strftime('%d/%m/%Y às %H:%M')
    return formatted_date

def format_brazilian_currency(number, cash_flow = cash_flow.CASH_IN):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    formatted_number = locale.currency(number, grouping=True, symbol=False)
    formatted_number = formatted_number.replace(' ', '')

    is_cash_in = cash_flow == cash_flow.CASH_IN
    is_cash_out = cash_flow == cash_flow.CASH_OUT

    if is_cash_in:
        return "+ R$ " + formatted_number
    if is_cash_out:
        return "- R$ " + formatted_number
    return "R$ " + formatted_number

account = {
    'nickname':'Good morning Vietnam',
    'document':'78.965.922/0001-20',
    'branch':'0001',
    'number':'55454-5'
}

transactions = [
    {
        "date": format_brazilian_date("2024-02-21 00:00:00"),
        "date_amount": format_brazilian_currency(83710.91, cash_flow.NONE),
        "transactions": [
            {
                "id": "ad2378f2-36ba-42be-b9ba-b409041e9ae7",
                "document": "53327618216",
                "transacted_at": format_brazilian_date("2024-02-22 13:14:59"),
                "event": "Transferência Pix recebida",
                "cash_flow": "cash_in",
                "context": "pix",
                "is_refund": False,
                "can_refund": True,
                "balance_before": format_brazilian_currency(83910.91),
                "balance_after": format_brazilian_currency(83870.91),
                "amount": format_brazilian_currency(40, cash_flow.CASH_IN),
                "display_message": "Medicamentos de Reodores de Pequeno Porte e CIA LTDA ME"
            }
        ]
    },
    {
        "date": format_brazilian_date("2024-02-22 23:59:59"),
        "date_amount": format_brazilian_currency(83670.91, cash_flow.NONE),
        "transactions": [
            {
                "id": "c8dd99f0-cafd-4cfb-8e49-7248d2d21a89",
                "document": "78250420268",
                "transacted_at": format_brazilian_date("2024-02-21 16:02:56"),
                "event": "Transferência Pix enviada",
                "cash_flow": "cash_out",
                "context": "pix",
                "is_refund": False,
                "can_refund": True,
                "balance_before": format_brazilian_currency(83770.81),
                "balance_after": format_brazilian_currency(83670.91),
                "amount": format_brazilian_currency(100, cash_flow.CASH_OUT),
                "display_message": "Roupa de Hamster ltda"
            },
            {
                "id": "a6dd88f0-cafd-4cfb-8e49-5241d2d21a89",
                "document": "78250420268",
                "transacted_at": format_brazilian_date("2024-02-21 10:02:56"),
                "event": "Transferência TED recebida",
                "cash_flow": "cash_in",
                "context": "ted",
                "is_refund": False,
                "can_refund": True,
                "balance_before": format_brazilian_currency(83970.91),
                "balance_after": format_brazilian_currency(83770.81),
                "amount": format_brazilian_currency(200.1, cash_flow.CASH_IN),
                "display_message": "Roupa de Hamster ltda"
            }
        ]
    },
]


def gerar_extrato():
    environment = Environment(loader=FileSystemLoader("./extrato"))
    template = environment.get_template("./template.html")
    html_string = template.render(
        transactions=transactions,
        start_date=format_brazilian_date("2024-02-21 00:00:00"),
        end_date=format_brazilian_date("2024-02-22 23:59:59"),
        created_at=format_brazilian_datetime("2024-02-24 13:20:23"),
        account=account
    )
    filename = './extrato/output.html'
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(html_string)
        print(f"... wrote {filename}")
    with open('./extrato/styles.css', 'r', encoding='utf-8') as css:
        css_string = css.read()
    pdf_output_path = './extrato/extrato.pdf'
    generate_pdf_by_html(html_string, css_string, pdf_output_path)