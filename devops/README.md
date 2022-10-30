# Stop docker containers

```shell
docker stop $(docker ps -a -q --filter ancestor=ghcr.io/khitrovmaksim/students_frontend:latest --format="{{.ID}}")
docker stop $(docker ps -a -q --filter ancestor=ghcr.io/khitrovmaksim/students_backend:latest --format="{{.ID}}")
```