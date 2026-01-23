import httpx

r = httpx.get('https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt')
print(r.text)
print(r.status_code)
lines = r.text.split('\n')
print(lines[0])
line_euro = ""

for line in lines:
    if "EUR" in line:
        line_euro = line
        break
rate_str = line_euro.split('|')[-1].replace(',','.')
rate = float(rate_str)

print("kurz je", rate)

value_in = float(input("kolik mas eur?"))
value_out = value_in * rate
print(f"Tak to je {value_out:.2f} korun")