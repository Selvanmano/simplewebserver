from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>computer details</title>
        <header>
            <h1>selvanmano (26000969)</h1>
         </header>
         <table border="2" cellpadding="4">
            <tr>
                <th>Device name</th>
                <th>processor</th>
                <th>Istalled RAM</th>
                <th>Graphics card</th>
                <th>storage</th>
                <th>Device id</th>
                <th>Product id</th>
                <th>system type</th>
                <th>pen and touch</th>
            </tr>
            <tr>
                <td>SMS-Laptop</td>
                <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
                <td>16.0 GB (15.7 GB usable)</td>
                <td>Intel(R) Graphics (128 MB)</td>
                <td>116 GB of 477 GB used</td>
                <td>EE529A96-ED92-4EB0-976E-B731EEC94B78</td>
                <td>00342-42954-08761-AAOEM</td>
                <td>64-bit operating system, x64-based processor</td>
                <td>No pen or touch input is available for this display</td>
            </tr>
         </table>  
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()