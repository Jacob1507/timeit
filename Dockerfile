FROM python:3.13-alpine

WORKDIR /app

COPY . .
RUN pip install pip-tools && pip-sync

CMD ["python", "-m", "src.main"]
