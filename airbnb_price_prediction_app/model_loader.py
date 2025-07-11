import gdown
import pickle
import os

def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths
    model_path = os.path.join(base_dir, "model.pkl")
    columns_path = os.path.join(base_dir, "model_columns.pkl")

    # Download model if not present
    if not os.path.exists(model_path):
        gdown.download(
            "https://drive.google.com/uc?id=1zpa4zHZOm-Hk3zkUHKEGy-oUrmbX1nq5",
            model_path,
            quiet=False
        )

    # Download columns if not present
    if not os.path.exists(columns_path):
        gdown.download(
            "https://drive.google.com/uc?id=144QNun-eO1Tu0ZgE2POnN4rCe_c5nWxJ",
            columns_path,
            quiet=False
        )

    # Load both
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(columns_path, "rb") as f:
        model_columns = pickle.load(f)

    return model, model_columns
