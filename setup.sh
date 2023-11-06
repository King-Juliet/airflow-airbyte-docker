#!/usr/bin/env bash
up(){
# run airbyte using docker-compoe
cd airbyte
docker-compose up -d
#run airflow using docker-compose up
cd ../airflow
docker-compose up --build
#wait for dependencies to be loaded(adjust the sleep time as required)
sleep 180
#start up containers
docker-compose up -d
#wait for containers to start
sleep 180
#print instructions for accessing airbyte and airflow
echo "Airbyte is running on https://localhost:8000"
echo "Airflow is running on https://localhost:8080"
}

down(){
  # stop airbyte containers form running
  echo "Stopping airbyte....."
  cd airbyte
  docker-compose down
  #stop airflow containers from running
  echo "Stopping airflow...."
  cd ../airflow
  docker-compose down
}

case $1 in
  up)
    up
    ;;
  down)
    down
    ;;
  *)
    echo "Usage: $0 {up|down}"
    ;;
esac