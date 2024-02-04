import pyshorteners
#Encurtar URL usando o serviço TinyURL

#Insira uma URL e a armazena na variável url
url = str(input('Digite a URL: '))
#pyshorteners.Shortener().tinyurl.short(url) cria um objeto Shortener e especifica o serviço TinyURL para encurtar o URL fornecido
print(f'A URL encurtada é: {pyshorteners.Shortener().tinyurl.short(url)}')
