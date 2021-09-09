import requests


param={'client_id':'219659553386884','client_secret':'7cf1bacf97bd987db14671acd60c0625','grant_type':'authorization_code','redirect_uri':'https://titan-rocky.github.io/Insta-Bot/?code=AQCwz24TFNusX-8ViW382ornkwtSQtlpW3tdK506riZ4dyurAXannEhykBOb3kypNBg3u35tTuOwJlr9VFHXdi9qS8-F-0YcoJbQwvzZXksiCKQdSZ7uxcZ_x4KMDr14bx-UX5TBSD8ETsll548XUqhwbwWzToZkhqT4udidX-q3CSGE-diK6o8JG3XMjkHCWV130-O3iEVBqdmMq-IMihBzd5cNlq6CmJBtTYpse3BLPw#_','code':'AQCwz24TFNusX-8ViW382ornkwtSQtlpW3tdK506riZ4dyurAXannEhykBOb3kypNBg3u35tTuOwJlr9VFHXdi9qS8-F-0YcoJbQwvzZXksiCKQdSZ7uxcZ_x4KMDr14bx-UX5TBSD8ETsll548XUqhwbwWzToZkhqT4udidX-q3CSGE-diK6o8JG3XMjkHCWV130-O3iEVBqdmMq-IMihBzd5cNlq6CmJBtTYpse3BLPw'}
ab=requests.post(url='https://api.instagram.com/oauth/access_token',data=param)
c=ab.json()
print(c)
print(ab.url)


TOKEN='IGQVJWTDkyLS1yQWdoV3FWcHo1ek5zX3VSNVV4OGRJaEVhSVRwN2ZAMc0dUNVZANT0h2NGZAiRUZA4dFJmZAm1xWmpnYm9Ea2lSSkExZAzQzekx6RUwtZAHNDRGJLMm5WcDRJdFlGdk5zMjd4WmU3Q25HLXR5RQZDZD'
par2={'fields':'id','access_token':f'{TOKEN}'}
idreq=requests.get(url='https://graph.instagram.com/me',params=par2)
print(idreq.json())