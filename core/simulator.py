"""Kavach AI Attack Simulator — Generates realistic attack scenarios for demo"""
import random, time
from datetime import datetime

class AttackSimulator:
    ATTACKER_SUBNETS = ['185.220.101','45.155.205','194.26.135','103.75.201','91.240.118','162.247.74','23.129.64']
    PROTO_NAMES = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}

    def __init__(self, detector, guardian, logger):
        self.detector = detector
        self.guardian = guardian
        self.logger = logger

    def _rand_attacker(self):
        return f"{random.choice(self.ATTACKER_SUBNETS)}.{random.randint(1,254)}"

    def _rand_local(self):
        return f"192.168.1.{random.randint(2,254)}"

    def _make_event(self, src_ip, dst_ip, pkt_len, proto, src_port, dst_port):
        return {'src_ip': src_ip, 'dst_ip': dst_ip, 'packet_length': pkt_len,
                'protocol': proto, 'src_port': src_port, 'dst_port': dst_port,
                'features': [pkt_len, proto, src_port, dst_port]}

    def simulate_ddos(self, n=15):
        attackers = [self._rand_attacker() for _ in range(3)]
        return [self._make_event(random.choice(attackers), '192.168.1.100',
                random.randint(5000,10000), random.choice([1,6,17]),
                random.randint(1,1024), random.choice([80,443])) for _ in range(n)]

    def simulate_port_scan(self, n=12):
        scanner = self._rand_attacker()
        return [self._make_event(scanner, '192.168.1.100',
                random.randint(40,64), 6, random.randint(40000,65535),
                random.randint(1,1024)) for _ in range(n)]

    def simulate_brute_force(self, n=10):
        attacker = self._rand_attacker()
        port = random.choice([22, 3389, 21])
        return [self._make_event(attacker, '192.168.1.100',
                random.randint(100,300), 6, random.randint(1024,65535), port) for _ in range(n)]

    def simulate_dns_amp(self, n=10):
        reflectors = [self._rand_attacker() for _ in range(4)]
        return [self._make_event(random.choice(reflectors), '192.168.1.100',
                random.randint(2000,6000), 17, 53, random.randint(1024,65535)) for _ in range(n)]

    def simulate_normal(self, n=8):
        events = []
        for _ in range(n):
            t = random.choice(['http','https','dns'])
            if t=='http': events.append(self._make_event(self._rand_local(),'142.250.190.78',random.randint(200,1500),6,random.randint(1024,65535),80))
            elif t=='https': events.append(self._make_event(self._rand_local(),'1.1.1.1',random.randint(200,1500),6,random.randint(1024,65535),443))
            else: events.append(self._make_event(self._rand_local(),'8.8.8.8',random.randint(50,200),17,random.randint(1024,65535),53))
        return events

    def run_scenario(self, scenario='mixed'):
        """Run a full attack scenario through the detection pipeline"""
        if scenario == 'ddos': events = self.simulate_ddos()
        elif scenario == 'port_scan': events = self.simulate_port_scan()
        elif scenario == 'brute_force': events = self.simulate_brute_force()
        elif scenario == 'dns_amp': events = self.simulate_dns_amp()
        elif scenario == 'normal': events = self.simulate_normal()
        else:  # mixed
            events = self.simulate_normal(5) + self.simulate_ddos(8) + self.simulate_port_scan(6) + self.simulate_brute_force(5) + self.simulate_dns_amp(5)
            random.shuffle(events)

        results = []
        for evt in events:
            pred = self.detector.predict(evt['features'])
            action = 'Logged'
            blocked = False
            if pred['is_threat']:
                action = self.guardian.handle_threat(evt['src_ip'], pred['threat_type'], pred['confidence'], pred['severity'])
                blocked = 'HONEYTRAPPED' in action

            proto_name = self.PROTO_NAMES.get(evt['protocol'], str(evt['protocol']))
            results.append({
                **evt, **pred, 'action_taken': action, 'blocked': blocked, 'protocol': proto_name
            })
        
        self.logger.batch_log_threats(results)
        return results
