#!/usr/bin/env bash

docker build -t test_task_lerkasan:latest .
docker run --name test_task_lerkasan --pid host --ipc host --rm -e arguments="mem disk cpu" -v /etc/passwd:/etc/passwd test_task_lerkasan:latest
#docker-compose up

# Uncomment this to clean up if needed
docker stop test_task_lerkasan
docker rm test_task_lerkasan
#docker rmi $(docker images | grep 'test_task_lerkasan')