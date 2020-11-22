#/usr/bin/python


import sys

number  = sys.argv



file_name = ('./pnn_Publico_20_11_2020.csv')
csv_file = open(file_name,'rb')
tels = {}
header = [csv_file.next()]




class telefon:
    def __init__(self, row_list):
        self.lada = row_list[7]
        self.serie = row_list[8]
        self.incial = row_list[9]
        self.final = row_list[10]
        self.tipo = row_list[12]
        self.compania = row_list[14]



def get_phones(csv_file):
    tels = {}
    for row in csv_file:
        tt = telefon(row.split(','))
        if not tels.get(tt.lada):
            tels[tt.lada] = {}
        if not tels[tt.lada].get(tt.serie):
            tels[tt.lada][tt.serie] = {}

        tels[tt.lada][tt.serie].update({
            'inicial':tt.incial,
            'final':tt.final,
            'tipo':tt.tipo,
            'compania':tt.compania})
    return tels



def search_area(phone):
    res = {'area_code':None, 'phone_series':None}
    if tels.get(phone[:2]):
        res = {'area_code':phone[:2], 'phone_series':tels[phone[:2]]}
    elif tels.get(phone[:3]):
        res = {'area_code':phone[:3], 'phone_series':tels[phone[:3]]}
    return res

def search_serie(serie, x_phone ):
    #print 'serie' , serie
    res = {'seire':None, 'datos':None}
    if serie.get(x_phone[:3]):
        res.update({'serie':phone[:3], 'datos':serie[x_phone[:3]]})
    elif serie.get(phone[:4]):
        res.update({'serie': x_phone[:4] ,'datos': serie[x_phone[:4]]})
    return res


if __name__ == "__main__":
    if (number) > 2:
        phone = number[1]
        print 'phone', phone
        tels = get_phones(csv_file)
        #print 'tels' , tels
        result = search_area(phone)
        if result['area_code']:
            area_code =  result['area_code']

        x_phone = phone[len(area_code):]
        print 'area code', area_code
        print 'x_phone',x_phone

        # print tels
        res = search_serie(tels[area_code], x_phone)

        print 'result',res

    else:
        print 'no phone provided'

