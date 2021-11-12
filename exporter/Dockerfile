FROM pypy:slim

LABEL maintainer="zeeshanshahid"

EXPOSE 8000

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python myapp.py
