import csv
import geocoder
import time
import sys
from os import listdir
from os.path import isfile, join


def main():
    path_not_geocoded = "data/not-geocoded"
    path_geocoded = "data/geocoded"
    rrcc_files = [f for f in listdir(path_not_geocoded) if isfile(join(path_not_geocoded, f))]

    for file in rrcc_files:
        print("Processing: {0}".format(file))

        with open(join(path_geocoded, file), "w") as csv_out:
            csv_writer = csv.writer(csv_out, delimiter=',', quoting=csv.QUOTE_ALL)
            csv_reader = csv.reader(open(join(path_not_geocoded, file)), delimiter=',')
            csv_headers = next(csv_reader, None)
            csv_writer.writerow(csv_headers)

            for row in csv_reader:
                entity = row[0]
                location = row[2]
                location_clean = row[3]
                latlng = None

                retries = 0
                while latlng is None:
                    try:
                        latlng = geocoder.arcgis(entity + " " + location_clean).latlng

                        if latlng is None:
                            retries += 1
                            time.sleep(2)
                        elif latlng is not None and len(latlng) == 0:
                            latlng = None
                            retries += 1
                            time.sleep(2)
                        else:
                            retries = 0

                        print("Retries: {}".format(retries))
                        if retries >= 5:
                            latlng = [0, 0]
                    except:
                        print("Exception: error geocoding with Google")
                        print("Exception: %s : %s" % (sys.exc_info()[0], sys.exc_info()[2]))

                print(latlng)
                if latlng is not None and len(latlng) > 0:
                    row[3] = latlng[0]
                    row[4] = latlng[1]

                csv_writer.writerow(row)


start = time.time()
main()
end = time.time()
print("Execution time: %.2f seconds" % (end - start))
