import sys
import requests

def urls(output_file):
    url2 = sys.stdin.read().splitlines()

    bad_urls=[]
    good_urls=[]

    for url in url2:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                good_urls.append(url)
        except requests.exceptions.MissingSchema():
            bad_urls.append(url)
            continue
        except requests.exceptions.ConnectionError():
            bad_urls.append(url)
            continue

    with open(output_file,"w") as file:
        file.write('\n'.join(good_urls))

    print(f"Saved URLs in {output_file}")        


#can use data analysing tools

output_file = "filtered_urls.txt"
urls(output_file)