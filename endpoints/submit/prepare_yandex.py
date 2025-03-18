import serializers.models as ser
import database

from ..base import app


def make_yandex_form_card(form: database.OpportunityForm, data: dict[str, any]) -> dict:
    card = {
        'link': form.opportunity.source.link,
        'form': data  # TODO: file as stream
    }
    return card
