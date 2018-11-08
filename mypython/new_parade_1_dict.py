
base_url_unit01 = 'https://www.shanbay.com/wordlist/75094/67672/?page=%d'
base_url_unit02 = 'https://www.shanbay.com/wordlist/75094/67699/?page=%d'

name = __file__

def get_url_dict():
    url_dict = {}
    unit01_url_list = []
    unit02_url_list = []
    for i in range(1,11):
        unit01_url_list.append(base_url_unit01 %i)
    url_dict['unit01'] = unit01_url_list
    for i in range(1,7):
        unit02_url_list.append(base_url_unit02 %i)
    url_dict['unit02'] = unit02_url_list
    return url_dict

