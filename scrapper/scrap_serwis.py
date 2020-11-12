import requests
from bs4 import BeautifulSoup
from os.path  import basename
import csv
import pathlib

def getIDNumberApple(title):
    number = 1079
    if title == "Naprawa iPhone 5S":
        return number
    elif title == "Naprawa iPhone 6":
        return number+1
    elif title == "Naprawa iPhone 6 Plus":
        return number+2
    elif title == "Naprawa iPhone 6S":
        return number+3
    elif title == "Naprawa iPhone 6S Plus":
        return number+4
    elif title == "Naprawa iPhone 7":
        return number+5
    elif title == "Naprawa iPhone 7 Plus":
        return number+6
    elif title == "Naprawa iPhone 8":
        return number+7
    elif title == "Naprawa iPhone 8 Plus":
        return number+8
    elif title == "Naprawa iPhone SE":
        return number+9
    elif title == "Naprawa iPhone X":
        return number+10
    else:    
        return 0

def getIDNumberSamsung(title):
    number = 1091
    if title == "Naprawa Galaxy S5 mini":
        return number
    elif title == "Naprawa Samsung Galaxy A10":
        return number+1
    elif title == "Naprawa Samsung Galaxy A20e":
        return number+2
    elif title == "Naprawa Samsung Galaxy A21s":
        return number+3
    elif title == "Naprawa Samsung Galaxy A3":
        return number+4
    elif title == "Naprawa Samsung Galaxy A3 2017":
        return number+5
    elif title == "Naprawa Samsung Galaxy A40":
        return number+6
    elif title == "Naprawa Samsung Galaxy A41":
        return number+7
    elif title == "Naprawa Samsung Galaxy A5":
        return number+8 
    elif title == "Naprawa Samsung Galaxy A5 2017":
        return number+9 
    elif title == "Naprawa Samsung Galaxy A50":
        return number+10 
    elif title == "Naprawa Samsung Galaxy A51":
        return number+11
    elif title == "Naprawa Samsung Galaxy A7":
        return number+12
    elif title == "Naprawa Samsung Galaxy A7 2018":
        return number+13
    elif title == "Naprawa Samsung Galaxy A70":
        return number+14
    elif title == "Naprawa Samsung Galaxy A71":
        return number+15
    elif title == "Naprawa Samsung Galaxy A8 2018":
        return number+16
    elif title == "Naprawa Samsung Galaxy J3":
        return number+17
    elif title == "Naprawa Samsung Galaxy J3 2017":
        return number+18
    elif title == "Naprawa Samsung Galaxy J4+":
        return number+19
    elif title == "Naprawa Samsung Galaxy J5":
        return number+20
    elif title == "Naprawa Samsung Galaxy J5 2017":
        return number+21
    elif title == "Naprawa Samsung Galaxy J6+":
        return number+22
    elif title == "Naprawa Samsung Galaxy J7":
        return number+23
    elif title == "Naprawa Samsung Galaxy J7 2017":
        return number+24
    elif title == "Naprawa Samsung Galaxy Note 8":
        return number+25
    elif title == "Naprawa Samsung Galaxy Note 9":
        return number+26
    elif title == "Naprawa Samsung Galaxy S10":
        return number+27
    elif title == "Naprawa Samsung Galaxy S10 Lite":
        return number+28
    elif title == "Naprawa Samsung Galaxy S10 Plus":
        return number+29
    else :
        return 0

def getIDNumberXiaomi(title):
    number = 1122
    if title == "Naprawa Xiaomi A2":
        return number
    elif title == "Naprawa Xiaomi A2 Lite":
        return number+1
    elif title == "Naprawa Xiaomi Mi 4C":
        return number+2
    elif title == "Naprawa Xiaomi Mi 6":
        return number+3
    elif title == "Naprawa Xiaomi Mi 9":
        return number+4
    elif title == "Naprawa Xiaomi Mi A1":
        return number+5
    elif title == "Naprawa Xiaomi Mi A2 Lite":
        return number+6
    elif title == "Naprawa Xiaomi Mi Max":
        return number+7
    elif title == "Naprawa Xiaomi Mi Max 2":
        return number+8 
    elif title == "Naprawa Xiaomi Mi Mix 2":
        return number+9 
    elif title == "Naprawa Xiaomi Mi Mix 2s":
        return number+10 
    elif title == "Naprawa Xiaomi Redmi 3 3S":
        return number+11
    elif title == "Naprawa Xiaomi Redmi 4A":
        return number+12
    elif title == "Naprawa Xiaomi Redmi 4X":
        return number+13
    elif title == "Naprawa Xiaomi Redmi 5 Plus":
        return number+14
    elif title == "Naprawa Xiaomi Redmi 6":
        return number+15
    elif title == "Naprawa Xiaomi Redmi 6A":
        return number+16
    elif title == "Naprawa Xiaomi Redmi 7":
        return number+17
    elif title == "Naprawa Xiaomi Redmi 7A":
        return number+18
    elif title == "Naprawa Xiaomi Redmi Note 2":
        return number+19
    elif title == "Naprawa Xiaomi Redmi Note 3":
        return number+20
    elif title == "Naprawa Xiaomi Redmi Note 3 Pro":
        return number+21
    elif title == "Naprawa Xiaomi Redmi Note 4":
        return number+22
    elif title == "Naprawa Xiaomi Redmi Note 4X":
        return number+23
    elif title == "Naprawa Xiaomi Redmi Note 5":
        return number+24
    elif title == "Naprawa Xiaomi Redmi Note 5 Pro":
        return number+25
    elif title == "Naprawa Xiaomi Redmi Note 5A":
        return number+26
    elif title == "Naprawa Xiaomi Redmi Note 7":
        return number+27
    elif title == "Naprawa Xiaomi Redmi Note 8":
        return number+28
    elif title == "Naprawa Xiaomi Redmi Note 8 Pro":
        return number+29
    else :
        return 0
        
