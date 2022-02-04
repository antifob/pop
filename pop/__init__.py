#
# pop is an offensive payload generator
# Copyright 2021-2022 Philippe Grégoire <git@pgregoire.xyz>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from pop import p


def g(*args, **kwargs):
    if 2 > len(args):
        raise Exception('not enough arguments')

    t = getattr(p, args[0])
    if t is None:
        raise Exception('unknown payload type: {}'.format(args[0]))
    if args[1] not in t:
        raise Exception('unknown generator type: {}/{}'.format(*args[:2]))

    r = ''
    try:
        r = t[args[1]].g(args[2:], **kwargs).strip()
    except Exception as e:
        raise e

    return r


def rndstr(n=4):
    from random import choice
    from string import ascii_letters, digits

    r = choice(ascii_letters)

    for _ in range(n - 1):
        r += choice(ascii_letters + digits)

    return r


def main(app, *cargs):
    import os
    from pop.__main__ import main

    r = rndstr(8)
    d = os.path.join(app.config['POP_DESTDIR'], r)
    os.mkdir(d)
    u = os.environ['POP_URL'] + '/p/' + r + '/'

    return main(*cargs, dstdir=d, url=u)


def create_app():
    from flask import Flask, render_template, request, send_from_directory
    from os import environ

    app = Flask(__name__)
    app.config['POP_DESTDIR'] = environ['POP_DESTDIR']
    app.config['POP_URL'] = environ['POP_URL']

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/s/<path:path>')
    def spath(path):
        return send_from_directory('static', path)

    @app.route('/p/<path:path>')
    def ppath(path):
        return send_from_directory(app.config['POP_DESTDIR'], path)

    @app.route('/g', methods=['POST'])
    def gen():
        js = request.get_json(force=True)
        try:
            if type(js['c']) is list:
                return {'r': main(app, js['c'])}
            elif type(js['c']) is str:
                return {'r': main(app, js['c'].split())}
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
            o = main(app, args.split())
        except Exception as e:
            o = str(e)

        return '```\n{}\n```'.format(o.strip())

    discord.set_route('/b/d')

    if update_commands:
        discord.update_commands(guild_id=environ['DISCORD_GUILD_ID'])

    return app
