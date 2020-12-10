import string
import random
from io import BytesIO

from museu.models import Tag
from museu.validators import ALLOWED_TYPES

TEST_PATH = 'tests/'
EMAIL_DOMAIN = 'email.com'


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def get_random_number(length):
    numbers = string.digits
    result_number = ''.join(random.choice(numbers) for i in range(length))
    return result_number


def create_historias_data(num_historias=10, string_length=30, num_tags=5, is_model=True):
    titles = [TEST_PATH + get_random_string(string_length) for i in range(num_historias)]
    tags = [[get_random_string(string_length) for j in range(num_tags)] \
            for i in range(num_historias)]
    types = [random.choice(ALLOWED_TYPES) for i in range(num_historias)]
    if is_model:
        media_urls = [get_random_string(string_length) for i in range(num_historias)]
        return titles, tags, types, media_urls
    media = [create_file() for i in range(num_historias)]
    return titles, tags, types, media

def create_users_data(num_users=5, string_length=30, number_length=11):
    name = [get_random_string(string_length) for i in range(num_users)]
    email = [get_random_string(string_length)+'@'+EMAIL_DOMAIN for i in range(num_users)]
    phone = [get_random_number(number_length) for i in range(num_users)]
    return name, email, phone

def save_tags(tags):
    tag_objs = []
    for tag in tags:
        tag_obj = Tag.objects.create(tag=tag)
        tag_obj.save()
        tag_objs.append(tag_obj)
    return tag_objs

def create_file():
    file = BytesIO(b'Test File content')
    file.seek(0)
    return file
