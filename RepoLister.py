import requests
import bs4


def list_repos(name, page_type):
    name = name.strip()
    page = 1
    repos = []
    repos_on_current_page = -1
    next_page = None

    while repos_on_current_page != 0:

        repos_on_current_page = 0
        url = "https://github.com/" + name
        if page_type == '1':
            url += '?tab=repositories'

        if page > 1:
            url += '?page='+str(page)

        if next_page:
            url = next_page

        next_page = None

        res = requests.get(url)

        page += 1

        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        repo_tags = soup.find_all("a", itemprop="name codeRepository")

        for tag in repo_tags:
            repo = tag.text.replace('\n', '').strip()

            stars_tag = soup.find("a", href='/' + name + '/' + repo + '/stargazers')
            if stars_tag:
                stars_tag = stars_tag.text.replace('\n', '').replace(',', '').strip()
                stars = int(stars_tag.replace('k', '000').replace('.', ''))
                if '.' in stars_tag:
                    stars //= 10
            else:
                stars = 0

            repos.append((repo, stars))
            repos_on_current_page += 1

        if page_type == '1':
            buttons = soup.find_all("a", {"class": "BtnGroup-item"})
            for button in buttons:
                if 'after' in button["href"]:
                    next_page = button["href"]

    return repos


def sort_repos_by_stars(repos, descending):
    if not repos:
        return repos
    repos = sorted(repos, key=lambda x: x[1], reverse=descending)
    return repos

