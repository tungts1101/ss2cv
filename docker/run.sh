#!/bin/bash

ENV_MODE=${1:-dev}

if [ "$ENV_MODE" = "prod" ]; then
  ENV_FILE=".env.production"
else
  ENV_FILE=".env.development"
fi

echo "Docker uses $ENV_FILE"
set -a
. $ENV_FILE
set +a

echo "Docker starts services: $SERVICES"
docker compose --env-file $ENV_FILE up --build $SERVICES
