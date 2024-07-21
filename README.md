# About
"""

Invoice Reader:

Accepts an invoice or an image.
Converts the image into byte data and passes it into the Gemini LLM model.
Displays the response from the model
 
"""

# How to run file
create new environment--   conda create -p venv pyhton==3.10 

activate environment--     conda activate venv 

switch the command palette to current environment

install all the libraries --  pip install -r requiremnts.txt

create .env file add your Google gemmini api GOOGLE_API_KEY=""

streamlit run app.py