from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
DATA_RAW_DIR = DATA_DIR / 'raw'
DATA_PROCESSED_DIR = DATA_DIR / 'processed'
MODELS_DIR = BASE_DIR / 'models'
SRC_DIR = BASE_DIR / 'src'

# Paths to data files
ARXIV_DATASET = DATA_RAW_DIR / 'arxiv.json'