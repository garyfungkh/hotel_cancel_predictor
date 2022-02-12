FROM python:3.9-bullseye

RUN pip install -r requirement.txt

COPY requirement.txt requirement.txt
COPY api_app/main.py main.py
COPY api_app/exported_classifier.pickle exported_classifier.pickle
COPY api_app/exported_one_hot.pickle exported_one_hot.pickle

CMD ["python3", "main.py"]