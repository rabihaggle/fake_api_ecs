FROM python:3.11.6-alpine3.18

WORKDIR /app

COPY  ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./fake_api.py .

EXPOSE 8080

CMD [ "python","./fake_api.py" ]