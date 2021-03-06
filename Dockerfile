FROM python:3.6.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY / .

CMD ["python","app.py"]