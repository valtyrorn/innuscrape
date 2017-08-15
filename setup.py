from distutils.core import setup
setup(
    name = 'innuscrape',
    packages = ['innuscrape'],
    version = '1.0',
    description = 'Scraping utility for schedules on inna.is',
    author = 'Valtýr Örn Kjartansson',
    author_email = 'valtyr@gmail.com',
    url = 'https://github.com/valtyrorn/innuscrape',
    download_url = 'https://github.com/valtyrorn/innuscrape/archive/master.zip',
    keywords = ['inna', 'scrape'],
    classifiers = [],
    install_requires = ['lxml','arrow','requests'],
)
 
