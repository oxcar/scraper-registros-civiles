
import csv
import geocoder

def main():
    f_urls = open("urls.txt", "r")
    for line in f_urls:
        download_rrcc(line)


start = time.time()
main()
end = time.time()
print("Execution time: %.2f seconds" % (end - start))