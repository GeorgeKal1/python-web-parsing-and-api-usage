import matplotlib.pyplot as plt
import json




#αναγνώριση των διάφορων authors και μέτρηση των quotes τους
try:
    with open("quotes.json", "r") as f:
        data = json.load(f)
        f.close()

    
    
    allauthors = []#λίστα με τους μοναδικούς συγγραφείς
    quotescount = [] #δημιουργία λίστας με τον αριθμό quotes καθε συγγραφέα
    
    for quote in data.get("quotes",[]):
        author= quote.get("author")
        if author in allauthors:
            index = allauthors.index(author)
            quotescount[index]+=1
        else:
            allauthors.append(author)
            quotescount.append(1)

    #ταξινόμηση
    author_quote_list = list(zip(allauthors, quotescount))
    sorted_author_quote_list = sorted(author_quote_list, key=lambda x: x[1], reverse=True)
    allauthors, quotescount = zip(*sorted_author_quote_list)


     #Δημιουργία του πλότ
    plt.figure(figsize=(10,6))
    plt.bar(allauthors,quotescount,color='purple')
    plt.xlabel("Authors")
    plt.ylabel("quotes")
    plt.title("Quotes per author")
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.savefig("histogram.png",format='png')
    plt.show()
    
    
except Exception as e:
    print(f'whoops:{e}')
