from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>Types of Protocols</title>
</head>
<body>
    <h1>Types of Network Protocols</h1>
    <ul>
        <li><strong>HTTP:</strong> Transfers web pages between browsers and servers.</li>
        <li><strong>HTTPS:</strong> Transfers web data securely using encryption.</li>
        <li><strong>FTP:</strong> Transfers files between computers.</li>
        <li><strong>SMTP:</strong> Sends email messages.</li>
        <li><strong>DNS:</strong> Translates domain names into IP addresses.</li>
        <li><strong>TCP:</strong> Delivers data reliably and in order.</li>
        <li><strong>UDP:</strong> Sends data quickly without guaranteeing delivery.</li>
    </ul>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()