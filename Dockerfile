FROM alpine:latest

RUN apk add --no-cache gcc \
                       musl-dev \
                       linux-headers \
                       python3 \
                       python3-dev \
                       py3-pip && \
    pip3 install --upgrade pip && \
    pip3 install psutil

#ARG arguments
ENV arguments ""
ENV PROCFS_PATH "/host/proc"

COPY metrics.py .
RUN chmod +x metrics.py

CMD ["sh", "-c", "./metrics.py ${arguments}"]