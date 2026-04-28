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

    def _process_packet(self, packet):
        try:
            from scapy.all import IP, TCP, UDP
            if not packet.haslayer(IP): return
            ip = packet[IP]
            length = len(packet)
            proto = ip.proto
            src_port = packet.sport if packet.haslayer(TCP) or packet.haslayer(UDP) else 0
            dst_port = packet.dport if packet.haslayer(TCP) or packet.haslayer(UDP) else 0
            features = [length, proto, src_port, dst_port]
            pred = self.detector.predict(features)
            action = 'Logged'
            blocked = False
            if pred['is_threat']:
                action = self.guardian.handle_threat(ip.src, pred['threat_type'], pred['confidence'], pred['severity'])
                blocked = 'HONEYTRAPPED' in action
            self.logger.log_threat(ip.src, ip.dst, self.PROTO.get(proto, str(proto)),
                                   src_port, dst_port, length, pred['threat_type'],
                                   pred['confidence'], action, pred['severity'], blocked)
        except Exception as e:
            print(f"Packet error: {e}")

    def start(self, interface=None):
        if self.running: return
        self.running = True
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
