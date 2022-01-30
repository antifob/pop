# pop

`pop` is an offensive payload generator designed for portability,
minimalism and efficiency.


## Usage

### Command line

```
pip install popsh
python -mpop -H
```

### Discord application

First, you'll have to decide on where to host the application. I
recommend Heroku and instructions are provided below.

First, register a bot following the instructions at
https://flask-discord-interactions.readthedocs.io/en/latest/botsetup.html

TODO env.rc

### Heroku

If you are deploying a Discord application, first register and prepare
the application by using the instructions above.

```
heroku apps create
heroku apps
git remote add heroku $APPNAME
sh ./tools/heroku-set-config.sh $APPNAME
git push heroku main
```

If you are deploying a Discord application, simply set the `Interaction
endpoint URL` to `https://$APPNAME.herokuapp.com/b/d`.
