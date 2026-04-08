
import os 
import time
import json
from dotenv import load_dotenv
from Bio import Entrez

time.sleep(0.1)
load_dotenv()
api_key = os.getenv("pubmed_key")


Entrez.email = "anikettryk2@gmail.com"
Entrez.api_key = api_key

class Medinfo:
    def __init__(self,query,max_ids=25):
        self.query = query 
        self.max_ids = max_ids
    
    def search(self):
        handle = Entrez.esearch(
            db="pubmed",
            term=self.query,
            retmax=self.max_ids
        )

        record = Entrez.read(handle)
        handle.close()

        return record['IdList']
    
    def fetch(self,id_list):
        handle = Entrez.efetch(
            db="pubmed",
            id = ",".join(id_list),
            rettype = "abstract",
            retmode="xml"
        )

        data = Entrez.read(handle)
        handle.close()

        return data
    
    def parse(self, data):
        Pubmed_metadata = []

        for article in data['PubmedArticle']:

            citation = article['MedlineCitation']
            content = citation['Article']

            abstract_list = content.get('Abstract', {}).get('AbstractText', {})
            if not abstract_list:
                continue
            
            pmid = citation['PMID']
            title = content['ArticleTitle']
            year = content['Journal']['JournalIssue']['PubDate'].get('Year', 'N/A')
            mesh_terms = []
            if 'MeshHeadingList' in citation: 
                for mesh in citation['MeshHeadingList']:
        
                    term = mesh['DescriptorName']
                    mesh_terms.append(str(term))

            full_abstract = ""
            for part in abstract_list:
                labels = getattr(part, 'attribute', {}).get('Labels' , '')
                full_abstract += f"[{labels}] : {part} \n" if labels else f"{part} \n"

            paper_dict = {
                "pmid": pmid,
                "title": title,
                "abstract": full_abstract.strip(),
                "year": int(year),
                "mesh_terms": mesh_terms
            }
            Pubmed_metadata.append(paper_dict)

        return Pubmed_metadata

    







# medfo = Medinfo("insulin resistance mechanism")
# idlst = medfo.search()
# fetched = medfo.fetch(idlst)
# papers = medfo.parse(fetched)
# filename = "Results.json"

# with open(filename, "w", encoding="utf-8") as f:
#     json.dump(papers, f, indent=4)

# print(f"Success! Data SAVED TO {filename}") 