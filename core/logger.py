"""Kavach AI Threat Logger — SQLite-based event logging"""
import sqlite3, threading
from datetime import datetime

class ThreatLogger:
    def __init__(self, db_path):
        self.db_path = db_path
        self._lock = threading.Lock()
        self._init_db()

    def _conn(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._lock:
            conn = self._conn()
            conn.execute('''CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL, src_ip TEXT NOT NULL, dst_ip TEXT DEFAULT '192.168.1.100',
                protocol TEXT, src_port INTEGER, dst_port INTEGER, packet_length INTEGER,
                threat_type TEXT NOT NULL, confidence REAL DEFAULT 0.0,
                action_taken TEXT DEFAULT 'Logged', severity TEXT DEFAULT 'info', blocked INTEGER DEFAULT 0
            )''')
            conn.commit(); conn.close()

    def log_threat(self, src_ip, dst_ip, protocol, src_port, dst_port,
                   packet_length, threat_type, confidence, action_taken, severity, blocked=False):
        with self._lock:
            conn = self._conn()
            conn.execute('''INSERT INTO threats 
                (timestamp,src_ip,dst_ip,protocol,src_port,dst_port,packet_length,threat_type,confidence,action_taken,severity,blocked)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                (datetime.now().isoformat(), src_ip, dst_ip, protocol, src_port, dst_port,
                 packet_length, threat_type, round(confidence,4), action_taken, severity, int(blocked)))
            conn.commit(); conn.close()

    def get_recent_threats(self, limit=50):
        with self._lock:
            conn = self._conn(); conn.row_factory = sqlite3.Row
            rows = [dict(r) for r in conn.execute('SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?', (limit,)).fetchall()]
            conn.close(); return rows

    def get_threat_stats(self):
        with self._lock:
            conn = self._conn(); c = conn.cursor()
            c.execute('SELECT COUNT(*) FROM threats WHERE threat_type != "Normal"')
            total_threats = c.fetchone()[0]
            c.execute('SELECT COUNT(DISTINCT src_ip) FROM threats WHERE blocked = 1')
            ips_blocked = c.fetchone()[0]
            c.execute('SELECT COUNT(*) FROM threats')
            total_events = c.fetchone()[0]
            c.execute('SELECT threat_type, COUNT(*) as cnt FROM threats WHERE threat_type != "Normal" GROUP BY threat_type ORDER BY cnt DESC')
            by_type = {r[0]: r[1] for r in c.fetchall()}
            c.execute('SELECT src_ip, COUNT(*) as cnt, threat_type FROM threats WHERE threat_type != "Normal" GROUP BY src_ip ORDER BY cnt DESC LIMIT 10')
            top_ips = [{'ip': r[0], 'count': r[1], 'type': r[2]} for r in c.fetchall()]
            c.execute('''SELECT strftime('%H:%M', timestamp) as minute, COUNT(*) as total,
                SUM(CASE WHEN threat_type != 'Normal' THEN 1 ELSE 0 END) as threats FROM threats GROUP BY minute ORDER BY minute''')
            time_series = [{'time': r[0], 'total': r[1], 'threats': r[2]} for r in c.fetchall()]
            c.execute('SELECT protocol, COUNT(*) as cnt FROM threats GROUP BY protocol')
            by_protocol = {r[0]: r[1] for r in c.fetchall()}
            conn.close()
            return {'total_threats': total_threats, 'ips_blocked': ips_blocked, 'total_events': total_events,
                    'by_type': by_type, 'top_ips': top_ips, 'time_series': time_series, 'by_protocol': by_protocol}

    def clear_all(self):
        with self._lock:
            conn = self._conn(); conn.execute('DELETE FROM threats'); conn.commit(); conn.close()
