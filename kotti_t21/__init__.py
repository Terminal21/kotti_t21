from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_t21')


def kotti_configure(settings):
    settings['kotti.fanstatic.view_needed'] += ' kotti_t21.fanstatic.kotti_t21_group'
