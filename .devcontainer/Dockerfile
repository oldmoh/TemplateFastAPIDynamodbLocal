# Debian Bookworm ベースのイメージ
FROM python:3.10.14-bookworm
# DynamoDB Local がポート 8000 を使用するため、別のポートを公開
EXPOSE 8080

# Python の標準出力と標準エラー出力のバッファリングを無効化
ENV PYTHONUNBUFFERED 1
# タイムゾーンを JST-9 に設定
ENV TZ JST-9 

RUN pip3 install --upgrade pip

COPY ../requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
