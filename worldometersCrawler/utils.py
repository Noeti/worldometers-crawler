import re

def clean_consump(string):
    return re.search('\((.*?)\)', string).group(1)
    
def clean_commas(string):
    return string.replace(",", "")

def clean_year(string):
    temp = re.findall(r'\d+', string)
    return temp[0]

def clean_lst(lst):
    return list(filter(None,[item.strip() for item in lst]))

def clean_names(lst):
    return list(map(lambda x: '_'.join(x.lower().split()), lst))

def clean_values(lst):
    return list(map(lambda x: re.sub("[ ,]", "", x), lst))