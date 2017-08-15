# -*- coding: utf-8 -*-

from lxml import html
import requests
import json
import arrow

def truue(tree, xpath, q):
    if len(tree.xpath(xpath)) != 0:
        return tree.xpath(xpath)[0] == q
    return False

def scrape_schedule(ssn, pwd):
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
    if truue(tree, '/html/body/div/div/div/div/div/h2/text()', u'Breyta lykilorði'):
        # need to handle gracefully
        raise Exception('You need to change your password')
    login_link = tree.xpath('/html/body/div[2]/div/table/tbody/tr[1]/td[2]/a')[0].attrib['href']
    login_link = 'https://nam.inna.is{}'.format(login_link)

    # STEP 3 --- Select new inna
    resp = s.get(login_link)

    # STEP 4 --- Get user
    resp = s.get('https://nam.inna.is/api/UserData/GetLoggedInUser')
    user_data = json.loads(resp.content)
    student_id = user_data['studentId']
    week = arrow.utcnow().span('week')
    monday = week[0].format('DD.MM.YYYY')
    sunday = week[1].format('DD.MM.YYYY')

    # STEP 5 --- Get schedule
    params = {
        'student_id': student_id,
        'date_from': monday,
        'date_to': sunday,
        'attendanceOverview': '0',
        'class_id': '',
        'classroom_id': '',
        'groupId': '',
        'moduleId': '',
        'staff_id': '',
        'terms': ''
    }
    resp = s.get('https://nam.inna.is/api/Timetable/GetTimetable', params=params)
    return json.loads(resp.content)
