import requests


def transfer_dict_parameter():
    payload = {
        'key1': 'value1',
        'key2': 'value2'
    }

    transfer_dict_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print('transfer_dict_parameter_url: ', transfer_dict_parameter_result.url)
    print('transfer_dict_parameter_text: ', transfer_dict_parameter_result.text)


transfer_dict_parameter()


def transfer_tuple_parameter():
    payload = (
        ('key1', 'value1'),
        ('key2', 'value2')
    )

    transfer_tuple_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print('transfer_tuple_parameter_url: ', transfer_tuple_parameter_result.url)
    print('transfer_tuple_parameter_text: ', transfer_tuple_parameter_result.text)


transfer_tuple_parameter()


def transfer_string_parameter():
    payload = {
        'string1', 'value'
    }

    transfer_string_parameter_result = requests.post('https://httpbin.org/post', params=payload)
    print('transfer_string_parameter_url: ', transfer_string_parameter_result.url)
    print('transfer_string_parameter_text: ', transfer_string_parameter_result.text)


transfer_string_parameter()


def transfer_multipart_encoded_file():
    interface_url = 'https:/httpbin.org/post'
    files = {
        'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})
    }

    transfer_multipart_encoded_file_result = requests.post(url=interface_url, files=files)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.url)
    print('transfer_multipart_encoded_file_result_url: ', transfer_multipart_encoded_file_result.text)


transfer_multipart_encoded_file()
