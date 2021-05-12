
from pop import p


def g(*args, encs=[]):
    if 2 >= len(args):
        raise Exception('not enough arguments')

    t = getattr(p, args[0])
    if t is None:
        raise Exception('unknown payload type: {}'.format(args[0]))
    if args[1] not in t:
        raise Exception('unknown generator type: {}/{}'.format(*args[:2]))

    r = ''
    try:
        r = t[args[1]].g(args[2:], encs).strip()
    except Exception as e:
        raise e

    return r


def ctree():
    r = {}
    for i in dir(p):
        if '_' in i or 'enc' == i:
            continue

        r[i] = {}
        m = getattr(p, i)
        for j in m:
            r[i][j] = m[j].USAGE

    return r


def create_app():
    from flask import Flask, render_template, request, send_from_directory

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', ctree=ctree())

    @app.route('/s/<path:path>')
    def spath(path):
        return send_from_directory('static', path)

    @app.route('/g', methods=['POST'])
    def gen():
        js = request.get_json(force=True)
        if 'c' not in js:
            print('fail')
        try:
            return {'r': g(*js['c'].split())}
        except Exception as e:
            return {'error': True, 'message': str(e)}

        return {'error': True, 'message': 'this should never happened'}

    return app


def create_bot(update_commands=False):
    import pop
    from pop.__main__ import main
    from os import environ

    from flask_discord_interactions import DiscordInteractions, CommandOptionType

    app = pop.create_app()
    discord = DiscordInteractions(app)
    app.config['DISCORD_CLIENT_ID'] = environ['DISCORD_CLIENT_ID']
    app.config['DISCORD_PUBLIC_KEY'] = environ['DISCORD_PUBLIC_KEY']
    app.config['DISCORD_CLIENT_SECRET'] = environ['DISCORD_CLIENT_SECRET']

    @discord.command(options=[{
        'name': 'args',
        'description': 'arguments to pass to pop',
        'type': CommandOptionType.STRING,
        'required': False,
    }])
    def pop(ctx, args=''):
        "generate a payload"
        try:
            o = main(args.split())
        except Exception as e:
            o = str(e)

        return '```\n{}\n```'.format(o)

    discord.set_route('/b/d')

    if update_commands:
        discord.update_commands(guild_id=environ['DISCORD_GUILD_ID'])

    return app
