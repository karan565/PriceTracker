# your_app/tasks.py

from celery import shared_task
import time
import urllib.request as urllib2
from home.models import register
from bs4 import BeautifulSoup


@shared_task
def send_email_task():

    while True:
        data = register.objects.all()
        for x in data:
            name = x.name
            email = x.email
            phone = x.phone
            targetprice = x.targetprice
            link = x.link
            currentprice = float(pricefinder(link))
            print(link)
            if (currentprice > 0):
                if (currentprice <= targetprice):
                    # print(pricefinder(link))
                    message = f"Dear {name}, your product having link {link} has came down to a price point of ₹ {currentprice}"
                    twilio(phone, message)
                    x.delete()
                else:
                    tempmessage = f"Dear {name}, your product having link {link} sill have current price of ₹ {currentprice} which is above your targetted price of {targetprice}"
                    print(tempmessage)
            else:
                message = f"Dear {name}, you have provided an valid amazon product link hence we are deleting your request ! \n Your link : {link}"
                twilio(phone, message)
                x.delete()
        time.sleep(15)
        return
        # url = input("Enter url of the amazon product : ")
        url = "https://www.amazon.in/Luxury-Pen-Scriveiner-London-Professional/dp/B07YV85NNB/ref=sr_1_1?crid=2HIX1Z0EHG3X0&keywords=premium+ball+pens+for+men&qid=1688724911&rnid=2665398031&s=office&sprefix=premium+ballpens+for+men+%2Coffice-products%2C192&sr=1-1"
        targetedprice = float(input("Input targeted price for the product : "))
        currentprice = float(pricefinder(url))
        if (currentprice > 0):
            if (currentprice <= targetedprice):
                # print(pricefinder(url))
                message = f"Your product having link {url} has came down to a price point of ₹ {currentprice}"
                twilio("9558441976", message)
            else:
                message = f"Your product having link {url} sill have current price of ₹ {currentprice} which is above your targetted price of {targetedprice}"
            print(message)
        else:
            print("Please enter a valid amazon product link !")

    def doregistration(request):
        link = request.POST.get('link')
        # url = input("Enter url of the amazon product : ")
    #url = "https://www.amazon.in/Luxury-Pen-Scriveiner-London-Professional/dp/B07YV85NNB/ref=sr_1_1?crid=2HIX1Z0EHG3X0&keywords=premium+ball+pens+for+men&qid=1688724911&rnid=2665398031&s=office&sprefix=premium+ballpens+for+men+%2Coffice-products%2C192&sr=1-1"
    targetedprice = float(input("Input targeted price for the product : "))
    currentprice = float(pricefinder(url))
    if (currentprice > 0):
        if (currentprice <= targetedprice):
            # print(pricefinder(url))
            message = f"Your product having link {url} has came down to a price point of ₹ {currentprice}"
            twilio("9558441976", message)
        else:
            message = f"Your product having link {url} sill have current price of ₹ {currentprice} which is above your targetted price of {targetedprice}"
            print(message)
    else:
        print("Please enter a valid amazon product link !")


def pricefinder(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url)
    html_contents = response.read()
    # print(html_contents)
    soup = BeautifulSoup(html_contents, 'html.parser')
    try:
        price = soup.find(
            class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").get_text()
    except:
        return -1
    first_index = price.index("₹")
    # Get the index of the second occurrence of "₹"
    second_index = price.find("₹", first_index + 1)
    price = price[first_index + 1: second_index]
    price = float(price.replace(",", ""))
    if price > 0:
        return price
    else:
        return 0


def twilio(num, msg):
    pnum = ''
    msg2snd = ''
    pnum = '+91'+num
    msg2snd = msg
    from twilio.rest import Client
    sid = 'ACb37dba56c0153279701e9ce27f032f12'
    auth_token = '102c773c33c657f3588c199b5cc6ed25'
    client = Client(sid, auth_token)
    resp = client.messages.create(body=msg2snd, from_="+15734968196", to=pnum)
    print(num+"  :  "+msg)
    print(resp.sid)
