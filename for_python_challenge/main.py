from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, send_file


def extract_jobs_remoteok(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs_board = soup.find('table', id="jobsboard")
    job_list = jobs_board.find_all('tr', {'data-offset': True})
    for job in job_list:
      link = job['data-url']
      company = job['data-company']
      position_card = job.find('td',
                               class_="company position company_and_position")
      position = position_card.select_one('a h2')
      location = position_card.select_one('div', class_="location")
      job_data = {
        'link': f"https://remoteok.com{link}",
        'company': company.strip(),
        'position': position.string.strip(),
        'location': location.text
      }
      results.append(job_data)
  return results


def extract_jobs_wwr(term):
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company = anchor.find('span', class_="company")
        position = anchor.find('span', class_="title")
        location = anchor.find('span', class_="region company")
        job_data = {
          'link': f"https://weworkremotely.com/{link}",
          'company': company.string.strip(),
          'position': position.string.strip(),
          'location': location.string.strip(),
        }
        results.append(job_data)
    return results


#file.py


def save_to_file(file_name, jobs):
  file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
  file.write("Position, Company, Location, URL\n")
  for job in jobs:
    file.wirte(
      f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n"
    )
  file.close()


#main.py 내용

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/search")
def search():
  term = request.args.get("term")
  if term == None:
    return redirect("/")
  if term in db:
    jobs = db[term]
  else:
    wwr = extract_jobs_wwr(term)
    remoteok = extract_jobs_remoteok(term)
    jobs = remoteok + wwr
    db[term] = jobs
  return render_template("search.html", term=term, jobs=jobs)


@app.route("/export")
def export():
  term = request.args.get("term")
  if term == None:
    return redirect("/")
  if term not in db:
    return redirect(f"/search?term={term}")
  save_to_file(term, db[term])
  return send_file(f"{term}.csv", as_attachment=True)


app.run("0.0.0.0")
