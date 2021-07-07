FROM python:3
RUN mkdir -p /root/jfrog-ci/
WORKDIR /root/jfrog-ci/
COPY . /root/jfrog-ci/
RUN apt-get -y update
RUN pip3 install flask
EXPOSE 5000
CMD [ "python3", "app.py" ]
