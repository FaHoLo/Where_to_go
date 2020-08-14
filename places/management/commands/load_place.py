from tempfile import NamedTemporaryFile, _TemporaryFileWrapper
import traceback

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
import requests
from slugify import slugify

from places.models import Place, Location, Image


class Command(BaseCommand):
    help = 'Load new loaction from url: http://file/url.json'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options['urls']:
            try:
                data = download_json_data(url)
                place = create_place(data)
                upload_place_images(place, data['imgs'])
                location = create_location(data, place)

                self.stdout.write(self.style.SUCCESS(
                    'Successfully added Place: {place_id}, Location: {location_title}'.format(
                        place_id=place.id, location_title=location.title
                    )
                ))
            except Exception:
                raise CommandError(
                    f'Got an exception while parsing url:\n{url}\n{traceback.format_exc()}'
                )


def download_json_data(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_place(data: dict) -> Place:
    place = Place.objects.get_or_create(
        title=data['title'],
        description_short=data['description_short'],
        description_long=data['description_long'],
        lat=data['coordinates']['lat'],
        lng=data['coordinates']['lng'],
    )[0]
    return place


def upload_place_images(place: Place, image_urls: dict) -> None:
    for image_number, image_url in enumerate(image_urls):
        image_obj = Image.objects.get_or_create(place=place, image_number=image_number+1)[0]
        image_name = image_url.split('/')[-1]
        image = download_image(image_url)
        temp_img = create_temporary_file(image)
        image_obj.image.save(image_name, File(temp_img))


def download_image(img_url: str) -> bytes:
    response = requests.get(img_url)
    response.raise_for_status()
    return response.content


def create_temporary_file(file_data: bytes) -> _TemporaryFileWrapper:
    temp_file = NamedTemporaryFile(delete=True)
    temp_file.write(file_data)
    temp_file.flush()
    return temp_file


def create_location(data: dict, place: Place) -> Location:
    title = parse_location_title(data['title'])
    location = Location.objects.get_or_create(
        title=title,
        place_id=slugify(title),
        place_info=place,
        lat=data['coordinates']['lat'],
        lng=data['coordinates']['lng'],
    )[0]
    return location


def parse_location_title(full_title: str, max_length=30) -> str:
    '''
    Parse location title from long string full_title
    Firstly, tries to find «Title», title = full_title if not
    Then, shortens received title to max_length.
    '''
    start_quote_index = full_title.find('«')
    end_quote_index = full_title.find('»')
    if start_quote_index != -1 and end_quote_index != -1:
        title = full_title[start_quote_index+1:end_quote_index]
    elif start_quote_index != -1 and end_quote_index == -1:
        title = full_title[start_quote_index+1:]
    else:
        title = full_title

    while len(title) > max_length:
        title = ' '.join(title.split(' ')[:-1])
    return title
