import httpx

r = httpx.get('https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt')
print(r.text)
print(r.status_code)
lines = r.text.split('\n')
print(lines[0])