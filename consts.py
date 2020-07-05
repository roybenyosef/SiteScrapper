from urllib.parse import urljoin

BUILD_DB = 'build-db'
CLEAR_DB = 'clear-db'
DOWNLOAD = 'download'

BASE_URL = 'http://www.abandonia.com'
PAGE_URL_PATH = '/en/game/all?page=$page_number'
PAGE_FULL_URL = urljoin(BASE_URL, PAGE_URL_PATH)