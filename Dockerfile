FROM arm32v7/python:3.8-alpine
COPY . /app
WORKDIR /app
CMD python ./main.py