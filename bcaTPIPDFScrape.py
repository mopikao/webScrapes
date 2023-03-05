#!/usr/bin/python

# https://automatetheboringstuff.com/2e/chapter15/

# Downloading the PDF from BCA Website
# import requests
# bcaURL = "https://www1.bca.gov.sg/docs/default-source/docs-corp-form/free-stats.pdf"
# response = requests.get(bcaURL)
# with open('bcaTPI.pdf', 'wb') as f:
#     f.write(response.content)

# Reading the PDF
# https://stackoverflow.com/questions/51585444/tabula-py-omitting-pages-from-a-pdf-document-i-am-trying-to-extract
import tabula
import pandas
test_area = [430.0, 16.0, 490.0, 555.0]
tables = tabula.read_pdf('bcaTPI.pdf' ,pages="all", multiple_tables=False, area=test_area, silent=True)

#print(tables[0])
del tables[0][tables[0]. columns[0]]

tpiScraped = tables[0].transpose()
tpiScraped = tpiScraped.reset_index(drop=True)
tpiScraped.rename(columns={tpiScraped.columns[0]: 'Year', tpiScraped.columns[1]: 'TPI'}, inplace=True)
tpiScraped['Year'] = tpiScraped['Year'].astype(str).apply(lambda x: x.replace('.0',''))
print(tpiScraped)

# set up excel with pre-populated data
# Read excel to df
# concat df (pre-read) and new read
# look for duplicates and delete duplicates
# save back to excel
