#!/usr/bin/env bash

args=""

# Concatenate all arguments into a string that will be passed as argument parameter to "docker run" command
# By default if no argument is provided script will show all possible metrics: processes, disk info, RAM and CPU usage
if [ $# -eq 0 ]
  then
    args="ps disk cpu mem"
else
    for arg in "$@"
    do
        args=${args}" "${arg}
    done
fi

docker build -t test_task_lerkasan:latest .

# Use privileged mode of docker run to see read/write bytes of host processes
# "--pid host" option is used to be able to see host processes inside docker container
# /etc/passwd file is mounted as volume to be able to see host usernames in process list inside docker container
# /proc folder is mounted to be able to get read/write in bytes metric of host processes
docker run --privileged --name test_task_lerkasan --pid host --rm -e arguments="${args}" \
           -v /etc/passwd:/etc/passwd:ro -v /proc:/host/proc:ro test_task_lerkasan:latest

# Alternative to docker run (requires installed docker-compose package)
#docker-compose build
#docker-compose run -e arguments="${args}" metrics

# Uncomment this to clean up if needed - to delete container and image
#docker stop test_task_lerkasan
#docker rm test_task_lerkasan
#docker rmi $(docker images | grep 'test_task_lerkasan')