import gdown
import pickle

# Download model_columns.pkl from Google Drive
gdown.download("https://drive.google.com/uc?id=144QNun-eO1Tu0ZgE2POnN4rCe_c5nWxJ", "model_columns.pkl", quiet=False)

# Load it
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)
