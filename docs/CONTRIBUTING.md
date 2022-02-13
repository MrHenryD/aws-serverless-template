# CONTRIBUTING

## Setup Environment
```
make build

docker-compose up --build
docker-compose down
```

## Add Packages
```
python3 -m poetry new app
python3 -m poetry install
python3 -m poetry add <package>

python3 -m poetry export -f requirements.txt --output requirements.txt
python3 -m poetry env info --path
```

## Run Tests
```
make test
```