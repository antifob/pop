# pop

`pop` is an offensive payload generator designed for portability,
minimalism and efficiency. It is usable as a command-line tool,
a Web application and a Discord app.

Note that, depending on the payload generator, some dependencies might
have to be satisfied, first. For example, the `rt-go` module requires
the `go` binary to be available.


### Command-line tool

```
pip install popsh
pop -H
```


## Heroku

Deployment to Heroku, whether for the web UI or the Discord applcation
is quite simple. First, make sure you have an Heroku account and install
the command-line tool locally. Then, simply create an app with the
following command:

```
heroku apps:create
```

You'll be provided the randomly-generated identifier for the app. The
app's publicly reachable URL will be `https://APPID.herokuapp.com/`.

### Simple deployment (no dependencies)

When you're ready to deploy the app, simply move to the project's
repository and run the following command.

```
# first time only
git remote add heroku https://git.heroku.com/$APPNAME.git

# if deploying the Discord app (+ Web UI).
. ./env.rc
sh ./tools/heroku-set-config.sh $APPNAME

# deploy the app
git push heroku main
```

### Full deployment

To deploy the application with all modules available, first make sure
that `Docker` is available and run the following commands.

```
# Fetch the existing image
docker pull registry.gitlab.com/pgregoire/pop:latest

# Re-tag the image for Heroku
docker tag registry.gitlab.com/pgregoire/pop:latest registry.heroku.com/$APPNAME/web

# Login to the Heroku image registry
docker login --username=_ --password=$(heroku auth:token) registry.heroku.com

# Push the image to Heroku
docker push registry.heroku.com/$APPNAME/web

# Deploy the image/app
heroku container:release web
```


## Discord application

To make the application available to Discord users, you'll have to
register the application with Discord and deploy the application where
it will be publicly reachable.

Before proceeding, you need to have the publicly reachable URL of the
app in hand. The `Interactions endpoint URL` for the Discord bot will
be `$URL/b/d`.

Register a bot following the instructions at
https://flask-discord-interactions.readthedocs.io/en/latest/botsetup.html

If you plan on using the project's scripts to deploy the app, set the
following environment variables (they could be stored in `env.rc` for
convenience).

```
DISCORD_CLIENT_ID='123456789012345678'
DISCORD_PUBLIC_KEY='123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0'
DISCORD_CLIENT_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
DISCORD_GUILD_ID='123456789012345678'

export DISCORD_CLIENT_ID
export DISCORD_PUBLIC_KEY
export DISCORD_CLIENT_SECRET
export DISCORD_GUILD_ID
```
