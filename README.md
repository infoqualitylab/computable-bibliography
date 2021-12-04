# computable-bibliography
## Project Description  
The goal is to compute multidimensional bibliographies, where the dimensions include: title, journal name, publication year, issue, page number, authors. We will do this by gathering bibliographic data from various databases such as Scopus, Web of Science, Crossref, etc. The outcome ofthe project is to compute “relatedness” between any two bibliographies and form a “relatedness matrix”. This will be used in the future to contribute to tools that will assist in decision-making.  

## Steps to Run
    1. Store your file containing titles in the data folder  
    2. Get Scopus API Key and INST Token. Paste it in the config.json file  
    3. Run data_extraction.py file, Type in your filename without extension  
        example. for salt_controversy_title_only.csv type "salt_controversy_title_only" in terminal  
    4. Run computing-bibliography.ipynb file  

## Code Description  

### data_extraction.py
- This tool uses a set of titles from a bibliography, extracts their EIDs, and pulls the titles, abstracts, and references from Scopus for documents associated with that EID.
- We use elsapy to search for EIDs using titles which returns a JSON response.  
- From said response we extract EIDs to input to Elsevier’s AbstractRetrieval API which returns the bibliography.

### computing-bibliography.ipynb
- Using the data returned by the Data Collection tool we compute relatedness between any pair of reference items.  
- This relatedness is represented as a Relatedness Matrix where values range from 0 to 1.  
