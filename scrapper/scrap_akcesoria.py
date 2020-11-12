import requests
from bs4 import BeautifulSoup
from os.path  import basename
import csv
import pathlib

colors = ["czarny","biały","różowy","granatowy","niebieski","transparentny","żółty","czerwony","czarne","miętowy","przezroczyste","zielony","brązowy","brązowe"]
urltoCheck = ""

manufactures=[]
models= []
manufactureNameToSave = ""
modelNameToSave = ""
fileName = ""
urlTab = []

ids_tab = []
titles_tab = []
description_tab = []
price_tab = []
photos_tab = []

def containsColor(title):
    for color in colors:
        if color in title:
            return True
    return False

def deleteColorsFromTitle(title):
    for color in colors:
        if title.endswith(color) or title.endswith(color+" "):
            return title.replace(color,'')[:-3]
    return title
            
def addPhotos(title,photos):
    global photos_tab
    i=-1
    for name in titles_tab:
        i=i+1
        if name == title:
            photos_tab[i] = photos_tab[i] + ','+ photos
            return

def prepareSite(url,current_manufacture,current_model,numberOfSites):
    globals().update(urlTab = [])
    globals().update(urltoCheck = url)
    globals().update(manufactureNameToSave = current_manufacture)
    globals().update(modelNameToSave = current_model)
    for x in range(numberOfSites):
        urlTab.append(urltoCheck+str(x+1))  
    try:
        f = open(fileName)
    except IOError:
        with open(fileName, "a",newline='',encoding='utf-8') as f:
             writer = csv.writer(f, delimiter=';')
             writer.writerow(["Product ID","Active (0/1)","Name *","Categories (x,y,z...)","Price tax included","Tax rules ID",	"Wholesale price","On sale (0/1)","Discount amount","Discount percent","Discount from (yyyy-mm-dd)","Discount to (yyyy-mm-dd)","Supplier","Manufacturer","Quantity","Minimal quantity","Low stock level","Send me an email when the quantity is under this level","Visibility","Summary","Description","Meta title","URL rewritten","Text when in stock","Text when backorder allowed","Show price (0 = No, 1 = Yes)","Image URLs (x,y,z...)","Delete existing images (0 = No, 1 = Yes)","Condition","Customizable (0 = No, 1 = Yes)","Out of stock action","Available for order (0 = No, 1 = Yes)","Tags"])
        print("File not accessible")
    finally:
        f.close()
       
def writeData(url):
    r = requests.get(url)
    print(modelNameToSave)
    soup = BeautifulSoup(r.text.encode("utf-8"), "lxml")
    body = soup.body 
    productsHrefs = body.findAll('a',{'class':'offer__link'})

    for product in productsHrefs:
        productHref = product.get('href')
        print(productHref)
        if "zaprojektuj" in productHref:
            continue

        r = requests.get(productHref)
        soup = BeautifulSoup(r.text.encode("utf-8"), "lxml")
        body = soup.body 

        #photos
        photosUrl = ""
        photos = body.findAll('a',{'rel':'productimages'})
        for photo in photos:
            photosUrl = photosUrl+ photo.get('href') +','
        photosUrl = photosUrl[:-1]

        #name
        title = body.find('h1',{'itemprop':'name'}).text[17:-24]
        title_first = title
        title = deleteColorsFromTitle(title)
        print(title)
        check = containsColor(title_first)
        if title in titles_tab:
            if manufactureNameToSave == "Inna":
                continue
            addPhotos(title,photosUrl)
            continue

        titles_tab.append(title)
        photos_tab.append(photosUrl)

        #id
        id_number = body.find('input',{'name':'product_id'}).get('value')
        ids_tab.append(id_number)
        # #print(id_number)  
        description = body.find('div',{'itemprop':'description'})
        description_tab.append(description)
        # #print(description)
        price = body.find('span',{'itemprop':'price'}).text[9:-7].replace(',','.')
        price_tab.append(price)
        # #print(price)
        manufactures.append(manufactureNameToSave)
        models.append(modelNameToSave)

#etui
fileName = 'etui.csv'
ids_tab = []
titles_tab = []
description_tab = []
price_tab = []
photos_tab = []

