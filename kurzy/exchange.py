import httpx


URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"


def get_eur_rate():
      response = httpx.get(URL)
      response.raise_for_status()

      lines = response.text.split("\n")

      for line in lines:
            if line.startswith("EMU|") or "|EUR|" in line:
                  rate_str = line.split("|")[-1].replace(",", ".")
                  return float(rate_str)

      raise ValueError("Kurz EUR nebyl nalezen")


def get_float_input(prompt):
   while True:
         try:
               return float(input(prompt).replace(",", "."))
         except ValueError:
               print("Zadej prosím číslo.")


def main():
        try:
             rate = get_eur_rate()
        except Exception as e:
             print("Nepodařilo se načíst kurz:", e)
             return

        print("Aktuální kurz EUR je", rate, "CZK")
        print("Vyber typ převodu:")
        print("1 - EUR -> CZK")
        print("2 - CZK -> EUR")

        choice = input("Zadej volbu (1/2): ")

        if choice == "1":
               eur = get_float_input("Zadej částku v EUR: ")
               czk = eur * rate
               print(round(eur, 2), "EUR =", round(czk, 2), "CZK")

        elif choice == "2":
               czk = get_float_input("Zadej částku v CZK: ")
               eur = czk / rate
               print(round(czk, 2), "CZK =", round(eur, 2), "EUR")

        else:
               print("Neplatná volba.")


if __name__ == "__main__":
        main()
