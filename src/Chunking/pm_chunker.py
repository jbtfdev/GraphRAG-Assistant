import re 
import os
import json
import spacy


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sentencizer")

def clean_text():
    with open("data/temp/Results.json", "r") as f:
        papers = json.load(f)
    for n in range(len(papers)):
        papers[n]["abstract"] = papers[n]['abstract'].replace("\n", " ").strip()
        papers[n]["abstract"] = papers[n]['abstract'].replace("\u00a0", " ").replace("\u2009", " ")
        papers[n]["abstract"] = papers[n]['abstract'].replace(" However,", ". However,")

        papers[n]['abstract'] = re.sub(r"<[^>]+>", "", papers[n]["abstract"])
        papers[n]['abstract'] = re.sub(r"\.(\S)", r". \1", papers[n]['abstract'])
        # papers[n]['abstract'] = re.split(r"(?<=\.)\s+(?=[A-Z])", papers[n]['abstract'])

    

    return papers


def med_chunk():
    papers = clean_text()
    for paper in papers:
        abstract = paper['abstract']
        doc = nlp(abstract)
        sentences = [sent.text for sent in doc.sents]

    chunks = []
    for paper in papers:
        pmid = paper["pmid"]
        title = paper['title']
        year = paper['year']
        mesh = paper['mesh_terms']
        for i, sent in enumerate(sentences):
            chunk = {
                "chunk_id": f"{pmid}_{i}",
                "text": sent,
                "pmid": pmid,
                "title": title,
                "year": year,
                "source": "pubmed" 
            }
            chunks.append(chunk)
    os.makedirs("data/processed", exist_ok=True)


    with open("data/processed/pubmed_chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    return chunks 


med_chunk()