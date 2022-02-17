
from asyncio.log import logger
import traceback


d = {
    "custom_claims": {
        'teams': ['tId1', 'tId2', 'tId3']
    }
}

# d['custom_claims']['teams'].append('tId5')
# idx = d['custom_claims']['teams'].index('tId5')
# print(idx)
try:
    team_id = 'tId1'
    d['custom_claims']['teams'].pop(d['custom_claims']['teams'].index(team_id))
except ValueError as e:
    print(traceback.format_exc())
    print('raised here ', e)
    raise Exception

team_id='tI3'
if team_id in d.values():
    print('----yes')

else:
    print('--no--')

if team_id in d['teams'].get(team_id):
    print('yes')
