#!/bin/bash
cd ../.docker
docker-compose -f docker-compose-ssl.yml build
docker-compose -f docker-compose-ssl.yml up -d

