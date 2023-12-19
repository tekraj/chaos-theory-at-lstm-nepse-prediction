FROM python:3.8-alpine
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers g++
COPY ./apps/symptom-detector/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
COPY ./apps/symptom-detector/ .
CMD ["python3", "./server.py"]
