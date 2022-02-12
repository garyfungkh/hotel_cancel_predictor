FROM python:3.9-bullseye

COPY requirement.txt requirement.txt
COPY api_app/main.py main.py
COPY exported_classifier.pickle exported_classifier.pickle
COPY exported_one_hot.pickle exported_one_hot.pickle

CMD ["python3", "main.py"]