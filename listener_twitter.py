import socket
import tweepy # facilitar a conexão

HOST = 'localhost'
PORT = 9009 # GARANTINDO QUE NÃO ESTÁ SENDO USADA

s = socket.socket()
s.bind((HOST,PORT))
print(f'Agurando conexão na porta: {PORT}')

s.listen(5)
conn,address = s.accept()

print(f'Recebendo a solictação de {address}')
# Agora vem o ponto diferente, onde utilizamos o Token - Twitter

token = 'AAAAAAAAAAAAAAAAAAAAAJVJnQEAAAAAPkfzlaO7C0qHISDlbApgqgh18WI%3DXcElHUIJKVcueRmZwFc3sup1stVeIa8K3nH74phc7ZOyFZJfMC'
keyword = 'futebol' # palavra de interesse que queremos fazer um filtro

# conexão com a API do Twitter, fechando o Listener

class GetTweets(tweepy.StreamingClient): # faremos uma classe com modificações de métodos específicos, da classe tweepy.StreamingClient
    def on_tweet(self,tweet):
        # TWEETS sejam imprimidos
        print(tweet.text) # o Tweet vem em formato JSON - queremos apenas o índice do TEXT: (VALOR)
        print('='*50) # GRACEJO oara separar
        conn.send(tweet.text.encode('utf-8','ignore')) # decodificador para não der problema nas palavras

printer = GetTweets(token) # passando o Token de conexão 
printer.add_rules(tweepy.StreamRule(keyword)) # em tempo real, você traz através das palavra chave
printer.filter()

conn.close() # configurando o nosso listener totalmente