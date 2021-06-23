import requests
from bs4 import BeautifulSoup

LIMIT = 50
indeed_url =f"https://es.indeed.com/ofertas?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=Espa%C3%B1a&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch"

def extract_indeed_pages():
    search_job = requests.get(indeed_url)
    job_soup = BeautifulSoup(search_job.text, "html.parser")
    pagination = job_soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.get_text(strip=True)))

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    result = requests.get(f"{indeed_url}&start={0 * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        print(title)
    return jobs