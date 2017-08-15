<p align="center"><img src="bag.png" width=80 alt="Icon"/></p>
<h2 align="center">Innuscrape</h2>

Einföld leið til að sækja stundartöflur í JSON formi af Innu sem ætti að virka fyrir alla framhaldsskóla á Íslandi. Skrifað til notkunar í [ögn](http://ogn.is).

### Notaðu innuscrape í eigin verkefni
Til að setja innuscrape upp í eigin verkefni notarðu eftirfarandi skipanir.
Ef þú notar pip:
```Shell
pip install -e git://github.com/valtyr/innuscrape.git#egg=innuscrape
```

Ef þú notar pipenv:
```Shell
pipenv git://github.com/valtyr/innuscrape.git
```

### Uppsetningarleiðbeiningar
Verkefnið notast við pipenv frá Kenneth Rietz og er því einfalt í uppsetningu:
```Shell
pip install pipenv
pipenv shell
pipenv install
```
Eftir það geturðu notað skraparann í þínum eigin kóða:
```Python
from scrape import scrape_schedule
schedule = scrape_schedule('[KENNITALA HÉR]', '[LYKILORÐ HÉR]')
# ...nota stundatöfluna
```

### To do:
- [x] Rannsaka server köll sem Inna framkvæmir 
- [x] Finna út úr CSRF drasli
- [x] Skrifa grunnlógík
- [ ] Finna og bæta inn _moment_ týpu dagsetningarsafni
- [ ] Testa þetta í þaula
