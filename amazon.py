# -*-coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import time

URL="https://www.amazon.it/Asus-GeForce-Advanced-Scheda-Grafica/dp/B07HNRKP7Z?pf_rd_p=e610d385-7bae-4f5e-8f7b-20508656a584&pd_rd_wg=SRMZo&pf_rd_r=6JMVEPFWY2RFKRBD0EDV&ref_=pd_gw_cr_cartx&pd_rd_w=3gKIp&pd_rd_r=6840a604-05d1-4be6-a522-f150749f43fb"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def controlla_prezzo():
    pagina = requests.get(URL, headers=headers)

    soup = BeautifulSoup(pagina.content, 'html.parser')

    prezzo = soup.find(id="priceblock_ourprice").get_text()
    if len(prezzo) > 9:
        prezzo_conVirgola = prezzo[0:8]
        prezzo_convertito = float(prezzo[0:8].replace(',',''))
    else:
        prezzo_convertito = float(prezzo[0:4].replace(',',''))

    if(prezzo_convertito < 1.295):
        avvisa()
    else:
        print("Prezzo non variato")

    print(prezzo_conVirgola)

def avvisa():
    print("Il prezzo è cambiato!")

while True:
    controlla_prezzo()
    time.sleep(60 * 60)