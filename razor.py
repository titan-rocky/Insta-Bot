import requests

param={'client_id':'219659553386884','client_secret':'b415914dc6f0fab90ad03c765237c417','scope':'user_profile,user_media','response_type':'code'}
ab=requests.get(url='https://api.instagram.com/oauth/authorize',headers=param)
print(ab)
c=ab.text
print(c)