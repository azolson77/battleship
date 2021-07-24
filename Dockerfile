from alpine:latest
RUN apk add --no-cache py3-pip \
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app



EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
