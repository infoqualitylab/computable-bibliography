import json
import requests
import bibtexparser
import rispy
import pandas as pd
import xmltodict
from thefuzz import fuzz

def getdoi(author, title):
    title = title.replace(" ", "+")
    q = "https://api.crossref.org/works/?query.title=" + title + '&query.author='
    if (author != None and (type(author) == str or type(author) == list)):
        
        if (type(author) == list):
            q = q + author[0]
        else:
            q = q + author
        
        val = "Not Found"
        response = requests.get(q)
        if response.status_code == 200:
            x = json.loads(response.content.decode('utf-8'))['message']
            x = x['items']
            num = 0
            count = 0
            for i in x:
                count = count + 1
                num2 = fuzz.ratio(title, i['title'][0])
                if num2 > num:
                    num = num2
                    val = i['DOI']

                if count == 5:
                    break
                
        if num < 50:
            val = "Not Found"
            
        return val

    
def pubmedtodoi(id):
    q = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=' + str(id) + '&version=2.0'
    response = requests.get(q)
    val = "Not Found"
    if response.status_code == 200:
        x = response.content.decode('utf-8')
        x = xmltodict.parse(x)
        try:
            x = x['eSummaryResult']['DocumentSummarySet']['DocumentSummary']['ArticleIds']['ArticleId']
            for i in x:
                if i['IdType'] == "doi":
                    val = i['Value']
                    break

        except:
            return val

    return val


def bibtodf(input):
    y = open(input, "r", encoding = 'utf-8')
    y = y.read()
    y = bibtexparser.loads(y)
    df = pd.DataFrame(y.entries)
    return df

def ristodf(input):
    y = open(input, "r", encoding = "utf-8")
    y = rispy.load(y)
    df = pd.DataFrame(y)
    return df

def getdoifromcite(citation):
    q = "https://api.crossref.org/works/?query.bibliographic=" + citation
    val = "Not Found"
    response = requests.get(q)
    if response.status_code == 200:
        x = json.loads(response.content.decode('utf-8'))['message']
        val = x['items'][0]['DOI']
        
    return val