#IPHONE
manufactureNameToSave = "Apple"
modelNameToSave = "iPhone SE 2020"
prepareSite('https://www.etuo.pl/etui-apple-iphone-se-2020?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 12"
prepareSite('https://www.etuo.pl/etui-apple-iphone-12?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 11"
prepareSite('https://www.etuo.pl/etui-apple-iphone-11?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 11 Pro"
prepareSite('https://www.etuo.pl/etui-apple-iphone-11-pro?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)   
modelNameToSave = "iPhone X"
prepareSite('https://www.etuo.pl/etui-apple-iphone-x?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)

#Samsung
manufactureNameToSave = "Samsung"
modelNameToSave = "Samsung Galaxy S20"
prepareSite('https://www.etuo.pl/etui-samsung-galaxy-s20?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S20 Ultra"
prepareSite('https://www.etuo.pl/etui-samsung-galaxy-s20-ultra?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S10"
prepareSite('https://www.etuo.pl/etui-samsung-galaxy-s10?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)

#Xiaomi
manufactureNameToSave = "Xiaomi"
modelNameToSave = "Xiaomi Mi 10"
prepareSite('https://www.etuo.pl/etui-xiaomi-mi-10?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "Xiaomi Mi 9"
prepareSite('https://www.etuo.pl/etui-xiaomi-mi-9?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)
modelNameToSave = "Xiaomi Redmi Note 8 Pro"
prepareSite('https://www.etuo.pl/etui-xiaomi-redmi-note-8-pro?p=',manufactureNameToSave,modelNameToSave,2)
for url in urlTab:
    writeData(url)

print(len(titles_tab))
with open(fileName, "a", newline='',encoding='utf-8') as f:        
    writer = csv.writer(f,delimiter=';')
    for i in range(len(titles_tab)):
        tags = "etui,ochrona,pokrowiec,"+manufactures[i]+","+models[i]+','+titles_tab[i].lower().replace(' ',',')[:-1]
        writer.writerow([ids_tab[i],1,titles_tab[i],'Etui i pokrowce/'+manufactures[i]+'/'+models[i],price_tab[i],1,price_tab[i],0,"","","","",manufactures[i],manufactures[i],100,1,10,0,"both","",description_tab[i],titles_tab[i],titles_tab[i].lower().replace(' ','-'),"Dostępny w magazynie.","Możliwy do zamówienia.",1,photos_tab[i],1,"new",0,"Chwilowo niedostępny",1,tags])


#szkla1
fileName = 'szkla1.csv'
ids_tab = []
titles_tab = []
description_tab = []
price_tab = []
photos_tab = []
doubletons = []
#Apple
manufactureNameToSave = "Apple"
modelNameToSave = "iPhone SE 2020"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-se-2020?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 11 Pro"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-11-pro?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 11 Pro Max"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-11-pro-max?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 12 Mini"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-12-mini?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 12 Pro"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-12-pro?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 12 Pro Max"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-12-pro-max?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
#Samsung
manufactureNameToSave = "Samsung"
modelNameToSave = "Samsung Galaxy S20 FE"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s20-fe?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S20 Plus"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s20-plus?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S10 Plus"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s10-plus?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S10 5G"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s10-5g?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S10e"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s10e?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S10 Lite"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s10-lite?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)

print(len(titles_tab))
with open(fileName, "a", newline='',encoding='utf-8') as f:        
    writer = csv.writer(f,delimiter=';')
    for i in range(len(titles_tab)):
        tags = "szklo,szkło,hartowane,szkła,szkla,"+manufactures[i]+","+models[i]+titles_tab[i].lower().replace(' ',',')[:-1]
        writer.writerow([ids_tab[i],1,titles_tab[i],'Szkła hartowane/'+manufactures[i]+'/'+models[i],price_tab[i],1,price_tab[i],0,"","","","",manufactures[i],manufactures[i],100,1,10,0,"both","",description_tab[i],titles_tab[i],titles_tab[i].lower().replace(' ','-'),"Dostępny w magazynie.","Możliwy do zamówienia.",1,photos_tab[i],1,"new",0,"Chwilowo niedostępny",1,tags])


#szkla
fileName = 'szkla1.csv'
ids_tab = []
titles_tab = []
description_tab = []
price_tab = []
photos_tab = []
doubletons = []
#Apple
manufactureNameToSave = "Apple"
modelNameToSave = "iPhone 12"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-12?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone 11"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-11?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "iPhone X"
prepareSite('https://www.etuo.pl/folie-szkla-apple-iphone-x?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
#Samsung
manufactureNameToSave = "Samsung"
modelNameToSave = "Samsung Galaxy S20"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s20?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S20 Ultra"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s20-ultra?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Samsung Galaxy S10"
prepareSite('https://www.etuo.pl/folie-szkla-samsung-galaxy-s10?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)

#Xiaomi
manufactureNameToSave = "Xiaomi"
modelNameToSave = "Xiaomi Mi 10"
prepareSite('https://www.etuo.pl/folie-szkla-xiaomi-mi-10?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Xiaomi Mi 9"
prepareSite('https://www.etuo.pl/folie-szkla-xiaomi-mi-9?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)
modelNameToSave = "Xiaomi Redmi Note 8 Pro"
prepareSite('https://www.etuo.pl/folie-szkla-xiaomi-redmi-note-8-pro?p=',manufactureNameToSave,modelNameToSave,1)
for url in urlTab:
    writeData(url)

print(len(titles_tab))
with open(fileName, "a", newline='',encoding='utf-8') as f:        
    writer = csv.writer(f,delimiter=';')
    for i in range(len(titles_tab)):
        tags = "szklo,szkło,hartowane,szkła,szkla,"+manufactures[i]+","+models[i]+titles_tab[i].lower().replace(' ',',')[:-1]
        writer.writerow([ids_tab[i],1,titles_tab[i],'Szkła hartowane/'+manufactures[i]+'/'+models[i],price_tab[i],1,price_tab[i],0,"","","","",manufactures[i],manufactures[i],100,1,10,0,"both","",description_tab[i],titles_tab[i],titles_tab[i].lower().replace(' ','-'),"Dostępny w magazynie.","Możliwy do zamówienia.",1,photos_tab[i],1,"new",0,"Chwilowo niedostępny",1,tags])

#Ładowarki
fileName = 'ladowarki.csv'
ids_tab = []
titles_tab = []
description_tab = []
price_tab = []
photos_tab = []
doubletons = []
#xiaomi
manufactureNameToSave = "Xiaomi"
modelNameToSave = ""
prepareSite('https://www.etuo.pl/ladowarki-xiaomi?p=',manufactureNameToSave,"",1)
for url in urlTab:
    writeData(url)
#samsung
manufactureNameToSave = "Samsung"
modelNameToSave = ""
prepareSite('https://www.etuo.pl/ladowarki-samsung?p=',manufactureNameToSave,"",1)
for url in urlTab:
    writeData(url)
#Apple
manufactureNameToSave = "Apple"
modelNameToSave = ""
prepareSite('https://www.etuo.pl/ladowarki-apple?p=',manufactureNameToSave,"",1)
for url in urlTab:
    writeData(url)
#inne
manufactureNameToSave = "Inna"
modelNameToSave = ""
prepareSite('https://www.etuo.pl/ladowarki?p=',manufactureNameToSave,"",1)
for url in urlTab:
    writeData(url)
    
print(len(titles_tab))
with open(fileName, "a", newline='',encoding='utf-8') as f:        
    writer = csv.writer(f,delimiter=';')
    for i in range(len(titles_tab)):
        tags = "ladowarki,ladowarka,ładowarki,ładowarka"+manufactures[i]+","+titles_tab[i].lower().replace(' ',',')[:-1]
        writer.writerow([ids_tab[i],1,titles_tab[i],'Ładowarki',price_tab[i],1,price_tab[i],0,"","","","",manufactures[i],manufactures[i],100,1,10,0,"both","",description_tab[i],titles_tab[i],titles_tab[i].lower().replace(' ','-'),"Dostępny w magazynie.","Możliwy do zamówienia.",1,photos_tab[i],1,"new",0,"Chwilowo niedostępny",1,tags])

#Kable
fileName = 'kable.csv'
ids_tab = []
titles_tab = []
description_tab = []
price_tab = []
photos_tab = []
doubletons = []

#inne
manufactureNameToSave = "Inna"
modelNameToSave = ""
prepareSite('https://www.etuo.pl/kable?p=',manufactureNameToSave,"",1)
for url in urlTab:
    writeData(url)
    
print(len(titles_tab))
with open(fileName, "a", newline='',encoding='utf-8') as f:        
    writer = csv.writer(f,delimiter=';')
    for i in range(len(titles_tab)):
        tags = "kabel,kable,"+manufactures[i]+titles_tab[i].lower().replace(' ',',')[:-1]
        
        writer.writerow([ids_tab[i],1,titles_tab[i],'Kable',price_tab[i],1,price_tab[i],0,"","","","",manufactures[i],manufactures[i],100,1,10,0,"both","",description_tab[i],titles_tab[i],titles_tab[i].lower().replace(' ','-'),"Dostępny w magazynie.","Możliwy do zamówienia.",1,photos_tab[i],1,"new",0,"Chwilowo niedostępny",1,tags])
