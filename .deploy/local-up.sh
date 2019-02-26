#!/bin/bash
cd ../.docker
export PORT=8080
docker-compose build --no-cache
docker-compose up -d

