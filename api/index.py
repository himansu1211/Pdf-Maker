from app import main # We will wrap your code in a main() function
import os

# This bridges Streamlit with Vercel's serverless environment
if __name__ == "__main__":
    os.system("streamlit run app.py --server.port 8080 --server.address 0.0.0.0")