#!/usr/bin/env bash

args = ""

for arg in "$@"
do
    args=${args}" "${arg}
done

docker build -t test_task_lerkasan:latest .

##Use privileged mode to see read/write bytes of host processes
docker run --privileged --name test_task_lerkasan --pid host --ipc host --rm -e arguments="${args}" \
           -v /etc/passwd:/etc/passwd:ro -v /proc:/host/proc:ro test_task_lerkasan:latest

# Alternative
#docker-compose run -e arguments="ps cpu mem disk" metrics

# Uncomment this to clean up if needed
docker stop test_task_lerkasan
docker rm test_task_lerkasan
docker rmi $(docker images | grep 'test_task_lerkasan')