FROM alpine:latest

RUN apk add --no-cache gcc \
                       musl-dev \
                       linux-headers \
                       python3 \
                       python-dev \
                       py-pip && \
    pip install --upgrade pip && \
    pip install psutil

ENV arguments ""

COPY metrics.py .
RUN chmod +x metrics.py

CMD ["sh", "-c", "./metrics.py ${arguments}"]