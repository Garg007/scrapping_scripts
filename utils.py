from random import randint
import time


SCRAPPER_SLEEP_MIN = 30  # in seconds
SCRAPPER_SLEEP_MAX = 60  # in seconds


def get_request_headers():
    """
    Function returns header for HTTP request

    Each call to this function has a User-Agent
    in header
    """

    # FIXME add more agent names later !!!
    agents = ['Mozilla/5.0', 'Safari/533.1', 'Chrome/33.0.1750.117']

    return {'User-Agent': agents[randint(0, len(agents)-1)]}


def get_rand_in_range(min, max):
    return randint(min, max)


def get_scrapper_sleep():
    return get_rand_in_range(SCRAPPER_SLEEP_MIN, SCRAPPER_SLEEP_MAX)


def sleep_scrapper(scrapper_name):
    val = get_scrapper_sleep()
    print "\n\n[%s] :: SLEEPING FOR %d seconds.....\n\n" % (scrapper_name, val)
    time.sleep(val)
    print "\n\n[%s] :: RESUMED \n\n" % scrapper_name
