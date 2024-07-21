# About
"""
Invoice reader
Acepcts a invoice or an image 
Image is converted into byte data and pass it into Gemmini llm model
response from the model is displayed

"""

# How to run file
create new environment--   conda create -p venv pyhton==3.10 

activate environment--     conda activate venv 

switch the command palette to current environment

install all the libraries --  pip install -r requiremnts.txt

create .env file add your Google gemmini api GOOGLE_API_KEY=""

streamlit run app.py