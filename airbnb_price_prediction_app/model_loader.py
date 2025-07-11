import gdown
import pickle
import os

def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths
    model_path = os.path.join(base_dir, "model.pkl")
    columns_path = os.path.join(base_dir, "model_columns.pkl")

    # Download model
    if not os.path.exists(model_path):
        gdown.download(
            "https://drive.google.com/uc?id=1zpa4zHZOm-Hk3zkUHKEGy-oUrmbX1nq5",
            model_path,
            quiet=False
        )

    # Download model_columns
    if not os.path.exists(columns_path):
        gdown.download(
            "https://drive.google.com/uc?id=144QNun-eO1Tu0ZgE2POnN4rCe_c5nWxJ",
            columns_path,
            quiet=False
        )

    # Load both files
    with open(model_path, "rb") as mf:
        model = pickle.load(mf)

    with open(columns_path, "rb") as cf:
        model_columns = pickle.load(cf)

    return model, model_columns
