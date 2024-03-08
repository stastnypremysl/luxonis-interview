FROM archlinux:latest

RUN pacman --noconfirm -Syu python postgresql scrapy python-psycopg2

COPY ./entrypoint /entrypoint
COPY ./scrape.py /scrape.py
COPY ./http-server.py /http-server.py

ENTRYPOINT /entrypoint
