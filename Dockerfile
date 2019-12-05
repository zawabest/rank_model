FROM python
COPY es-test.py /opt/es-test/
COPY tool/ /opt/es-test/tool/
COPY requirements.txt /tmp/
WORKDIR /opt/es-test
RUN pip install -r /tmp/requirements.txt
ENTRYPOINT ["python", "es-test.py"]
