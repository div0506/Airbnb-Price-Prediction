import gdown
import pickle
import os

# Only download if the file doesn't already exist
if not os.path.exists("model_columns.pkl"):
    gdown.download(
        "https://drive.google.com/uc?id=144QNun-eO1Tu0ZgE2POnN4rCe_c5nWxJ",
        "model_columns.pkl",
        quiet=False
    )

# Now load it
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)
