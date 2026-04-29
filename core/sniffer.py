"""Kavach AI Network Sniffer — Real-time packet capture with Scapy"""
import threading
from datetime import datetime

class NetworkSniffer:
    """Captures live packets and runs them through the AI pipeline"""
    def __init__(self, detector, guardian, logger):
        self.detector = detector
        self.guardian = guardian
        self.logger = logger
        self.running = False
        self._thread = None
        self.PROTO = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        self.buffer = []
        self.buffer_size = 1 
        self.scan_counts = {} 
        self.target_ip = None # Blackout Mode by default
        self.NOISY_PORTS = [5353, 137, 138, 139, 445, 1900, 5355, 3702, 5000] 
        # WHITELIST: Google and Cisco/OpenDNS only
        self.WHITELIST_IPS = ['146.112.', '216.239.', '8.8.8.8', '8.8.4.4']

    def _process_packet(self, packet):
        try:
            from scapy.all import IP, TCP, UDP
            if not packet.haslayer(IP): return
            ip = packet[IP]
            
            # 🔒 IRON SHIELD LOCKDOWN: Only the friend's laptop exists to this AI
            ALLOWED_IP = '172.111.1.41'
            if ip.src != ALLOWED_IP and ip.src != '127.0.0.1':
                return 

            # Skip Whitelisted background services
            if any(ip.src.startswith(prefix) for prefix in self.WHITELIST_IPS): return
            
            length = len(packet)
            proto = ip.proto
            src_port = packet.sport if packet.haslayer(TCP) or packet.haslayer(UDP) else 0
            dst_port = packet.dport if packet.haslayer(TCP) or packet.haslayer(UDP) else 0
            
            # Skip local Streamlit traffic and common background noise
            if dst_port == 8501 or src_port == 8501: return
            if dst_port in self.NOISY_PORTS or src_port in self.NOISY_PORTS: return
            if ip.dst.endswith('.255') or ip.dst.startswith('224.') or ip.dst.startswith('239.'): return
            
            # Feature extraction
            features = [length, proto, src_port, dst_port]
            pred = self.detector.predict(features)

            # 🔴 DEMO HARDENING: Now set to "EXCLUSIVE IP" mode
            is_syn = packet.haslayer(TCP) and packet[TCP].flags == 0x02
            
            if is_syn and length < 64 and (pred['threat_type'] == 'Normal'):
                self.scan_counts[ip.src] = self.scan_counts.get(ip.src, 0) + 1
                if self.scan_counts[ip.src] >= 20: 
                    pred['is_threat'] = True
                    pred['threat_type'] = 'Port Scan'
                    pred['confidence'] = 0.99
                    pred['severity'] = 'high'
                else:
                    return 
            else:
                if ip.src in self.scan_counts: del self.scan_counts[ip.src]

            action = 'Logged'
            blocked = False
            if pred['is_threat']:
                action = self.guardian.handle_threat(ip.src, pred['threat_type'], pred['confidence'], pred['severity'])
                blocked = 'HONEYTRAPPED' in action
            
            # Buffer the event
            self.buffer.append({
                'src_ip': ip.src, 'dst_ip': ip.dst, 'protocol': self.PROTO.get(proto, str(proto)),
                'src_port': src_port, 'dst_port': dst_port, 'packet_length': length,
                'threat_type': pred['threat_type'], 'confidence': pred['confidence'],
                'action_taken': action, 'severity': pred['severity'], 'blocked': blocked
            })

            # Instant flush for demo
            self.logger.batch_log_threats(self.buffer)
            self.buffer = []

        except Exception as e:
            pass

    def start(self, interface=None):
        if self.running: return
        self.running = True
        
        # Auto-detect interface if None
        if interface is None:
            try:
                from scapy.all import conf
                interface = conf.iface
            except: pass

        def _sniff():
            try:
                from scapy.all import sniff
                sniff(prn=self._process_packet, store=0, iface=interface,
                      stop_filter=lambda _: not self.running)
            except Exception as e:
                print(f"Sniffer error: {e}")
                self.running = False
        self._thread = threading.Thread(target=_sniff, daemon=True)
        self._thread.start()

    def stop(self):
        self.running = False
