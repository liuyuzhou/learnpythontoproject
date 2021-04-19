from urllib import request

response = request.urlopen("https://movie.douban.com/")
content = response.read().decode('utf-8')
print(content)
