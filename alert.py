import requests
import sys

auth = 'your@email.com', 'you password'
view_tickets = []
# view ID, open view in a brower, the ID is the trailing number in the URL
view_id = '11762533354001'

#print(f'Getting tickets from view ID {view_id}')
url = f'https://icewarp.zendesk.com/api/v2/views/{view_id}/tickets.json'
while url:
   response = requests.get(url, auth=auth)
   page_data = response.json()
   tickets = page_data['tickets']
   view_tickets.extend(tickets)
   url = page_data['next_page']
   tcount = page_data['count']
   if tcount >= 1:
     print("Ticket alert")
print(page_data['count'])
