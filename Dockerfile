FROM python:3.11.6-slim

WORKDIR /app

COPY  ./fake_api.py .
COPY  ./rand_str.py .

COPY  ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 5000

CMD [ "python","./fake_api.py" ]