# Making Bibliographies Computable 
## Project Description  
The goal is to extract complete bibliography of each scholarly document(e.g. - research papers, conference paper, articles etc). This will be used in the future to calculate co-citation strength and apply social network analysis and other data mining techniques to detect biases in the research papers. This tool will assist policy makers and grant reviwers in decision-making.  

## Definitions:  

Bibliography: - Simply put, a bibliography is a list of references that is created at the end of your research paper. This resource discusses either all the sources that were used to create the work or just those that were cited in the work [1] 

Scholarly Document: - Any article, research paper, conference paper or similar document. 


## Steps to Run
    1. Write the path of the input excel file in the variable path_input in file main.py 
    2. Get Scopus API Key and INST Token. Paste it in the config.json file  
    3. The script searches each scholarly document by DOI and extract its bibliography.   
    4. If the script is unable to locate the document in the SCOPUS database by DOI then it skips the document and prints the input row and the error(printed on screen as “reason: ”) for failure. 
    5. The bibliography of each document is saved in individual excel files.The names of the excel files are the titles of the scholarly documents in the excel files. 

## Code Description  

### main.py
- This tool uses a set of DOIs from a bibliography, extracts their EIDs, and pulls their complete bibliography including titles, abstracts, ItemID and other details from Scopus for documents associated with that DOI.
- We use elsapy to search for EIDs using DOIs which returns a XML response.  
- From said response we extract EIDs to input to Elsevier’s AbstractRetrieval API which returns the bibliography.
  
