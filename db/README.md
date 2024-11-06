
## DOCKER BUILD

```shell
docker build -t mysql-portafolio-db:1.0.0 .
```

## DOCKER RUN

```shell
docker run -d -p 10306:3306 --name mysql-portafolio-container  mysql-portafolio-db:1.0.0
```
