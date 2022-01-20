#!/bin/bash
docker-compose -f coin_db/docker/docker-compose.yml up -d
docker-compose -f pipelines/BTCUSDT/docker-compose.yml up -d
docker-compose -f pipelines/DOGEUSDT/docker-compose.yml up -d
docker-compose -f pipelines/ETHUSDT/docker-compose.yml up -d
