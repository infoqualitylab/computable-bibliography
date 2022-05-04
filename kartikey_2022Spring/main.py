

import pandas as pd
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
import json
import requests

path_input = "D:/MSIM - Coursework/Independent study/Input_Sample.csv"

inp_file = pd.read_csv(path_input)

new = []
lst = ["Publication Year", "Author" , "Title" , "Publication Title" , "ISBN", "ISSN" , "DOI" ,"Url", "Pages ", "Issue", "Volume"]


for col in inp_file.columns:
    if col in lst:
        new.append(col)
dfn = inp_file[new]
print("printing file", dfn.head())
dfn = dfn.reset_index()

# Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

# Initialize client
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']

pd.options.display.max_columns = None

for index, row in dfn.iterrows():

    doiv = row['DOI']
    doc_srch = ElsSearch(f'DOI({doiv})', 'scopus')
    doc_srch.execute(client, get_all=False)

    print()
    print("index", index)

    headers_dict = {"Accept": "application/json", "X-ELS-APIKey": config['apikey'],
                    "X-ELS-Insttoken": config['insttoken']}

    try:

        response = requests.get(f"https://api.elsevier.com/content/abstract/eid/{doc_srch.results[0]['eid']}",
                                headers=headers_dict)

        jsonResponse = response.json()
        #         print(jsonResponse)

        loop = 0
        for k, v in jsonResponse.items():
            print(f"KEY: {k},        ")
            print()

        df = pd.json_normalize(
            jsonResponse['abstracts-retrieval-response']['item']['bibrecord']['tail']['bibliography']['reference'])
        #         for each in doc_srch.results:
        #             print("TITLE IS : " ,each["dc:title"])
        print("title is : ", jsonResponse["abstracts-retrieval-response"]["item"]["bibrecord"]["head"]["citation-title"])

        # df = df.explode('abstracts-retrieval-response.item.bibrecord.tail.bibliography.reference')

        #         print(jsonResponse['abstracts-retrieval-response']['item']['bibrecord']['tail']['bibliography']['reference'][0][])

        #         for col in df.columns:
        #             print(col)

        df.to_csv('data/{}.csv'.format(jsonResponse["abstracts-retrieval-response"]["item"]["bibrecord"]["head"]["citation-title"][0:40]), encoding='utf-8')
        print()

    except Exception as e:
        # print(" skipped {}".format(jsonResponse["abstracts-retrieval-response"]["item"]["bibrecord"]["head"]["citation-title"]))
        print("skipped  :  ", row)
        # print(" content : ", jsonResponse["abstracts-retrieval-response"]["item"]["bibrecord"]["head"])
        print("Reason   :  ",e)
        # exit()



