<p align="center"><img src="bag.png" width=80 alt="Icon"/></p>
<h2 align="center">Innuscrape</h2>

Einföld leið til að sækja stundartöflur í JSON formi af Innu sem ætti að virka fyrir alla framhaldsskóla á Íslandi. Skrifað til notkunar í [anorak](http://anorak.is).

### Notaðu innuscrape í eigin verkefni
Til að setja innuscrape upp í eigin verkefni notarðu eftirfarandi skipanir.
Ef þú notar pip:
```Shell
pip install -e git+https://github.com/valtyrorn/innuscrape.git#egg=innuscrape
```

Ef þú notar pipenv:
```Shell
pipenv install git+https://github.com/valtyrorn/innuscrape.git#egg=innuscrape
```

Eftir það geturðu notað skraparann í þínum eigin kóða:
```Python
import innuscrape
schedule = innuscrape.scrape_schedule('[KENNITALA HÉR]', '[LYKILORÐ HÉR]')
# ...nota stundatöfluna
```

### Uppsetningarleiðbeiningar
Þetta eru leiðbeiningar fyrir þá sem hafa áhuga á að vinna í verkefninu. Verkefnið notast við pipenv frá Kenneth Rietz og er því einfalt í uppsetningu:
```Shell
pip install pipenv
pipenv shell
pipenv install
```

### To do:
- [x] Rannsaka server köll sem Inna framkvæmir 
- [x] Finna út úr CSRF drasli
- [x] Skrifa grunnlógík
- [ ] Finna og bæta inn _moment_ týpu dagsetningarsafni
- [ ] Testa þetta í þaula
