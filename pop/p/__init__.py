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

from glob import glob
from os.path import basename, dirname


class Encoder():
    def __init__(self, name):
        from importlib import import_module
        self.m = import_module('.{}'.format(name), __name__)
        del globals()[name]

    def __call__(self, pl):
        return self.m.enc(pl)


class Module():
    def rndstr(self, n=4):
        from random import choice
        from string import ascii_letters, digits

        r = choice(ascii_letters)

        for _ in range(n - 1):
            r += choice(ascii_letters + digits)

        return r

    def varrepl(self, s):
        for i in range(32):
            k = 'VAR{}'.format(i)
            s = s.replace(k, self.rndstr())

        return s

    def randnum(self):
        from random import random
        return int(random() * 10000)

    def numrepl(self, s):
        for i in range(32):
            k = 'NUM{}'.format(i)
            s = s.replace(k, str(self.randnum()))
        return s

    def argrepl(self, s, ARGS):
        args = ARGS[::]
        for i in range(1, 10):
            k = 'ARG{}'.format(i)
            if k not in s:
                continue
            p = ARGS[i - 1]
            if hasattr(self.pymod, 'tr'):
                p = self.pymod.tr(p, i)
            s = s.replace(k, p)

        if 'ARGN' in s:
            if 0 != len(ARGS[self.pymod.NARGS[0]:]):
                args = ARGS[self.pymod.NARGS[0]:]
                if hasattr(self.pymod, 'tr'):
                    args = [self.pymod.tr(a, 1) for a in args]
                s = s.replace('ARGN', ' ' + ' '.join(args))
            else:
                s = s.replace('ARGN', '')

        return s

    def repl(self, args, pl=None):
        pl = pl if pl else self.pymod.pl
        return self.numrepl(self.varrepl(self.argrepl(pl, args)))

    def __init__(self, name):
        from importlib import import_module
        keys = ['USAGE', 'LANG', 'NARGS', 'EXEC', 'pl']

        m = import_module('.{}'.format(name), __name__)
        assert(all([k for k in keys if getattr(m, k)]))
        del globals()[name]
        self.pymod = m

    def checkargs(self, a):
        n = self.pymod.NARGS
        if len(a) < n[0]:
            return -1
        elif 0 != n[1] and len(a) > n[1]:
            return 1
        return 0

    def __getattr__(self, k):
        r = None
        if k in dir(self.pymod):
            r = getattr(self.pymod, k)
        if k.upper() in dir(self.pymod):
            r = getattr(self.pymod, k.upper())

        if 'g' == k:
            if r is None:
                def r(args, encs):
                    if 0 > self.checkargs(args):
                        raise Exception('not enough arguments')
                    elif 0 < self.checkargs(args):
                        raise Exception('too many arguments')

                    t = self.repl(args)
                    for e in encs:
                        if self.pymod.LANG not in globals()['enc']:
                            raise Exception('Language has no encoder')
                        if e not in globals()['enc'][self.pymod.LANG]:
                            raise Exception('No encoder "{}" for language "{}"'.format(e, self.pymod.LANG))
                        t = globals()['enc'][self.pymod.LANG][e](t)
                        t = self.varrepl(t)
                    return t
            else:
                # atm, binaries don't have encoders
                def r(a, _):
                    return self.pymod.g(a)

        return r


for f in glob('{}/*.py'.format(dirname(__file__))):
    f = basename(f)[:-3]
    if '__init__' == f:
        continue

    n = f.split('-')[0]
    if n not in globals():
        globals()[n] = {}

    if 'enc' == n:
        n = f.split('-')[1]
        if n not in globals()['enc']:
            globals()['enc'][n] = {}
        globals()['enc'][n][f.split('-')[2]] = Encoder(f)

    else:
        n = '-'.join(f.split('-')[1:])
        globals()[f.split('-')[0]][n] = Module(f)


del globals()['glob']
del globals()['basename']
del globals()['dirname']
del globals()['Encoder']
del globals()['Module']
del globals()['f']
del globals()['n']
