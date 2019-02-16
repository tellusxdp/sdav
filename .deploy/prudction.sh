#!/bin/bash
cd ../.docker
docker-compose -f docker-compose-ssl.yml build --no-cache
docker-compose -f docker-compose-ssl.yml up -d

