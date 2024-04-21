from vidstream import StreamingServer
import threading
reciver = StreamingServer('192.168.222.104',8080)

t = threading.Thread(target=reciver.start_server)
t.start()

while input("") !="stop":
  continue

reciver.stop_server()