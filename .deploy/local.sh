#!/bin/bash
cd ../.docker
export PORT=8080
docker-compose build
docker-compose up -d

