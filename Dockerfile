FROM python:3.9

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# # # RUN flask db init
# # # RUN flask db migrate -m "Initial migration"
# # # RUN flask db upgrade

EXPOSE 5000

CMD ["flask", "run"]
