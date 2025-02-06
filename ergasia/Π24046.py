import requests
from bs4 import BeautifulSoup 
import json 
import os 

am= 'Π24046'
url = f'https://tma111.netlify.app/.netlify/functions/generate?id={am}'
quoteURL='https://dummyjson.com/quotes?limit=0'



quote_ids= []#δηλωση και αρχικοποίηση της λίστας quotes id
color = '000'#δηλωση και αρχικοποίηση του χρώματος ως μαύρο
bg_color = '000'#δηλωση και αρχικοποίηση ττου χρώματος background ως μαύρο
quotes = []

def isID(x):#Συνάρτηση που φιλτράρει τα lorem κομμάτια
    if x.isnumeric() or "Quote" in x or "ID:" in x:
        return True
    return False 
    

def numFinder(text):#συνάρτηση που παίρνει τον αριθμό από το κείμενο που δίνεται
    temp=''
    for char in text:
        if char.isdigit():
            temp += char

    return int(temp)



def Hashremover(text):#Αυτή η συνάρτηση αφαιρεί αυτό το χαρακτήρα(#) από ένα string
    temp=''
    for i in text:
        if i != '#':
            temp+=i
    return temp



def getImage(bgcolor , color , text , id1):#δημιουργεί τις εικόνες ή τις αλλάζει αν ήδη υπάρχουν
    print(text)
    imageurl = f'https://dummyjson.com/image/1200x200/{bgcolor}/{color}?text={text}'
    
    try:
        response = requests.get(imageurl)
        if response.status_code == 200:
            with open(f"{id1}.png", "wb") as f:
                f.write(response.content)
                f.close()

    except Exception as e:
        print(f'Whoops: {e}')



#1o ζητούμενο
try:
    r = requests.get(url)

    if r.status_code== 200:

        #1ο ζητούμενο

        doc= BeautifulSoup(r.text,'html.parser')


        TDs = doc.find_all('td')#βρισκει όλα τα κελια 
        IDs = []#εδω θα αποθηκευτούν τα κείμενα των κελιών
        for x in TDs:#αυτή η επανάληψη βγάζει τις ετικέτες <td> και εκχωρει τις τιμές των κελιών σε λίστα IDs
            IDs.append(x.text.strip())


        
        for x in IDs:#Αυτή η επανάληψη ελέγχει αν είναι quote id και τα προσθέτει στη λίστα quote_ids
            if isID(x):
                num = numFinder(x)
                quote_ids.append(num)


        quote_ids.sort()
        print(f'Τα quote ids είναι', quote_ids)    
        

        
        #Εδώ παίρνουμε τα χρώματα από την δυναμική ιστοσελίδα
        colors_finder = doc.find('div',{'id' : 'colors'})
        color_style_div = colors_finder.select_one('div[style]')
        color_style = color_style_div['style']
        
        #δημιουργείται dictionary με όλα τα στοιχεία του style attribute
        styles = dict(item.strip().split(": ", 1) for item in color_style.split(";") if item.strip())
        if styles:
            bg_color= styles.get('background-color')
            color = styles.get('color')

            bg_color= Hashremover(bg_color) #Αυτη η συνάρτηση έχει δηλωθεί πιο πάνω στο πρόγραμμα 
            color = Hashremover(color)

except Exception as e:
    print(f'whoops: {e}')



#2ο ζητούμενο
try:
    r2 = requests.get(quoteURL)

    if r2.status_code == 200:
        quotes= r2.json()
        
        #φιλτράρισμα των quotes με βάση το id και δημιουργία του quotes.json
        filtered_quotes = [quote for quote in quotes.get('quotes',[]) if quote['id'] in quote_ids]
        with open('quotes.json', 'w') as f:
            json.dump({'quotes':filtered_quotes} , f , indent=4)
except Exception as e:
    print(f'whoops: {e}')    




#3ο ζητούμενο
try:
    #Δημιουργία φακέλου quotes και δημιουργία των εικόνων σε αυτόν
    if not os.path.exists('quotes'):
        os.mkdir('quotes')

    os.chdir('quotes')

    
    for i in filtered_quotes:
        getImage(bg_color, color, i['quote'] , i['id'])
        

    os.chdir('..')
except Exception as e:
    print(f'whoops{e}')   


        