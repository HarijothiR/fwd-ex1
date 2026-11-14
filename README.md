# EX01 Developing a Simple Webserver
## Date:15/10/2026
## REG NO:26018293

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~from http.server import HTTPServer, BaseHTTPRequestHandler
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
~~~
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
~~~


## OUTPUT:
![alt text](<Screenshot 2026-10-15 145308.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

