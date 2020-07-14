import requests as req
import winsound as ws
import time
import threading

count = 0

def notify():
    global cond
    while cond:
        ws.Beep(500,500)
        time.sleep(0.2)
        print("Check result")
while True:
    try:
        cont = req.get("http://cbseresults.nic.in/")
        code = cont.status_code
        if code == 200:
            cond = True
            try:
                if count == 0:
                    count+=1
                    threading.Thread(target=notify).start()
                    
            except Exception as e:
                print(e)
                pass
            
        else:
            print("Server down, retrying...")
            cond = False
            count = 0

    except Exception as e:
        print(e)
