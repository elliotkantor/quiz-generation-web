# Question and answer generation web app
## Clone this repo
```bash
git clone https://github.com/elliotkantor/quiz-generation-web.git
```
## Install requirements
```bash
pip install -r requirements.txt
python -m nltk.downloader punkt
git clone https://github.com/patil-suraj/question_generation.git
```
## Run the script
```bash
streamlit run main.py
```
## Use the script
A website such as localhost:8501 should pop up in your default browser. Copy text into it and watch as machine learning generates questions and answers!
## Credits
The pipelines software was taken from https://github.com/patil-suraj/question_generation, as allowed by the permissive MIT license.