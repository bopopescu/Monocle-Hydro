import sys

from numbers import Number
from pathlib import Path
from datetime import datetime
from logging import getLogger

try:
    from . import config
except ImportError as e:
    raise ImportError('Please copy config.example.py to config.py and customize it.') from e

sequence = (tuple, list)
path = (str, Path)
set_sequence = (tuple, list, set, frozenset)
set_sequence_range = (tuple, list, range, set, frozenset)

worker_count = config.GRID[0] * config.GRID[1]
monocle_dir = Path(__file__).resolve().parents[1]

_valid_types = {
    'ACCOUNTS': set_sequence,
    'ACCOUNTS_CSV': path,
    'ACCOUNTS_SWAP_OUT_ON_WARN': bool,
    'ACCOUNTS_HIBERNATE_CONFIG': dict,
    'ALT_PRECISION': int,
    'ALT_RANGE': sequence,
    'ALWAYS_NOTIFY': int,
    'ALWAYS_NOTIFY_IDS': set_sequence_range,
    'ANNOUNCEMENTS': str,
    'APP_SIMULATION': bool,
    'AREA_NAME': str,
    'AUTHKEY': bytes,
    'BALANCE': str,
    'BOOTSTRAP_RADIUS': Number,
    'BOUNDARIES': object,
    'CACHE_CELLS': bool,
    'CAPTCHAS_ALLOWED': int,
    'CAPTCHA_KEY': str,
    'CLEANUP_LIMIT': int,
    'CLEANUP_RAIDS_OLDER_THAN_X_HR': Number,
    'CLEANUP_SIGHTINGS_OLDER_THAN_X_HR': Number,
    'CLEANUP_FORT_SIGHTINGS_OLDER_THAN_X_HR': Number,
    'CLEANUP_MYSTERY_SIGHTINGS_OLDER_THAN_X_HR': Number,
    'COMPLETE_TUTORIAL': bool,
    'COROUTINES_LIMIT': int,
    'DARK_MAP_OPACITY': Number,
    'DARK_MAP_PROVIDER_ATTRIBUTION': str,
    'DARK_MAP_PROVIDER_URL': str,
    'DB': dict,
    'DB_ENGINE': str,
    'DB_POOL_RECYCLE': Number,
    'DB_POOL_SIZE': Number,
    'DB_MAX_OVERFLOW': Number,
    'DIRECTORY': path,
    'DISCORD_INVITE_ID': str,
    'DISPLAY_BOOSTED_FEATURE': bool,
    'ENCOUNTER': str,
    'ENCOUNTER_IDS': set_sequence_range,
    'EXTRA_ACCOUNT_PERCENT': Number,
    'FAILURES_ALLOWED': int,
    'FAVOR_CAPTCHA': bool,
    'FB_PAGE_ID': str,
    'FIXED_OPACITY': bool,
    'FORCED_KILL': bool,
    'FORCE_SPLASH': bool,
    'FULL_TIME': Number,
    'FUNDING_GOAL': str,
    'GIVE_UP_KNOWN': Number,
    'GIVE_UP_UNKNOWN': Number,
    'GOOD_ENOUGH': Number,
    'GOOGLE_MAPS_KEY': (str,) + set_sequence,
    'GRID': sequence,
    'HASHTAGS': set_sequence,
    'HASH_KEY': (str,) + set_sequence,
    'HASH_ENDPOINT': str,
    'IV_NOTE': str,
    'GO_HASH': bool,
    'GOHASH_ENDPOINT': str,
    'GO_HASH_KEY': (str,) + set_sequence,
    'HEATMAP': bool,
    'HIBERNATE_WEBHOOK': str,
    'HIBERNATE_WEBHOOK_MIN_LEVEL': Number,
    'ICONS_URL': str,
    'EGG_ICONS_URL': str,
    'GMAP_ICONS_URL': str,
    'GMAP_EGG_ICONS_URL': str,
    'IGNORE_IVS': bool,
    'IGNORE_RARITY': bool,
    'IMAGE_STATS': bool,
    'INCUBATE_EGGS': bool,
    'INITIAL_SCORE': Number,
    'INSTANCE_ID': str,
    'ITEM_LIMITS': dict,
    'IV_FONT': str,
    'KEEP_GYM_HISTORY': bool,
    'KEEP_SPAWNPOINT_HISTORY': bool,
    'LANDMARKS': object,
    'LANGUAGE': str,
    'LAST_MIGRATION': Number,
    'LEGENDARY_RAID_POKEMON_ID': Number,
    'LEGENDARY_RAID_CP': Number,
    'LIGHT_MAP_OPACITY': Number,
    'LIGHT_MAP_PROVIDER_ATTRIBUTION': str,
    'LIGHT_MAP_PROVIDER_URL': str,
    'LOAD_CUSTOM_CSS_FILE': bool,
    'LOAD_CUSTOM_HTML_FILE': bool,
    'LOAD_CUSTOM_JS_FILE': bool,
    'LOGGED_FILES': Number,
    'LOGGED_SIZE': Number,
    'LOGIN_TIMEOUT': Number,
    'LV30_PERCENT_OF_WORKERS': Number,
    'LV30_ENCOUNTER_WAIT': Number,
    'LV30_GMO': bool,
    'LV30_MAX_QUEUE': int,
    'LV30_MAX_SPEED': Number,
    'MANAGER_ADDRESS': (str, tuple, list),
    'MAP_END': sequence,
    'MAP_FILTER_IDS': sequence,
    'MAP_PROVIDER_ATTRIBUTION': str,
    'MAP_PROVIDER_URL': str,
    'MAP_SHOW_DETAILS': bool,
    'MAP_START': sequence,
    'MAP_WORKERS': bool,
    'MAX_CAPTCHAS': int,
    'MAX_RETRIES': int,
    'MINIMUM_RUNTIME': Number,
    'MINIMUM_SCORE': Number,
    'MORE_POINTS': bool,
    'MOTD': str,
    'MOVE_FONT': str,
    'NAME_FONT': str,
    'NEVER_NOTIFY_IDS': set_sequence_range,
    'NO_DB_INSERT_IDS': set_sequence_range,
    'NOTIFY': bool,
    'NOTIFY_GYMS_WEBHOOK': bool,
    'NOTIFY_EGGS': bool,
    'NOTIFY_RAIDS': bool,
    'NOTIFY_RAIDS_WEBHOOK': bool,
    'NOTIFY_IDS': set_sequence_range,
    'NOTIFY_RANKING': int,
    'NOTIFY_WEATHER': bool,
    'PARK_CHECK': bool,
    'PASS': str,
    'PAYPAL_URL': str,
    'PAYPAL_BUTTON_CODE': str,
    'PB_API_KEY': str,
    'PB_CHANNEL': int,
    'PGSCOUT_ENDPOINT': set_sequence,
    'PGSCOUT_TIMEOUT': int,
    'PLAYER_LOCALE': dict,
    'POGOSD_REGION': str,
    'PROVIDER': str,
    'PROXIES': set_sequence,
    'PULL_GYM_NAME': bool,
    'RAIDERS_PER_GYM': Number,
    'POKEMON_ALARMS': dict,
    'DEFAULT_ALARM': dict,
    'RAIDS_FILTER': set_sequence_range,
    'TELEGRAM_RAIDS_FILTER': set_sequence_range,
    'TELEGRAM_RAIDS_LVL_MIN': int,
    'TELEGRAM_RAIDS_IDS': set_sequence_range,
    'RAID_ALARMS': dict,
    'DEFAULT_EGG_ALARM': dict,
    'DEFAULT_RAID_ALARM': dict,
    'RAID_IDS': set_sequence_range,
    'RARE_IDS': set_sequence_range,
    'RARITY_OVERRIDE': dict,
    'REFRESH_RATE': Number,
    'REPORT_MAPS': bool,
    'REPORT_SINCE': datetime,
    'RESCAN_UNKNOWN': Number,
    'SB_DETECTOR': bool,
    'SB_COMMON_POKEMON_IDS': set_sequence,
    'SB_MAX_ENC_MISS': Number,
    'SB_MIN_SIGHTING_COUNT': Number,
    'SB_QUARANTINE_VISITS': Number,
    'SCAN_DELAY': Number,
    'SCAN_LOG_WEBHOOK': str,
    'SEARCH_SLEEP': Number,
    'SHOW_FORM': bool,
    'SHOW_FORM_MENU_ITEM': bool,
    'SHOW_RAID_TIMER': bool,
    'SHOW_SPLASH': bool,
    'SPLASH_MESSAGE': str,
    'SHOW_TIMER': bool,
    'SHOW_TIMER_RAIDS': bool,
    'SHOW_IV': bool,
    'SHOW_EX_GYMS_BY_DEFAULT': bool,
    'SHOW_FILTERED_POKEMON_BY_DEFAULT': bool,
    'SHOW_PARKS_IN_S2_CELLS_BY_DEFAULT': bool,
    'SHOW_POKEMON_BY_DEFAULT': bool,
    'SHOW_GYMS_BY_DEFAULT': bool,
    'SHOW_RAIDS_BY_DEFAULT': bool,
    'SHOW_SCAN_AREA_BY_DEFAULT': bool,
    'SHOW_SPAWNPOINTS_BY_DEFAULT': bool,
    'SHOW_WEATHER_BY_DEFAULT': bool,
    'SIMULTANEOUS_LOGINS': int,
    'SIMULTANEOUS_SIMULATION': int,
    'SKIP_SPAWN': Number,
    'SMART_THROTTLE': Number,
    'SPEED_LIMIT': Number,
    'SPEED_UNIT': str,
    'SPIN_COOLDOWN': Number,
    'SPIN_POKESTOPS': bool,
    'GYM_NAMES': bool,
    'GYM_DEFENDERS': bool,
    'STAT_REFRESH': Number,
    'SWAP_OLDEST': Number,
    'TEAM': dict,
    'TELEGRAM_BOT_TOKEN': str,
    'TELEGRAM_CHAT_ID': str,
    'TELEGRAM_MESSAGE_TYPE': Number,
    'TELEGRAM_RAIDS_CHAT_ID': str,
    'TELEGRAM_USERNAME': str,
    'TICKER_ITEMS': str,
    'TICKER_COLOR': str,
    'TIME_REQUIRED': Number,
    'TRASH_IDS': set_sequence_range,
    'TWEET_IMAGES': bool,
    'TWITTER_ACCESS_KEY': str,
    'TWITTER_ACCESS_SECRET': str,
    'TWITTER_CONSUMER_KEY': str,
    'TWITTER_CONSUMER_SECRET': str,
    'TWITTER_SCREEN_NAME': str,
    'TZ_OFFSET': Number,
    'USE_ANTICAPTCHA': bool,
    'UVLOOP': bool,
    'WEBHOOKS': set_sequence,
    'WEATHER_STATUS': dict,
    'WEBHOOK_GYM_MAPPING': dict,
    'WEBHOOK_RAID_MAPPING': dict, 
}

