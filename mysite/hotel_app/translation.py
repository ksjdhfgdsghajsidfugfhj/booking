from .models import Services, Country, City
from modeltranslation.translator import TranslationOptions,register

@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('service_name', )

@register(Country)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('country_name', )

@register(City)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('city_name', )

