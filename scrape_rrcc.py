import csv
import time
from urllib import request
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def clean_text(text):
    return text.replace("\n", "").replace("\"", "")


def download_rrcc(url):
    req = request.Request(url)
    entidad = clean_text(urlparse(url).path.replace("/", ""))
    entidad_sin_guiones = entidad.replace("-", " ")
    print("Processing: {0}".format(entidad))

    with request.urlopen(req) as response:
        html_response = response.read()
        beautiful_soup = BeautifulSoup(html_response, "html.parser")
        trs = beautiful_soup.find("table", {"class": "oficialias"}).find("tbody").find_all("tr")

        with open("data/not-geocoded/" + entidad + ".csv", "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(["entidad", "nombre_registro", "direccion", "latitud", "longitud", "contacto"])

            for tr in trs:
                tds = tr.find_all("td")
                name = clean_text(tds[0].find("a").text)
                location = clean_text(tds[1].text)
                contact = clean_text(tds[2].text)
                writer.writerow([entidad_sin_guiones, name, location, None, None, contact])


def main():
    f_urls = open("urls.txt", "r")
    for line in f_urls:
        download_rrcc(line)


start = time.time()
main()
end = time.time()
print("Execution time: %.2f seconds" % (end - start))
