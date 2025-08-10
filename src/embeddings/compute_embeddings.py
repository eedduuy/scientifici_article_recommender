from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from config import CLEANED_ART, EMBEDDINGS, METADATA


def main():
    df = pd.read_csv(CLEANED_ART)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    abstracts = df['abstract'].tolist()

    embeddings = model.encode(abstracts, batch_size=64, show_progress_bar=True)
    np.save(EMBEDDINGS, embeddings)
    print(f"Successfully saved embeddings of shape {embeddings.shape} to {EMBEDDINGS}")

    metadata = df[['id', 'title', 'year', 'authors', 'categories', 'journal']]
    metadata.to_csv(METADATA, index=False)
    print(f"Successfully saved metadata to {METADATA}")

if __name__ == '__main__':
    main()
