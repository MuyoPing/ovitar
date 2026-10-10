FROM python:3.11-slim
WORKDIR /app
COPY redirect.py /app/redirect.py
USER 65534:65534
CMD ["python", "redirect.py"]
