import re
import json
import pandas as pd
from config import ARXIV_DATASET, CLEANED_ART, NUM_OF_ART


def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def main():
    papers = []
    with open(ARXIV_DATASET, 'r') as file:
        for i, line in enumerate(file):
            temp = json.loads(line)
            if i >= NUM_OF_ART:
                break
            papers.append(
                {
                    'id': temp['id'],
                    'title': clean_text(temp['title']),
                    'abstract': clean_text(temp['abstract']),
                    'year': temp['update_date'][:4],
                    'authors': temp['authors_parsed'],
                    'categories': temp['categories'],
                    'journal': temp['journal-ref']
                }
            )
    df = pd.DataFrame(papers)
    df.to_csv(CLEANED_ART, index=False)
    print(f"Succesfully saved {NUM_OF_ART} articles to {CLEANED_ART}")


if __name__ == '__main__':
    main()