#!/usr/bin/env python3
import os

import re
import sqlite3 as sql
import sys
import datetime
from configparser import ConfigParser


def load_config():
    parser = ConfigParser()
    parser.read('cookies.conf')
    return parser


def remove_all_cookies(path, config):
    print('===============================================\nREMOVING COOKIES IN PROFILE %s ON %s' % (path, datetime.datetime.now()))
    rules = [hostname.replace('.', r'\.').replace('*', '.*?') for hostname in [r.strip() for r in config['allowed_hosts'].split('\n') if r.strip()]]
    print('Connecting to database %s...' % path)
    try:
        conn = sql.connect(os.path.join(path, 'cookies.sqlite'))
        c = conn.cursor()
        ids = set()
        for row in c.execute("SELECT * FROM moz_cookies"):
            id_, host, *_ = row
            if not any(re.match(rule, host) for rule in rules):
                print('deleting cookie %s from' % id_, host)
                ids.add(id_)
        cmd = 'DELETE FROM moz_cookies WHERE id IN (%s)' % ','.join(map(str, ids))
        c.execute(cmd)
    except sql.OperationalError as e:
        print('Database Error: %s. Maybe next time...' % str(e))
    else:
        conn.commit()
        conn.close()

def main(*args):
    config = load_config()
    for path in config.sections():
        remove_all_cookies(path, config[path])


if __name__ == '__main__':
    main(sys.argv)
