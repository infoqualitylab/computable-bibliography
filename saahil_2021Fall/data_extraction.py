"""
    Citation Project v1
"""
import pandas as pd
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
import json
import csv
import requests
import time

def extract_data():
    """
    Extracts data from scopus based on title
    """
    # Reading a csv file containing titles
    df = pd.DataFrame(pd.read_csv("data/National Academies Report References.csv", header=0, quoting=csv.QUOTE_ALL))

    headers_dict = {"Accept": "application/json", "X-ELS-APIKey": config['apikey'],
                    "X-ELS-Insttoken": config['insttoken']}

    with open('data/extracted_scopus_data.csv', 'w', newline='', encoding='utf-8') as o:
        writer = csv.writer(o)
        writer.writerow(["Title", "Abstract", "Number of results", "Reference Titles"])
        for i in df.index:
            print(df.iloc[i, 0])
            doc_srch = ElsSearch(f'TITLE-ABS-KEY("{df.iloc[i, 0]}")', 'scopus')
            doc_srch.execute(client, get_all=False)
            print("doc_srch has", len(doc_srch.results), "results.")

            for res in doc_srch.results:
                response = requests.get(f"https://api.elsevier.com/content/abstract/eid/{res['eid']}",
                                        headers=headers_dict)

                references_titles = []
                if response.json()['abstracts-retrieval-response']['item']['bibrecord']['tail'] is not None:
                    references_list = response.json()['abstracts-retrieval-response']['item']['bibrecord']['tail']['bibliography']['reference']

                    for r in references_list:
                        if 'ref-title' in r['ref-info']:
                            references_titles.append(r['ref-info']['ref-title']['ref-titletext'])
                else:
                    references_titles.append(None)
                response_data = [
                    response.json()['abstracts-retrieval-response']['item']['bibrecord']['head']['citation-title'],
                    response.json()['abstracts-retrieval-response']['item']['bibrecord']['head']['abstracts'],
                    len(doc_srch.results),
                    references_titles]

                writer.writerows([response_data])


if __name__ == '__main__':
    # Load configuration
    con_file = open("config.json")
    config = json.load(con_file)
    con_file.close()

    # Initialize client
    client = ElsClient(config['apikey'])
    client.inst_token = config['insttoken']

    extract_data()


