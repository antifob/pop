#!/bin/sh
set -eu

APP_NAME="${1}"

heroku config:set -a "${APP_NAME}" "POP_URL=https://${APP_NAME}.herokuapp.com/"
