import os
import json

try:
    from TiketcomAPI import(Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from TiketcomAPI import(
        Client, __version__ as client_version)

if __name__ == '__main__':
    print('Client version: {0!s}'.format(client_version))

    api = Client()

    tanggal = input('Scraping data tanggal berapa? (Format YYYY-MM-DD, contoh: 2020-10-13) : ')

    while True:
        prov = input('Scraping data provinsi mana? (Bali, Yogyakarta, NTB, Sulsel, Sumut) : ')
        if prov.lower() == 'bali':
            region = 'REGION'
            city = 'bali-108001534490276212'
            break
        elif prov.lower() == 'yogyakarta':
            region = 'REGION'
            city = 'yogyakarta-province-108001534490276304'
            break
        elif prov.lower() == 'ntb':
            region = 'REGION'
            city = 'west-nusa-tenggara-108001534490280165'
            break
        elif prov.lower() == 'sulsel':
            region = 'REGION'
            city = 'south-sulawesi-108001534490277179'
            break
        elif prov.lower() == 'sumut':
            region = 'REGION'
            city = 'north-sumatera-108001534490276409'
            break
        else:
            print('Kode kota tidak ditemukan')


    result = api.search(region, city, tanggal, page = 2)

    _dir = os.path.dirname(__file__)
    _dir = os.path.join(_dir, 'json')

    if not os.path.exists(_dir):
        print("\n\nCreating json folder..\n\n")
        os.makedirs(_dir)

    with open(_dir + '/{}_{}.json'.format(prov, tanggal), 'w') as outfile:
        json.dump(result, outfile, indent=2)

    print('All ok')
