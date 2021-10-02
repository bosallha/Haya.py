try: 
 import requests,re 
except: 
 exit('\nDownload re & requests Please') 
print('\t<\> By k8-5o') 
print('\033[35m') 
 
bn = ''' 
                  
 D   A           T     A 
 
 ██░ ██  ▄▄▄     ▓██   ██▓ ▄▄▄       
▓██░ ██▒▒████▄    ▒██  ██▒▒████▄     
▒██▀▀██░▒██  ▀█▄   ▒██ ██░▒██  ▀█▄   
░▓█ ░██ ░██▄▄▄▄██  ░ ▐██▓░░██▄▄▄▄██  
░▓█▒░██▓ ▓█   ▓██▒ ░ ██▒▓░ ▓█   ▓██▒ 
 ▒ ░░▒░▒ ▒▒   ▓▒█░  ██▒▒▒  ▒▒   ▓▒█░ 
 ▒ ░▒░ ░  ▒   ▒▒ ░▓██ ░▒░   ▒   ▒▒ ░ 
 ░  ░░ ░  ░   ▒   ▒ ▒ ░░    ░   ▒    
 ░  ░  ░      ░  ░░ ░           ░  ░ 
                  ░ ░                
Snap : k8-5o  
Twiter : bosalha_ 
ــــــــــــــــــ 
Note: I am not responsible for your actions 
ــــــــــــــــــ 
 
 
 
 
 
 
 
 
 
''' 
 
 
print(bn) 
 
 
 
 
 
 
 
 
print('\033[37m') 
user=input('[?] user id : ') 
if user=="": 
 exit('[!] Enter a user id !!') 
else: 
 pass 
 
 
 
h={ 
 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',  
 'accept-language': 'ar,en-US;q=0.9,en;q=0.8',  
 'cache-control': 'max-age=0',  
 'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',  
 'sec-ch-ua-mobile': '?0',  
 'sec-ch-ua-platform': '"Windows"', 
 'sec-fetch-dest': 'document',  
 'sec-fetch-mode': 'navigate',  
 'sec-fetch-site': 'none',  
 'sec-fetch-user': '?1',  
 'upgrade-insecure-requests': '1',  
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'} 
 
 
 
 
try: 
 req=requests.get(f'https://hayah.co/api/v1//users/index?i_id={user}',headers=h) 
 Name=re.findall('"s_nickname":"(.*?)"',req.text)[0] 
 Email=re.findall('"s_email":"(.*?)"',req.text)[0] 
 print("[*] Done !")
 
 print('\033[32m') 
 print("")
 print('ــــــــــــــــــــــــ') 
 print("")
 print(f'[+] Email: {Email}') 
 print("")
 print('ــــــــــــــــــــــــ') 
 print("")
 print(f'[+] Name: {Name}') 
 print("")
 print('ــــــــــــــــــــــــ')
 print("")
 print('Phone Soon . . !')
 print("")
 print('ــــــــــــــــــــــــ')   
 print("")
 print('[\] Nice , Good Lack 🔭') 
 print('Snap k 8 - 5 o ') 
except: 
 exit('Not Found Email or phone or name')
