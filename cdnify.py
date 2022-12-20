from bs4 import BeautifulSoup
import requests


def extractDownloadLink(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    link = soup.find("div", class_="row",
                     id="download-wrapper").find("a",
                                                 id="download-url")['href']
    return link


# def download_file(url):
#     # Send an HTTP request to the URL and store the response
#     response = requests.get(url)

#     # Check if the response is successful
#     if response.status_code == 200:
#         # Get the file name from the URL
#         file_name = url.split("/")[-1]

#         # Open a file with the same name as the file on the server
#         with open(file_name, "wb") as f:
#             # Write the contents of the response to the file
#             f.write(response.content)


# Open the file containing the links
with open("links.txt", "r") as f:
    # Read each line of the file
    for line in f:
        # Extract the download link from the URL
        download_link = extractDownloadLink(line.strip())
        with open("results.txt", "a+") as f2:
            f2.writelines(download_link + "\n")
        # Download the file using the download link
        # download_file(download_link)
