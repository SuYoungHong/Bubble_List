import json


def write_json(data):
    """
    update json on file
    :param data: nested dictionary of form {company: {field1:value1, field2:value2, etc.}}
    :return: nothing, just updates the json on file
    """
    with open('data/temp.json', 'w') as f:
        json.dump(data, f)


def read_json():
    """
    read json on file
    :return: dictionary of json on file
    """
    try:
        with open('data/temp.json', 'r') as f:
            data = json.load(f)
    except ValueError:
        data = {}
    return data


def breakInfo(info):
    """
    breaks info string delimited by ,, and : into dictionary
    :param info: string of fields and values
    :return: dictionary of fields and values
    """
    companyAttr = {}
    try:
        infoList = info.split(',,')
        for i in infoList:
            field, value = i.strip().split(':')
            companyAttr[field.strip()] = value.strip()
    except Exception:
        pass
    return companyAttr


def updateInfo(old_info, company, info):
    """
    updates the dictionary of json on file with new inputs
    :param old_info: dictionary of json on file
    :param company: string of company name
    :param info: string of info delimited by : and ,,
    :return: nothing, but old info is updated with new info
    """
    if info == '' or company == '':
        if company == '':
            pass
        else:
            old_info[company] = {}
    elif company in old_info:
        new_values = breakInfo(info)
        for i in new_values:
            old_info[company][i] = new_values[i]
    else:
        old_info[company] = breakInfo(info)


def getFields(record):
    """
    takes a record and gets all the company names and field names
    :param record: nested dict, {company: {field1: value1, etc.}, etc.}
    :return: tuple with list of company names and list of field names
    """
    companies = record.keys()
    companies.sort()
    fields = set()
    for i in companies:
        i_fields = record[i].keys()
        if i_fields != []:
            fields.update(i_fields)
    return (companies, fields)


