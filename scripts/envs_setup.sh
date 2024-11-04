#!/bin/bash

# Shell script for setting up the environment variables to run the bot

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <API_ID> <API_HASH> <BOT_TOKEN>"
  exit 1
fi

export API_ID=$1 | sudo tee -a /etc/environment
export API_HASH=$2 | sudo tee -a /etc/environment
export BOT_TOKEN=$3 | sudo tee -a /etc/environment

source /etc/environment

echo "Environment variables set:"
echo "API_ID: $API_ID"
echo "API_HASH: $API_HASH"
echo "BOT_TOKEN: $BOT_TOKEN"
