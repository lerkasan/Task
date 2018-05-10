FROM alpine:latest

RUN apk add --no-cache gcc \
                       musl-dev \
                       linux-headers \
                       python3 \
                       python3-dev \
                       py3-pip && \
    pip3 install --upgrade pip && \
    pip3 install psutil

# PROCFS_PATH is used by psutils to calculate processes "read/write bytes" metric. Default value is "/proc"
# For docker container value "/host/proc" is set in Dockerfile because host /proc folder is mounted there
ENV PROCFS_PATH "/host/proc"
ENV arguments ""

COPY metrics .
RUN chmod +x metrics

CMD ["sh", "-c", "./metrics ${arguments}"]