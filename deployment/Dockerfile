# Use an official Python runtime as a parent image
FROM python:3.10-slim
WORKDIR /app
ADD deployment/deploy.py .
ADD deployment/model model
ADD deployment/requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 1150
CMD ["python", "deploy.py"]
