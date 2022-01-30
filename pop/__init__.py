
from pop import p
from pop.__main__ import main


def create_app():
    from flask import Flask, render_template, request, send_from_directory

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/s/<path:path>')
    def spath(path):
        return send_from_directory('static', path)

    @app.route('/g', methods=['POST'])
    def gen():
        js = request.get_json(force=True)
        if 'c' not in js:
            print('fail')
        try:
            if type(js['c']) is list:
                return {'r': main(js['c'])}
            elif type(js['c']) is str:
                return {'r': main(js['c'].split())}
            raise Exception('invalid argument')
        except Exception as e:
            return {'error': True, 'message': str(e)}

        return {'error': True, 'message': 'this should never happened'}

    return app


def create_bot(update_commands=False):
    import pop
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
