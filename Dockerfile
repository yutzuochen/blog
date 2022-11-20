FROM python:3.11.0
WORKDIR /docker_blog

RUN pip install Django~=4.1.0 Pillow==9.2.0 django-taggit==3.0.0

COPY . .