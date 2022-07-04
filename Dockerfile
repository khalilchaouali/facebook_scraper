FROM python:3

WORKDIR /usr/src/

COPY requirements.txt /usr/src/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/

CMD ["python", "main.py"]