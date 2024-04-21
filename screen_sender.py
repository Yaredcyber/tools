from vidstream import ScreenShareClient
import threading
sender = ScreenShareClient('192.168.222.104',8080)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") !="stop":
  continue

sender.stop_server()