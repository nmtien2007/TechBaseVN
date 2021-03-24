from django.conf import settings

class DatabaseRouter(object):

    def db_for_read(self, model, **hints):
        if hasattr(model, 'Config'):
            if hasattr(model.Config, 'db_for_read'):
                return model.Config.db_for_read
            elif hasattr(model.Config, 'db_for_all'):
                return model.Config.db_for_all
        if (hasattr(settings, 'DATABASE_APPS_MAPPING') and
            (model._meta.app_label in settings.DATABASE_APPS_MAPPING)):
            return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
        return 'default'

    def db_for_write(self, model, **hints):
        if hasattr(model, 'Config'):
            if hasattr(model.Config, 'db_for_write'):
                return model.Config.db_for_write
            elif hasattr(model.Config, 'db_for_all'):
                return model.Config.db_for_all
        if (hasattr(settings, 'DATABASE_APPS_MAPPING') and
            (model._meta.app_label in settings.DATABASE_APPS_MAPPING)):
            return settings.DATABASE_APPS_MAPPING[model._meta.app_label]
        return 'default'
