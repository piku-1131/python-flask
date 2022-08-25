FROM python:3.7-slim-buster

WORKDIR /helloworld

COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

