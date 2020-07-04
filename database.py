from shutil import copyfile
import logging
import os
import time

from tinydb import TinyDB, Query


DB_FILE = 'db.json'
GAMES_TABLE_NAME = 'games_data'

db = TinyDB(DB_FILE, indent=4)
games_table = db.table(name=GAMES_TABLE_NAME)


def _backup_db():
    if not os.path.exists('db_backup'):
        os.makedirs('db_backup')
    copyfile(DB_FILE, f'db_backup//{DB_FILE}.{time.strftime("%Y%m%d-%H%M%S")}.backup')


def create_db():
    logging.info('Building Database')

    Game = Query()
    games_table.upsert({'int': 1, 'char': 'a'}, cond=Game.int == 1)

    _backup_db()


def clear_db():
    confirm = input('About to Delete Games Table, Enter "delete" to Confirm: ')
    if confirm == 'delete':
        db.drop_table(name=GAMES_TABLE_NAME)
        logging.info('Database Deleted')
    else:
        logging.info('Aborting Database Deletion')
