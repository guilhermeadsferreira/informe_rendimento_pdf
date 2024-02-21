api_response = {
    "data": {
        "holder": {
            "type": "BUSINESS",
            "createdAt": "2023-07-25T13:27:19.235Z",
            "name": "50515887 IGOR LUCIANO MAGRO",
            "document": {
                "value": "50515887000129",
                "type": "CNPJ"
            }
        },
        "account": {
            "branch": "0001",
            "number": "1109073833"
        },
        "payers": [
            {
                "source": {
                    "name": "Acesso Soluções De Pagamento SA - Instituição de Pagamento",
                    "document": {
                        "value": "13140088000199",
                        "type": "CNPJ"
                    }
                },
                "currencies": {
                    "brl": {
                        "balances": [
                            {
                                "year": 2022,
                                "amount": {
                                    "value": 0.00,
                                    "currency": "BRL"
                                }
                            },
                            {
                                "year": 2023,
                                "amount": {
                                    "value": 3.69,
                                    "currency": "BRL"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    },
    "links": [
        {
            "url": "/api/accounts/1109073833/income-report",
            "rel": "get_income_report",
            "method": "GET"
        }
    ]
}
response_data = api_response['data']
holder_name = response_data['holder']['name']
holder_document = response_data['holder']['document']['value']
account_branch = response_data['account']['branch']
account_number = response_data['account']['number']
balances = response_data['payers'][0]['currencies']['brl']['balances']
reference_year = balances[-1]['year']