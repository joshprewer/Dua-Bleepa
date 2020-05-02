FROM python:3.6
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . /app
CMD streamlit run --server.port=5000 --server.enableCORS=false application.py