import http.server
import socketserver
ip = input("Podaj adres IP serwera:")
port = int(input("Podaj port serwera http: "))
tekst = input("Napisz tresc strony: ")
plik = open("index.html", "w")
plik.write(tekst)
plik.close()
print("Serwer wlaczony")
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer((ip, port), Handler) as httpd:
    httpd.serve_forever()
