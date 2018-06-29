import requests
for i in range(10):
    r = requests.get('http://www.sunat.gob.pe/cl-ti-itmrconsruc/captcha?accion=image')
    if r.status_code == 200:
        print(i+1,"Ok")
        img = r.content
        with open("new_sunat_captchas/"+str(i+1)+".jpeg", 'bw') as f:
            f.write(img)
    else:
        print(i+1,"Bad")
