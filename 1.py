import re
from datetime import datetime

def ganti_tanggal(teks): 
    try: 
        tanggal = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', teks)
        hasil = []        
        for tgl in tanggal:         
            tglh = datetime.strptime(tgl, '%Y-%m-%d') 
            tglbaru = tglh.strftime('%d-%m-%Y') 
            selisih_hari = (datetime.now() - tglh).days 
            hasil.append(f'{tglbaru} 00:00:00 selisih {selisih_hari} hari')
        
        for item in hasil:
            print(item)
    except Exception as e: 
        print("Kesalahan Input")

teks = 'Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).' 
ganti_tanggal(teks)
