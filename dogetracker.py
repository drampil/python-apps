import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

page = requests.get("https://www.coindesk.com/price/dogecoin")
soup = BeautifulSoup(page.content, 'html.parser')

div = soup.find("div", {"class": "price-large"})

today = datetime.today()
d1 = today.strftime("%B %d %Y %H:%M:%S")
content =str(div)
numbers = re.sub('[^0-9+.]', '', content)
print("Dogecoin is currently: $",numbers)
print(d1)


f = open(r"C:\Users\XXXXXXXXXX\Desktop\dogecointracker.txt", "a")
print(numbers,"-", d1, file = f)
