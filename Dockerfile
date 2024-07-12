# FROM python:3.7
# WORKDIR /usr/src/personalised_nudges
# COPY ./rutilea_app ./app
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# #CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

# Run the application
CMD ["uvicorn", "rutilea_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
