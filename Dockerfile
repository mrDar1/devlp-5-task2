FROM python:3.13-alpine3.21
WORKDIR /app
EXPOSE 5000
COPY requirements.txt index.html .
RUN pip install --no-cache-dir -r requirements.txt && adduser -D -h /home/dduser dduser

USER dduser
COPY backend.py .

ENTRYPOINT ["python", "backend.py"]
