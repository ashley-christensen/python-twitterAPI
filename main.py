import tweepy
ak = 'sibhNbJDsT2q0IKXCjbHFO9Sb'
aks = 'I0wFt6xSlFbbkJctosYFDwt8ARsTM12vSme1jve5iPfKNYvC3k'

at = '1486471993796923399-KQSwNchXy8wCQBZrmfTDdCg35d3i88'
ats = 'u2WNIIBy6GU5EGA2gYbBDw2zsOl7YZnFQOztS3pbyLgll'

def OAuth(): 
    try: 
      auth = tweepy.OAuthHandler(ak, aks)
      auth.set_access_token(at,ats)
      return auth
    except Exception as e:
      return 🔞 

oauth = OAuth()
apicall = tweepy.API(oauth) 

apicall.update_status('here is a sample tweet from the API call program')
print('Tweet created')
