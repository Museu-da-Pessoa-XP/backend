import string
import random

from museu.validators import ALLOWED_TYPES

TEST_PATH = 'tests/'


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def create_historias_data(num_historias, string_length=30):
    titles = [TEST_PATH + get_random_string(string_length) for i in range(num_historias)]
    descriptions = [get_random_string(string_length) for i in range(num_historias)]
    types = [random.choice(ALLOWED_TYPES) for i in range(num_historias)]
    media_urls = [get_random_string(string_length) for i in range(num_historias)]
    return titles, descriptions, types, media_urls
