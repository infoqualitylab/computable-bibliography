import pandas as pd
import inputmodules

## Programatically aquire DOIS from author and title

csv_file = "csv-Calcitonin-set-filtered.csv"
df = pd.read_csv(csv_file, encoding = 'utf-8')
df = df.head(10)

df2 = pd.DataFrame()

df2['title'] = df.Title

doi = []
for i in range(len(df)):
    doi.append('')

df2['retreived doi'] = doi

for i in range (0, len(df)):
    author = df.loc[i, 'First Author']
    title = df.loc[i, 'Title']
    df2.loc[i, 'retreived doi'] = inputmodules.getdoi(author, title)

df2.to_csv('results/Title_to_DOI.csv')

## Programatically testing doi from PMID:

csv_file = "csv-Calcitonin-set-filtered.csv"
df = pd.read_csv(csv_file, encoding = 'utf-8')
df = df.head(10)
df2 = pd.DataFrame()

df2['pmid'] = df.PMID

doi = []
for i in range(len(df)):
    doi.append('')

df2['doi'] = doi

for i in range (0, len(df)):
    pmid = df.loc[i, 'PMID']
    df2.loc[i, 'doi'] = inputmodules.pubmedtodoi(pmid)

df2.to_csv('results/PMID_to_DOI.csv')

## Testing Bib and Ris conversion

inputmodules.bibtodf("Salt_SRRs.bib")
df2.to_csv('results/Salt_SRRs_bib.csv')

inputmodules.ristodf("Salt_SRRs.ris")
df2.to_csv('results/Salt_SRRs_ris.csv')

## Programatically retreiving DOIS from citations

csv_file = "csv-Calcitonin-set-filtered.csv"
df = pd.read_csv(csv_file, encoding = 'utf-8')
df = df.head(10)
df

df2 = pd.DataFrame()

df2['Citation'] = df.Citation

doi = []
for i in range(len(df)):
    doi.append('')

df2['retreived cite'] = doi

for i in range (0, len(df)):
    citation = df.loc[i, 'Citation']
    df2.loc[i, 'retreived cite']= inputmodules.getdoifromcite(citation)

df2.to_csv('results/Citation_to_DOI.csv')