# 1. TEMPLATES
https://bootstrapmade.com/
folio
myPortfolio

# 2. Add Django-toolbar

# 3. Add django_extensions to settings.py INSTALLED_APPS

# 4. Add categories and books.essential.csv

    Script:
    https://django-oscar.readthedocs.io/en/3.2/howto/importing_a_catalogue.html 

    Example records:
    https://github.com/django-oscar/django-oscar/tree/master/sandbox/fixtures

    mkdir utils; cd utils, touch __init__.py
    # copy-paste books.essential.csv from 'https://github.com/django-oscar/django-oscar/tree/master/sandbox/fixtures' 

    from oscar.apps.partner.importers import CatalogueImporter
    from utils.create_categories import create_categories
    #create_categories()

    import logging
    logger=logging.getLogger()

    importer = CatalogueImporter(logger=logger, delimiter='|')
    importer.handle('utils/books.essential.csv')



