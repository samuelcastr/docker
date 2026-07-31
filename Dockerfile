FROM python
WORKDIR /home/myapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5050
CMD ["python", "sample_app.py"]