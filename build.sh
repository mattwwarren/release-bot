#!/bin/bash -e
# Detect and error if these are not in the environment (maybe source a .env file)
export SLACK_SIGNING_SECRET=***
export SLACK_BOT_TOKEN=xoxb-***

pip install -r requirements.txt
uvicorn async_app:api --reload --port 3000 --log-level debug