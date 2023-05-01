FROM python:3.7-slim
RUN mkdir -p /opt/nlp/headline_generator
WORKDIR /opt/nlp/headline_generator
COPY main.py .
COPY utils.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python","main.py" ]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app