_defaults = {
    'ACCOUNTS': None,
    'ACCOUNTS_CSV': None,
    'ACCOUNTS_SWAP_OUT_ON_WARN': True,
    'ACCOUNTS_HIBERNATE_CONFIG': {'banned': 45.0, 'warn': 45.0, 'sbanned': 45.0, 'code3': 45.0, 'tempdisabled': 0.02083333333},
    'ALT_PRECISION': 2,
    'ALT_RANGE': (300, 400),
    'ALWAYS_NOTIFY': 0,
    'ALWAYS_NOTIFY_IDS': set(),
    'ANNOUNCEMENTS': None,
    'APP_SIMULATION': True,
    'AREA_NAME': 'Area',
    'AUTHKEY': b'm3wtw0',
    'BALANCE': None,
    'BOOTSTRAP_RADIUS': 120,
    'BOUNDARIES': None,
    'CACHE_CELLS': False,
    'CAPTCHAS_ALLOWED': 3,
    'CAPTCHA_KEY': None,
    'CLEANUP_LIMIT': 100000,
    'CLEANUP_RAIDS_OLDER_THAN_X_HR': 4.0,
    'CLEANUP_SIGHTINGS_OLDER_THAN_X_HR': 4.0,
    'CLEANUP_FORT_SIGHTINGS_OLDER_THAN_X_HR': 4.0,
    'CLEANUP_MYSTERY_SIGHTINGS_OLDER_THAN_X_HR': 48.0,
    'COMPLETE_TUTORIAL': False,
    'CONTROL_SOCKS': None,
    'COROUTINES_LIMIT': worker_count,
    'DARK_MAP_OPACITY': 1.0,
    'DARK_MAP_PROVIDER_ATTRIBUTION': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    'DARK_MAP_PROVIDER_URL': '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'DB_POOL_RECYCLE': 299,
    'DB_POOL_SIZE': 5,
    'DB_MAX_OVERFLOW': 10,
    'DIRECTORY': '.',
    'DISCORD_INVITE_ID': None,
    'DISPLAY_BOOSTED_FEATURE': True,
    'ENCOUNTER': None,
    'ENCOUNTER_IDS': None,
    'EXTRA_ACCOUNT_PERCENT': 0.0,
    'FAVOR_CAPTCHA': True,
    'FAILURES_ALLOWED': 3,
    'FB_PAGE_ID': None,
    'FIXED_OPACITY': False,
    'FORCED_KILL': None,
    'FORCE_SPLASH': False,
    'FULL_TIME': 1800,
    'FUNDING_GOAL': None,
    'GIVE_UP_KNOWN': 300,
    'GIVE_UP_UNKNOWN': 1500,
    'GO_HASH': False,
    'GOHASH_ENDPOINT': 'http://hash.gomanager.biz',
    'HASH_ENDPOINT': 'http://pokehash.buddyauth.com',
    'GOOD_ENOUGH': 0.1,
    'GOOGLE_MAPS_KEY': '',
    'GYM_COOLDOWN': 300,
    'GYM_POINTS': False,
    'GYM_WEBHOOK': False,
    'HASHTAGS': None,
    'HIBERNATE_WEBHOOK': None,
    'HIBERNATE_WEBHOOK_MIN_LEVEL': 1,
    'ICONS_URL': "",
    'EGG_ICONS_URL': "https://raw.githubusercontent.com/M4d40/my-po-icons/master/Original-Assets/egg_{}.png",
    'GMAP_ICONS_URL': "https://raw.githubusercontent.com/M4d40/my-po-icons/master/Original-Assets-16x16/{}.png",
    'GMAP_EGG_ICONS_URL': "https://raw.githubusercontent.com/M4d40/my-po-icons/master/Original-Assets-16x16/egg_{}.png",
    'IGNORE_IVS': False,
    'IGNORE_RARITY': False,
    'IMAGE_STATS': False,
    'INCUBATE_EGGS': True,
    'INITIAL_RANKING': None,
    'INSTANCE_ID': str(monocle_dir),
    'ITEM_LIMITS': None,
    'IV_FONT': 'monospace',
    'IV_NOTE': None,
    'KEEP_GYM_HISTORY': False,
    'KEEP_SPAWNPOINT_HISTORY': True,
    'LANDMARKS': None,
    'LANGUAGE': 'EN',
    'LAST_MIGRATION': 1481932800,
    'LEGENDARY_RAID_POKEMON_ID': 0,
    'LEGENDARY_RAID_CP': 0,
    'LIGHT_MAP_OPACITY': 1.0,
    'LIGHT_MAP_PROVIDER_ATTRIBUTION': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    'LIGHT_MAP_PROVIDER_URL': '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'LOAD_CUSTOM_CSS_FILE': False,
    'LOAD_CUSTOM_HTML_FILE': False,
    'LOAD_CUSTOM_JS_FILE': False,
    'LOGGED_FILES': 4,
    'LOGGED_SIZE': 500000,
    'LOGIN_TIMEOUT': 2.5,
    'LV30_PERCENT_OF_WORKERS': 0.0,
    'LV30_ENCOUNTER_WAIT': 0.0,
    'LV30_GMO': False,
    'LV30_MAX_QUEUE': 0,
    'LV30_MAX_SPEED': 0.0,
    'MANAGER_ADDRESS': None,
    'MAP_FILTER_IDS': None,
    'MAP_PROVIDER_URL': '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'MAP_PROVIDER_ATTRIBUTION': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    'MAP_SHOW_DETAILS': True,
    'MAP_WORKERS': True,
    'MAX_CAPTCHAS': 0,
    'MAX_RETRIES': 3,
    'MINIMUM_RUNTIME': 10,
    'MORE_POINTS': False,
    'MOTD': None,
    'MOVE_FONT': 'sans-serif',
    'NAME_FONT': 'sans-serif',
    'NEVER_NOTIFY_IDS': (),
    'NO_DB_INSERT_IDS': None,
    'NOTIFY': False,
    'NOTIFY_GYMS_WEBHOOK': False,
    'NOTIFY_EGGS': False,
    'NOTIFY_RAIDS': False,
    'NOTIFY_RAIDS_WEBHOOK': True,
    'NOTIFY_IDS': None,
    'NOTIFY_RANKING': None,
    'PARK_CHECK': True,
    'NOTIFY_WEATHER': True,
    'PASS': None,
    'PAYPAL_URL': None,
    'PAYPAL_BUTTON_CODE': None,
    'PB_API_KEY': None,
    'PB_CHANNEL': None,
    'PGSCOUT_ENDPOINT': None,
    'PGSCOUT_TIMEOUT': 40,
    'PLAYER_LOCALE': {'country': 'US', 'language': 'en', 'timezone': 'America/Denver'},
    'PROVIDER': None,
    'PROXIES': None,
    'PULL_GYM_NAME': False,
    'RAIDERS_PER_GYM': 0.0,
    'POKEMON_ALARMS': {},
    'RAID_ALARMS': {},
    'RAIDS_FILTER': (3, 4, 5),
    'RAID_IDS': (),
    'TELEGRAM_RAIDS_FILTER': (3, 4, 5),
    'TELEGRAM_RAIDS_LVL_MIN': 4,
    'RAIDS_IDS': (),
    'RARE_IDS': (),
    'RARITY_OVERRIDE': {},
    'REFRESH_RATE': 0.6,
    'REPORT_MAPS': True,
    'REPORT_SINCE': None,
    'RESCAN_UNKNOWN': 90,
    'SB_DETECTOR': True,
    'SB_COMMON_POKEMON_IDS': (16,19,23,27,29,32,43,46,52,54,60,69,77,81,98,118,120,129,177,183,187,191,194,209,218,293,304,320,325,339),
    'SB_MAX_ENC_MISS': 3,
    'SB_MIN_SIGHTING_COUNT': 30,
    'SB_QUARANTINE_VISITS': 12,
    'SCAN_DELAY': 10,
    'SCAN_LOG_WEBHOOK': None,
    'SEARCH_SLEEP': 2.5,
    'SHOW_FORM': True,
    'SHOW_FORM_MENU_ITEM': False,
    'SHOW_RAID_TIMER': False,
    'SHOW_SPLASH': True,
    'SPLASH_MESSAGE': None,
    'SHOW_TIMER': False,
    'SHOW_IV': False,
    'SHOW_EX_GYMS_BY_DEFAULT': False,
    'SHOW_FILTERED_POKEMON_BY_DEFAULT': False,
    'SHOW_PARKS_IN_S2_CELLS_BY_DEFAULT': False,
    'SHOW_POKEMON_BY_DEFAULT': True,
    'SHOW_GYMS_BY_DEFAULT': False,
    'SHOW_RAIDS_BY_DEFAULT': False,
    'SHOW_SCAN_AREA_BY_DEFAULT': True,
    'SHOW_SPAWNPOINTS_BY_DEFAULT': False,
    'SHOW_WEATHER_BY_DEFAULT': False,
    'SHOW_TIMER_RAIDS': False,
    'SIMULTANEOUS_LOGINS': 2,
    'SIMULTANEOUS_SIMULATION': 4,
    'SKIP_SPAWN': 1500,
    'SMART_THROTTLE': False,
    'SPEED_LIMIT': 19.5,
    'SPEED_UNIT': 'miles',
    'SPIN_COOLDOWN': 300,
    'SPIN_POKESTOPS': True,
    'GYM_NAMES': True,
    'GYM_DEFENDERS': True,
    'STAT_REFRESH': 5,
    'SWAP_OLDEST': 21600 / worker_count,
    'TEAM': {0: "No Team", 1: "Mystic (blue)", 2: "Valor (red)", 3: "Instinct (yellow)"},
    'TELEGRAM_BOT_TOKEN': None,
    'TELEGRAM_CHAT_ID': None,
    'TELEGRAM_MESSAGE_TYPE': 0,
    'TELEGRAM_RAIDS_CHAT_ID': None,
    'TELEGRAM_USERNAME': None,
    'TICKER_ITEMS': None,
    'TICKER_COLOR': 'red',
    'TIME_REQUIRED': 300,
    'TRASH_IDS': (),
    'TWEET_IMAGES': False,
    'TWITTER_ACCESS_KEY': None,
    'TWITTER_ACCESS_SECRET': None,
    'TWITTER_CONSUMER_KEY': None,
    'TWITTER_CONSUMER_SECRET': None,
    'TWITTER_SCREEN_NAME': None,
    'TZ_OFFSET': None,
    'USE_ANTICAPTCHA': False,
    'UVLOOP': True,
    'WEBHOOK_GYM_MAPPING': {},
    'WEBHOOKS': None,
    'WEATHER_STATUS': {0: "Not boosted", 1: "Clear", 2: "Rainy", 3: "Partly Cloudy",
        4: "Overcast", 5: "Windy", 6: "Snow", 7: "Fog"},
    'WEBHOOK_RAID_MAPPING': {},
}


