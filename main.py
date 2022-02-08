"""
Aplikasi deteksi gempa terkini
Modularisasi dengan Function

"""
def ekstraksi_data():
    """
    08 Februari 2022, 07:29:30 WIB
    3.2
    10 km
    2.52 LS - 140.55 BT
    Pusat gempa berada di darat 8 km barat laut Kota Jayapura
    Dirasakan (Skala MMI): II-III Kabupaten Jayapura, II Kota Jayapura

    """
    hasil = dict()
    hasil['tanggal'] = '24 agustus 2021'
    hasil['waktu'] = '07:29:30 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'ls' : 1.48, 'bt': 134.25}
    hasil['pusat'] = 'Pusat gempa berada di darat 18 km barat laut papua'
    hasil['dirasakan'] = '(Skala MMI): II-III Kabupaten Jayapura, II Kota Jayapura'


    return hasil




def tampilkan_data(result):
    print("gempa terakhir berdasarkan BMKG ")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")



if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
