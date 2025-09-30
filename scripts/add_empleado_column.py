import sqlite3, os
p = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')
p = os.path.normpath(p)
print('DB path:', p)
if not os.path.exists(p):
    raise SystemExit('Database not found')
conn = sqlite3.connect(p)
cur = conn.cursor()
# Check if table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='prestamos_prestamo'")
if not cur.fetchone():
    print('Table prestamos_prestamo does not exist')
    conn.close()
    raise SystemExit(1)
# Check columns
cur.execute("PRAGMA table_info('prestamos_prestamo')")
cols = [r[1] for r in cur.fetchall()]
print('Existing columns:', cols)
if 'empleado_id' in cols:
    print('Column empleado_id already exists; nothing to do')
else:
    print('Adding column empleado_id (INTEGER)')
    cur.execute("ALTER TABLE prestamos_prestamo ADD COLUMN empleado_id INTEGER")
    conn.commit()
    cur.execute("PRAGMA table_info('prestamos_prestamo')")
    cols = [r[1] for r in cur.fetchall()]
    print('New columns:', cols)
conn.close()
