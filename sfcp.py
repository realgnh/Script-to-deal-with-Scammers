#THIS SCRIPT IS SUPPOSED TO BE USED AGAINST SCAM WEBSITES THAT ASK FOR YOUR CREDIT CARD INFO
#MORE INFO ABOUT IT IN THE 'README' TXT FILE


import requests
#to make the loop run faster
import threading

#HOW TO GET url in the 'README' txt
url = 'PASTE_THE_URL_HERE'

#HOW TO GET data in the 'README' txt
data = {
    'YOUR_DATA_HERE'
}

def requests():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

#this means there's 50 threads running at the same time in an infinite loop
for i in range(50):
    t = threading.Thread(target=requests)
    t.daemon = True
    threads.append(t)

#New loop to start thread
for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
