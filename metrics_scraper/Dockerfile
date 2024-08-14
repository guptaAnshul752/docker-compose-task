# Dockerfile for Building Metrics Scraper Image

FROM python:3.9-slim
COPY metric_scraper.py /opt/metrics/metric_scraper.py
RUN pip install flask psutil
EXPOSE 5000
CMD ["python3", "/opt/metrics/metric_scraper.py"]
