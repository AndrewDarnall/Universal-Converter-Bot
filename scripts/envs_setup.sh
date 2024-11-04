#!/bin/bash

# Shell script for setting up the environment variables to run the bot

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <API_ID> <API_HASH> <BOT_TOKEN>"
  exit 1
fi

echo "export API_ID=$1" >> ~/.bashrc
echo "export API_HASH=$2" >> ~/.bashrc
echo "export BOT_TOKEN=$3" >> ~/.bashrc

source ~/.bashrc

echo "Environment variables set:"
echo "API_ID: $API_ID"
echo "API_HASH: $API_HASH"
echo "BOT_TOKEN: $BOT_TOKEN"
