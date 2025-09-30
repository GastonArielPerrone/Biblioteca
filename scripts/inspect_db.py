import os, sqlite3
p='db.sqlite3'
print('db exists?', os.path.exists(p), 'size=', os.path.getsize(p) if os.path.exists(p) else 'n/a')
conn=sqlite3.connect(p)
cur=conn.cursor()
cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='prestamos_prestamo'")
row=cur.fetchone()
print('row:', row)
if row:
    print('schema:\n', row[1])
    cur.execute("PRAGMA table_info('prestamos_prestamo')")
    for r in cur.fetchall():
        print(r)
conn.close()
