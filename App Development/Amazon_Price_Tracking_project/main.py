from bs4 import BeautifulSoup
from flask import Flask
from flask_mail import Mail, Message
import requests



app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "lathass199027@gmail.com",
    "MAIL_PASSWORD": "nxmfaxrodkysmpid"
}


parameters= {
             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
             "Accept-Language": "en-US,en;q=0.9"
}

AMAZON_URL ="https://www.amazon.com/Dash-Stand-Mixer-Electric-Everyday/dp/B00KW6F8V8/ref=sxin_17?asc_contentid=amzn1.osa.70390b26-d974-4366-9961-ebf0ee5196ec.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.70390b26-d974-4366-9961-ebf0ee5196ec.ATVPDKIKX0DER.en_US&content-id=amzn1.sym.c09abb10-336c-4c8f-b9f0-681fcf5f04dc%3Aamzn1.sym.c09abb10-336c-4c8f-b9f0-681fcf5f04dc&creativeASIN=B00KW6F8V8&crid=2YT2KH65MKRHJ&cv_ct_cx=mixer&cv_ct_id=amzn1.osa.70390b26-d974-4366-9961-ebf0ee5196ec.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&keywords=mixer&linkCode=oas&pd_rd_i=B00KW6F8V8&pd_rd_r=2057b3eb-336d-455a-b024-de4418c71204&pd_rd_w=1tkF1&pd_rd_wg=PGbBM&pf_rd_p=c09abb10-336c-4c8f-b9f0-681fcf5f04dc&pf_rd_r=M9E6ZDHTXDTFK07702JW&qid=1657872913&s=electronics&sprefix=mix%2Celectronics-intl-ship%2C166&sr=1-2-c26ac7f6-b43f-4741-a772-17cad7536576&tag=buyersguide0e-20&th=1"

response = requests.get(url=AMAZON_URL, headers=parameters)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

text = soup.find(name="span", class_="a-offscreen")
price_data = text.get_text()
price = float(price_data[1::])


app.config.update(mail_settings)
mail = Mail(app)
if price > 30:
    with app.app_context():
        message = f"The DASH Stand Mixer price is low. Please check {'AMAZON_URL'} for more information."
        msg = Message(subject=message,
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["lathaec8@gmail.com"],  # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)