class Config:
    __spec__ = __spec__
    __slots__ = tuple(_valid_types.keys()) + ('log',)

    def __init__(self):
        self.log = getLogger('sanitizer')
        for key, value in (x for x in vars(config).items() if x[0].isupper()):
            try:
                if isinstance(value, _valid_types[key]):
                    setattr(self, key, value)
                    if key in _defaults:
                        del _defaults[key]
                elif key in _defaults and value is _defaults[key]:
                    setattr(self, key, _defaults.pop(key))
                else:
                    valid = _valid_types[key]
                    actual = type(value).__name__
                    if isinstance(valid, type):
                        err = '{} must be {}. Yours is: {}.'.format(
                            key, valid.__name__, actual)
                    else:
                        types = ', '.join((x.__name__ for x in valid))
                        err = '{} must be one of {}. Yours is: {}'.format(
                            key, types, actual)
                    raise TypeError(err)
            except KeyError:
                self.log.warning('{} is not a valid config option'.format(key))

    def __getattr__(self, name):
        try:
            default = _defaults.pop(name)
            setattr(self, name, default)
            return default
        except KeyError:
            if name == '__path__':
                return
            err = '{} not in config, and no default has been set.'.format(name)
            self.log.error(err)
            raise AttributeError(err)

sys.modules[__name__] = Config()

del _valid_types, config
