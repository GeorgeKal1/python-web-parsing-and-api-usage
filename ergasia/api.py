from fastapi import FastAPI, Query
import json

app = FastAPI()




@app.get('/')
def root():
    kati = {
        'quotes':'Για να δεις τα quotes ενός συγγραφέα πρόσθεσε στο λινκ το endpoint π.χ./quotes?author=Walt Disney',
        'Ολα τα quotes':'Για να δεις όλα τα quotes προσθεσε στο λινκ το endpoint /allquotes',
        'authors':'Για να δεις όλους τους authors προσθεσε στο λινκ το endpoint /authors'
    }
    return kati


@app.get("/quotes")#Εδώ γίνεται το endpoint /quotes?author="kapoios author"
async def get_quotes(author: str = Query(..., description="Name of the author")):
   
    try:
        with open("quotes.json", "r") as f:
            data = json.load(f)
            f.close()
        
        quotes = [quote for quote in data.get("quotes", []) if quote.get("author") == author]
        return quotes

    except Exception as e:
        return(f'whoops{e}')

#Έξτρα endpoints που δημιούργησα καθαρά για πειραματισμό
@app.get("/allquotes")
def get_authors():
    try:
        with open("quotes.json",'r') as f:
            data= json.load(f)
            f.close()


        allquotes = [quote for quote in data.get("quotes",[])]
        return  allquotes
    except Exception as e:
        return(f'whoops{e}')

@app.get("/authors")
def get_authors():#επιστρέφει ολους τους διαφορετικο΄ύς authors
    try:
        with open("quotes.json",'r') as f:
            data= json.load(f)
            f.close()

        authors= [quote.get('author') for quote in data.get("quotes",[])]
        allauthors = []
        for i in authors:
            if i not in allauthors:
                allauthors.append(i)

        return  allauthors
    except Exception as e:
        return(f'whoops{e}')