def createFile(fileName):
    try:
        f = open(fileName)
    except IOError:
        with open(fileName, "a",newline='',encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Product ID","Active (0/1)","Name *","Categories (x,y,z...)","Price tax included","Tax rules ID",	"Wholesale price","On sale (0/1)","Discount amount","Discount percent","Discount from (yyyy-mm-dd)","Discount to (yyyy-mm-dd)","Supplier","Manufacturer","Quantity","Minimal quantity","Low stock level","Send me an email when the quantity is under this level","Visibility","Summary","Description","Meta title","URL rewritten","Text when in stock","Text when backorder allowed","Show price (0 = No, 1 = Yes)","Image URLs (x,y,z...)","Delete existing images (0 = No, 1 = Yes)","Condition","Customizable (0 = No, 1 = Yes)","Out of stock action","Available for order (0 = No, 1 = Yes)","Tags"])
        print("File not accessible")
    finally:
        f.close()

def writeData(url,fileName,manufacture):
    r = requests.get(url)
    soup = BeautifulSoup(r.text.encode("utf-8"), "lxml")
    body = soup.body 
    products = body.findAll('div',{'class':'content-product'})
    for product in products:
        productHref = product.a.get('href')
        #print(productHref)
        r = requests.get(productHref)
        soup = BeautifulSoup(r.text.encode("utf-8"), "lxml")
        body = soup.body 
        #title
        title = body.find('h1',{'itemprop':'name'}).text
        #price
        price = body.find('span',{'class':'woocommerce-Price-amount amount'}).text[:-3].replace(',','.')
        #summary
        summary = body.find('div',{'class':'woocommerce-product-details__short-description'}).text
        #description
        description = body.find('div',{'class':'tab-content-scroll'})
        #img
        photo = body.find('div',{'class','woocommerce-product-gallery__image'}).get('data-thumb')  
        ############ combination
        types = body.find('select',{'id':'pa_rodzaj-usterki'}).findAll('option')
        for repair in types:
            get_text = repair.text
            position_of_first_nawias = 0
            while get_text[position_of_first_nawias] is not '(':
                if position_of_first_nawias+1 >= len(get_text):
                    break
                position_of_first_nawias=position_of_first_nawias+1 
            position_of_second_nawias = 0
            while get_text[position_of_second_nawias] is not ')':
                if position_of_second_nawias+1>=len(get_text):
                    break
                position_of_second_nawias=position_of_second_nawias+1 
            repair_price = repair.text[position_of_first_nawias:position_of_second_nawias][1:-2]
            
            if repair_price is not "":
                repair_price = (float(repair_price)-float(price))/1.23
                with open("kombinacja_xiaomi.csv", "a",newline='',encoding='utf-8') as f:
                    writer = csv.writer(f, delimiter=';')
                    number = getIDNumberXiaomi(title)
                    writer.writerow([number,"Rodzaj naprawy:select:0",get_text+":0",100,"{:.2f}".format(repair_price),10,1,0])
            print(repair_price)
        ################### end
        # print(title)
        # print(price)
        # print(summary)
        # print(photo)

        with open(fileName, "a",newline='',encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            tags = "etui,ochrona,pokrowiec,"+"uBrokeIt,"+title.lower().replace(' ',',')[:-1]
            writer.writerow(["",1,title,'Serwis GSM/'+manufacture,price,1,price,0,"","","","","uBrokeIt","uBrokeIt",100,1,10,0,"both",summary,description,title,title.lower().replace(' ','-'),"Dostępny w magazynie.","Możliwy do zamówienia.",1,photo,1,"new",0,"Chwilowo niedostępny",1,tags])

with open("kombinacja_apple.csv", "a",newline='',encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Product ID*","Attribute (Name:Type:Position)*","Value (Value:Position)*","Wholesale price","Impact on price","Quantity","Minimal quantity","Low stock level"])        
fileName = "serwis_iphone.csv"
createFile(fileName)
writeData('https://telefonek.pl/kategoria/serwis-telefonow/naprawa-telefonu-apple/',fileName,'Apple')

with open("kombinacja_samsung.csv", "a",newline='',encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Product ID*","Attribute (Name:Type:Position)*","Value (Value:Position)*","Wholesale price","Impact on price","Quantity","Minimal quantity","Low stock level"])
fileName = "serwis_samsung.csv"
createFile(fileName)
writeData('https://telefonek.pl/kategoria/serwis-telefonow/naprawa-telefonu-samsung/',fileName,'Samsung')

with open("kombinacja_xiaomi.csv", "a",newline='',encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Product ID*","Attribute (Name:Type:Position)*","Value (Value:Position)*","Wholesale price","Impact on price","Quantity","Minimal quantity","Low stock level"])
fileName = "serwis_xiaomi.csv"
createFile(fileName)
writeData('https://telefonek.pl/kategoria/serwis-telefonow/naprawa-telefonu-xiaomi/',fileName,'Xiaomi')