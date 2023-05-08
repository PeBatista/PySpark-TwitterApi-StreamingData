import time
import socket 

HOST = 'localhost'
PORT = 3000

s = socket.socket()

s.bind((HOST, PORT))
print(f'aguardando Conexão na Porta: {PORT}')

s.listen(5) # OUVINDO
conn, address = s.accept()

print(f'recebendo solicitação de {address}')

messages = [
    'Mensagem A',
    'Mensagem B',
    'Mensagem C',
    'Mensagem D',
    'Mensagem E',
    'Mensagem F',
    'Pedro Lindo',
]

for message in messages:
    message = bytes(message,'utf-8') # convertendo ele em bytes para não der errado na comunicação
    conn.send(message)
    time.sleep(4)

conn.close()
#socket criado.

#TESTE DE LISTENER