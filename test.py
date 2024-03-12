import main
import pytest
from requests import get
from requests import post


print(post('http://localhost:5000/api/news', json={}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'job': 'Заголовок',
                 'team_leader_id': 2,
                 'work_size': 10,
                 'if_finished': False}).json())