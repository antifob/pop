#!/bin/sh
set -eu

APP_NAME="${1}"

heroku config:set -a "${APP_NAME}" "DISCORD_CLIENT_ID=${DISCORD_CLIENT_ID}"
heroku config:set -a "${APP_NAME}" "DISCORD_CLIENT_SECRET=${DISCORD_CLIENT_SECRET}"
heroku config:set -a "${APP_NAME}" "DISCORD_PUBLIC_KEY=${DISCORD_PUBLIC_KEY}"
heroku config:set -a "${APP_NAME}" "DISCORD_GUILD_ID=${DISCORD_GUILD_ID}"
#heroku config:set -a "${APP_NAME}" 'PORT=33507'
