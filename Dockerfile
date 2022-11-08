FROM python:3.10
EXPOSE 5000
WORKDIR /wats
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_APP=basic.py
CMD ["flask", "run", "--host", "0.0.0.0"]