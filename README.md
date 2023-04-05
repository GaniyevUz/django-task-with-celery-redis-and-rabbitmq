# Requirements
## Create Redis Container
```
docker run -d --name redis_container -p 6379:6379 redis:alpine
```

## Create Rabbitmq Container
```
docker run -d --name my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management 
```

## Create Postgres Container
```
docker run --name postgres_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=1 -d -p 5432:5432 postgres:alpine
```

## View Celery Tasks
  ```
  celery -A root worker -l info
```
