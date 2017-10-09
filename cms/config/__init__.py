# coding: utf-8

from dynaconf.contrib.flask_dynaconf import FlaskDynaconf


def configure(app):
    """Configure Dynaconf Flask Extension
    Dynaconf permite que variaveis sejam carregadas de diversas fontes
    e arquivos diferentes.
    Como arquivos yaml, ini, json,
    bancos de dados como Mongo ou Redis
    e variaveis de ambiente
    """
    FlaskDynaconf(
        app=app,
        DYNACONF_NAMESPACE='CMS',
        SETTINGS_MODULE='{}/settings.yml'.format(app.root_path)
    )
