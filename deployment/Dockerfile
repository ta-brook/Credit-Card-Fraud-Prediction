# Use an official Python runtime as a parent image
FROM python:3.10-slim
WORKDIR /app
ADD deploy.py .
ADD models models
ADD requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 1150
CMD ["python", "deploy.py"]
