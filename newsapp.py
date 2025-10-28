import requests
import smtplib, ssl
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "useremail"
    password = "ennter the app password"
    reciver = "useremail"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context)as server:
        server.login(username,password)
        server.sendmail(username,reciver,message)

apikey="6ec16b98333e4f94b6e3f11b01f5d916"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6ec16b98333e4f94b6e3f11b01f5d916&language=en"
request = requests.get(url)
content = request.json()
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = "subject: Today's news"+"\n"+body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"]+  2*"\n"
body =body.encode("utf-8")
send_email(message = body)
t="studied"
