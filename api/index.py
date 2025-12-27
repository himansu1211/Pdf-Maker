from app import main 
import os

if __name__ == "__main__":

    os.system("streamlit run app.py --server.port 8080 --server.address 0.0.0.0")
