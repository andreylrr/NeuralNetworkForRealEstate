# library to generate user agent
from user_agent import generate_user_agent
# generate a user agent
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
for i in range(3):
    print(generate_user_agent(device_type="desktop", os=('mac', 'linux')))
print(headers)