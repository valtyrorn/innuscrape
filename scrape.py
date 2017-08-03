# -*- coding: utf-8 -*-

from lxml import html
import requests

def scrape_stundaskra(ssn, pwd):
    s = requests.Session()

    # STEP 1 --- Fetch CSRF token
    resp = s.get('https://nam.inna.is/auth/login')
    tree = html.fromstring(resp.content)

    csrf_input = tree.xpath('/html/body/div/div/div/div/div/form/div[3]/input')[0]
    if csrf_input is None:
        raise Exception('No csrf input element')
    else:
        csrf_token = csrf_input.value

    # STEP 2 --- Send login request to Inna
    resp = s.post('https://nam.inna.is/auth/login', data={'kennitala':ssn, 'password': pwd, 'CSRF_TOKEN': csrf_token})
    tree = html.fromstring(resp.content)
    if tree.xpath('/html/body/div/div/div/div/div/h2/text()')[0] == u'Breyta lykilorði':
        # need to handle gracefully
        raise Exception('You need to change your password')
