import csv
from database.models import geo


FILE_PATH = 'country.csv'
DEBUG = True


def get_existing_counties() -> list[str]:
    return [str(county.name.en) for country in geo.Country.objects]


def save_country_to_db(name_en: str, name_ru: str, phone_code: str, flag_emoji: str):
    debug(f'Starting saving county {name_en}/{name_ru}')
    name = geo.ContainedTransString(en=name_en, ru=name_ru, fallback_language=geo.Language.ENGLISH)
    name.save()
    country = geo.Country(name=name, phone_code=phone_code, flag_emoji=flag_emoji)
    country.save()
    debug(f'Saved county {name_en}/{name_ru}')


def debug(mes: str):
    if DEBUG:
        print(f'[COUNTRY LOAD] {mes}')


def update_countries():
    existing_countries = get_existing_counties()
    debug(f'{len(existing_countries)} exist')
    file = open(FILE_PATH, 'r', newline='')
    reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)
    next(reader, None)  # skip the headers
    for row in reader:
        if row[0] not in existing_countries:
            debug(f'Saving country {row}')
            save_country_to_db(row[0], row[1], row[2], row[3])
        else:
            debug(f'Country {row} skipped')
    debug('Finished')
    file.close()
