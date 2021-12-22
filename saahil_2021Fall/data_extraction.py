"""
    Making Bibliographies Computable
    - Independent Study by Saahil Hiranandani

    Packages needed to run:
    Pandas, elsapy (pip install elsapy), json, csv, requests

    Steps to run:
        1. Store your file containing titles in the data folder
        2. Get Scopus API Key and INST Token. Paste it in the config.json file
        3. Run data_extraction.py file, Type in your filename without extension
            example. for salt_controversy_title_only.csv type "salt_controversy_title_only" in terminal
        4. Run computing-bibliography.ipynb file

    Code Description:
        data_extraction.py
            This tool uses a set of titles from a bibliography, extracts their EIDs, and pulls the titles, abstracts,
            and references from Scopus for documents associated with that EID.
            We use elsapy to search for EIDs using titles which returns a JSON response.
            From said response we extract EIDs to input to Elsevier’s AbstractRetrieval API
            which returns the bibliography.

        computing-bibliography.ipynb
            Using the data returned by the Data Collection tool we compute relatedness
            between any pair of reference items.
            This relatedness is represented as a Relatedness Matrix where values range from 0 to 1.
"""
import pandas as pd
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
import json
import csv
import requests


def extract_data():
    """
    Extracts data from scopus based on title
    """
    # Reading a csv file containing titles
    print("Insert Filename Without Extension (File Should be a CSV file and should be placed in the data folder)")
    filename = input()
    df = pd.DataFrame(pd.read_csv(f"data/{filename}.csv", header=0, quoting=csv.QUOTE_ALL))

    headers_dict = {"Accept": "application/json", "X-ELS-APIKey": config['apikey'],
                    "X-ELS-Insttoken": config['insttoken']}

    with open('data/extracted_scopus_data.csv', 'w', newline='', encoding='utf-8') as o:
        writer = csv.writer(o)
        writer.writerow(["Title", "Abstract", "Number of results", "Reference Titles", "Authors"])
        for i in df.index:
            print(df.iloc[i, 0])

            # Using ELSAPY to do a Scopus search on TITLES which returns a JSON response
            # containing EIDs of those papers.

            doc_srch = ElsSearch(f'TITLE("{df.iloc[i, 0]}")', 'scopus')
            doc_srch.execute(client, get_all=False)
            print("doc_srch has", len(doc_srch.results), "results.")

            for res in doc_srch.results:
                if 'error' in res:
                    continue

                # Using those EIDs we have performed an API request to elsevier to get JSON data about the paper.
                # Can use the EID 2-s2.0-85084320421 and try sending a request
                # using postman or chrome to get sample response

                response = requests.get(f"https://api.elsevier.com/content/abstract/eid/{res['eid']}",
                                        headers=headers_dict)

                # Since References and Authors can be multiple for a paper, we cannot directly add them to our data
                references_titles = []
                author_names = []

                # Adding References to our data
                if response.json()['abstracts-retrieval-response']['item']['bibrecord']['tail'] is not None:
                    try:
                        references_list = response.json()['abstracts-retrieval-response']['item']['bibrecord']['tail']['bibliography']['reference']

                        for r in references_list:
                            try:
                                if 'ref-title' in r['ref-info']:
                                    # print(r['ref-info'])
                                    references_titles.append(r['ref-info']['ref-title']['ref-titletext'])
                            except TypeError:
                                continue
                    except KeyError:
                        continue
                # Adding Authors to our data
                if 'author-group' in response.json()['abstracts-retrieval-response']['item']['bibrecord']['head']:
                    author_groups = response.json()['abstracts-retrieval-response']['item']['bibrecord']['head']['author-group']
                    for ag in author_groups:
                        try:
                            if 'author' in ag:
                                authors = ag['author']
                                for a in authors:
                                    if 'ce:given-name' in a:
                                        author_names.append(a['preferred-name']['ce:given-name'] + " " + a['preferred-name']['ce:surname'])
                        except TypeError:
                            continue
                else:

                    # If not found append nothing
                    references_titles.append('')
                    author_names.append('')

                # This is our final data consisting of Titles, Abstracts,
                # Number of results returned after searching the title, References, and  Authors.
                response_data = [
                    response.json()['abstracts-retrieval-response']['item']['bibrecord']['head']['citation-title'],
                    response.json()['abstracts-retrieval-response']['item']['bibrecord']['head']['abstracts'],
                    len(doc_srch.results),
                    references_titles,
                    author_names]

                # Writing data to CSV
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


