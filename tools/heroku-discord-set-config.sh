#!/bin/sh
set -eu

PROGBASE=$(d=$(dirname -- "${0}"); cd "${d}" && pwd)


APP_NAME="${1}"

heroku config:set -a "${APP_NAME}" "DISCORD_CLIENT_ID=${DISCORD_CLIENT_ID}"
heroku config:set -a "${APP_NAME}" "DISCORD_CLIENT_SECRET=${DISCORD_CLIENT_SECRET}"
heroku config:set -a "${APP_NAME}" "DISCORD_PUBLIC_KEY=${DISCORD_PUBLIC_KEY}"
heroku config:set -a "${APP_NAME}" "DISCORD_GUILD_ID=${DISCORD_GUILD_ID}"

sh "${PROGBASE}/heroku-flask-set-config.sh" "${APP_NAME}"
