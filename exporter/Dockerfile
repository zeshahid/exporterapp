FROM python:alpine
LABEL maintainer="zeeshanshahid"
WORKDIR /myapp
COPY requirements.txt .
COPY myapp.py /myapp
RUN cd /myapp && pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "/myapp/myapp.py"]
