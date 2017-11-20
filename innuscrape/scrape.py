# -*- coding: utf-8 -*-

from lxml import html
import requests
import json
import arrow


class InnuException(Exception):
    def __init__(self, value):
        self.message = value

    def __str__(self):
        return repr(self.message)


def truue(tree, xpath, q):
    if len(tree.xpath(xpath)) != 0:
        return tree.xpath(xpath)[0] == q
    return False


def scrape_schedule(ssn, pwd):
    s = requests.Session()

    # STEP 1 --- Send login request to Inna
    resp = s.post(
        'https://r.inna.is/auth/login',
        json={'username': ssn, 'password': pwd})
    data = resp.json()
    if (resp.status_code is not 200):
        raise InnuException(data['message'])

    s.headers.update({'Authorization': 'Bearer {}'.format(data['token'])})

    # STEP X --- Get login list
    resp = s.get('https://r.inna.is/auth/access?callback_url=&callback_system=')
    data = resp.json()

    # STEP X --- Select new inna
    resp = s.post('https://r.inna.is/auth/system?i=0&system=1&user_id={}&status=1'.format(data[0]['user_id']))
    data = resp.json()
    resp = s.get(data['url'])

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
