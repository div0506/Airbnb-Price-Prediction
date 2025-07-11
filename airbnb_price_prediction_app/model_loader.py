import gdown
import pickle

def load_model():
    url = "https://drive.google.com/uc?id=1zpa4zHZOm-Hk3zkUHKEGy-oUrmbX1nq5"
    output = "model.pkl"
    gdown.download(url, output, quiet=False)
    
    with open(output, "rb") as f:
        model = pickle.load(f)
    return model
