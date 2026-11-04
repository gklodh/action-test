FROM python:3.12-slim as Builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/package -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=builder /package /usr/local 
COPY . .
CMD ["python3","app.py"]
