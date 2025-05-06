# Build stage
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/tasks || exit 1
CMD ["python", "app.py"]git add api
 
