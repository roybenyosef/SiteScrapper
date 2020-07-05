import argparse
import logging

from consts import BUILD_DB, CLEAR_DB, DOWNLOAD
import database

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('--mode', choices=[BUILD_DB, CLEAR_DB, DOWNLOAD], required=True, help='Mode of operation')
args = parser.parse_args()

mode_functions = { 
    BUILD_DB: database.create_db, 
    CLEAR_DB: database.clear_db,
    DOWNLOAD: None
}


def unknown_mode():
    logging.error('Unknown mode, aborting')


def main():
    logging.info('Welcome to SiteScrapper')
    mode_functions.get(args.mode, unknown_mode)()


if __name__ == "__main__":
    main()