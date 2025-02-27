# python3.10.14 を含む Debian bookworm イメージ
FROM python:3.10.14-bookworm
# DynamoDB Local が 8000 を使用するので、別の port を使います
EXPOSE 8080

# Python の stdout と stderr のバッファリングを無効化させます。
ENV PYTHONUNBUFFERED 1
# タイムゾーン
ENV TZ JST-9 

RUN pip3 install --upgrade pip

COPY ../requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
