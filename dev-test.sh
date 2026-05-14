#!/bin/bash

sudo docker compose down
sudo docker compose up --build
curl -X POST "http://127.0.0.1:9999/fraud-score" \
     -H "Content-Type: application/json" \
     -d '{"nome": "Victor Alex", "profissao": "Programador"}'