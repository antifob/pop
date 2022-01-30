
import pop


def ls(name=None):
    o = ''

    o += '=> generators\n'
    for k in dir(pop.p):
        if '_' in k or 'enc' == k:
            continue
        if name is not None and k != name:
            continue

        t = getattr(pop.p, k).keys()
        if name is None:
            o += '  {}\t'.format(k)
        o += ' '.join(sorted(t)) + '\n'

    # TODO list supported encoders
    if name is not None and name:
        return o[:-1]

    o += '\n=> encoders\n'
    for k in pop.p.enc:
        if name is not None and k != name:
            continue

        t = getattr(pop.p, 'enc')[k].keys()
        if name is None:
            o += '  {}\t'.format(k)
        o += ' '.join(sorted(t)) + '\n'

    return o


def usage():
    u = 'pop [-Ehl] [-e encoder[,...]] type module [arg...]'
    return 'usage: {}'.format(u)


def main(args):
    from getopt import getopt, GetoptError

    opts, args = getopt(args, 'Ee:hl')

    o_encs = ''
    o_noex = True
    for k, v in opts:
        if '-E' == k:
            o_noex = False
        elif '-h' == k:
            return usage()
        elif '-l' == k:
            return ls()
        elif '-e' == k:
            o_encs = v

    if 0 == len(args):
        raise Exception(usage())
    if 1 == len(args):
        if args[0] not in dir(pop.p):
            raise Exception('error: unknown payload type ({})'.format(args[0]))
        return ls(args[0])

    if args[0] not in dir(pop.p):
        raise Exception('error: unknown payload type ({})'.format(args[0]))
    if args[1] not in getattr(pop.p, args[0]):
        raise Exception('error: unknown generator ({}/{})'.format(args[0], args[1]))

    m = getattr(pop.p, args[0])[args[1]]
    # if less than minargs or greater than maxargs
    if len(args[2:]) < m.nargs[0] or (len(args[2:]) > m.nargs[1] and m.nargs[1] >= m.nargs[0]):
        o = 'error: missing arguments\n'
        o += 'usage: {} {} {}'.format(args[0], args[1], m.usage)
        raise Exception(o)

    e = [e for e in o_encs.split(',') if e.strip()]
    pl = pop.g(*args, encs=e)
    if getattr(m, 'EXEC') and not o_noex:
        e = getattr(m, 'EXEC').strip()
        if e != 'PAYLOAD':
            e = e.replace('PAYLOAD', pl)
            e = m.repl(args[2:], e)
            pl += '\n\nexample:\n' + e

    return pl


if '__main__' == __name__:
    import sys

    try:
        print(main(sys.argv[1:]))
    except Exception as e:
        sys.stderr.write('{}\n'.format(e))
        exit(1)

    exit(0)
