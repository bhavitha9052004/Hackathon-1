FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD automation.py /
CMD [ "python", "./main.py" ]