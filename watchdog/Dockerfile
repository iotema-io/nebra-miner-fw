FROM python:3.10.1-slim-buster
WORKDIR /usr/src/app
COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]