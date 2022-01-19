#!/bin/bash
docker-compose -f coin_db/docker/docker-compose.yml up -d
docker-compose -f pipelines/docker/docker-compose.yml up --build
