import re 
import random 
import string 

def passs(teks): 
    try: 
        mail = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', teks)        
        hasil = []
        for email in mail: 
            username = email.split('@')[0] 
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  
            hasil.append(f'{email} username: {username}, password: {password}')
        
        for item in hasil:
            print(item)
    except Exception as e: 
        print(f"Input yang anda masukkan salah, harap lakukan input ulang. Error: {e}")

teks = 'Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari'
passs(teks)
