FROM python:3.14.5-slim
WORKDIR /app
COPY ./config/requirements.txt ./
COPY ./app ./
COPY ./src ./

RUN pip install --no-cached-dir -r requirements.txt
CMD [ "uvicorn",  "main:app",  "--host", "0.0.0.0", "--port", "9999", "--reload" ]
EXPOSE 9999