FROM python:3.11-slim

WORKDIR /app

COPY checkAccess.py /app/
COPY printColors.py /app/
COPY textBox.py /app/
COPY buttonControl.py /app/
COPY jsCode.py /app/
COPY config.json /app/
COPY requirements.txt /app/
COPY app.log /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "checkAccess.py"]