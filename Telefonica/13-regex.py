import re

def isValidMail(mail):
    if re.search(".+@[a-z]+\\.com", mail):
        return True
    else:
        return False

print(isValidMail("antonio@gmail.com"))
print(isValidMail("@gmail.com"))
print(isValidMail("antonio@gmailcom"))
print(isValidMail("antonio@.com"))
print(isValidMail("antoniogmail.com"))

def isValidUrl(url):
    if re.search("http.*://" + 
                "(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}" + 
                "\\.[a-z]{2,6}" + 
                "(/[a-zA-Z0-9@:%._\\+~#?&//=])*", url):
        return True
    else:
        return False

print(isValidUrl("https://open.spotify.com/playlist/6URl7UbPfOxa3dqTcg1jxL"))
print(isValidUrl("https://open.spotify.com"))
print(isValidUrl("http://open.spotify.com/playlist/6URl7UbPfOxa3dqTcg1jxL"))
print(isValidUrl("https://spotify.com/playlist/6URl7UbPfOxa3dqTcg1jxL"))
print(isValidUrl("https://spotify"))