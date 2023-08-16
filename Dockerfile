FROM python:3.8.11

ADD blockchain.py .
ADD run.py .

RUN pip install ecdsa datetime blake3

RUN apt-get update && apt-get install -y rustc cargo


CMD ["python", "./run.py"]


