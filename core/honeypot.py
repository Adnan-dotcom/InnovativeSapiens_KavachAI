"""Kavach AI — Deceptive Web Honeypot"""
import http.server
import socketserver
import threading
from datetime import datetime

class DeceptiveHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # This is the "Alert" that your friend will see on THEIR laptop
        attacker_ip = self.client_address[0]
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>KAVACH AI - SESSION INTERCEPTED</title>
            <style>
                body {{ background: #050000; color: #ff3366; font-family: 'Courier New', monospace; text-align: center; padding: 100px; overflow: hidden; }}
                .alert {{ border: 10px solid #ff3366; padding: 60px; display: inline-block; box-shadow: 0 0 100px #f00; }}
                h1 {{ font-size: 5rem; margin: 0; letter-spacing: -2px; }}
                h2 {{ color: #fff; font-size: 1.8rem; letter-spacing: 8px; margin-top: 0; }}
                .ip {{ color: #00f2ff; font-size: 3rem; font-weight: 900; margin-top: 40px; border: 2px solid #00f2ff; padding: 10px; display: inline-block; }}
                .status {{ font-size: 1.2rem; color: #fff; margin-top: 50px; text-transform: uppercase; letter-spacing: 5px; }}
            </style>
        </head>
        <body>
            <div class="alert">
                <h1>SYSTEM BREACH</h1>
                <h2>ACCESS PERMANENTLY REVOKED</h2>
                <div class="status">KAVACH AI HAS INTERCEPTED YOUR SESSION</div>
                <div class="ip">ATTACKER IP LOGGED: {attacker_ip}</div>
                <div style="margin-top: 60px; color: #555; font-size: 0.7rem; letter-spacing: 3px;">
                    BIOMETRIC DATA HARVESTED | GEOLOCATION ENCRYPTED | AUTHORITIES DISPATCHED
                </div>
            </div>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        # Prevent spamming the console, we'll log via our ThreatLogger if needed
        return

class HoneyportServer:
    def __init__(self, port=9999):
        self.port = port
        self.httpd = None
        self.thread = None
        self.running = False

    def start(self):
        if self.running: return
        self.running = True
        
        def _serve():
            with socketserver.TCPServer(("", self.port), DeceptiveHandler) as httpd:
                self.httpd = httpd
                httpd.serve_forever()
        
        self.thread = threading.Thread(target=_serve, daemon=True)
        self.thread.start()
        print(f"ShadowGuard Honeyport active on port {self.port}")

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
        self.running = False
