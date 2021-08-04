# Question and answer generation web app
## Clone this repo
```bash
git clone https://github.com/elliotkantor/quiz-generation-web.git
cd quiz-generation-web
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
## Use the REST API
1. 
    ```bash
    uvicorn rest_api:app --reload
    ```
2. Now navigate to the localhost site listed in the terminal. Go to that site's `/docs` page, i.e. `localhost:5000/docs` to see documentation and try the methods out.
3. You can use this with the post method in python requests, i.e.:
    ```python
    import requests
    r = requests.post("localhost:8500", json={"text": "There are 5 apples in the box"})
    ```
4. The response is in the shape of:
    ```json
    [
        {
            "question": "How many apples are in the box?", 
            "answer": "5",
        },
    ]
    ```
## Credits
The pipelines software was taken from https://github.com/patil-suraj/question_generation, as allowed by the permissive MIT license.