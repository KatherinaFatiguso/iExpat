import requests
from lxml import html

categories = {"Engineer": "Engineers Australia",
              "Teacher": "AITSL",
              "Doctor": "Medical Board of Australia",
              "Nurse": "ANMAC",
              "Tech Worker": "ACS"}

class Occupation:
    def __init__(self):
        self.sol = False
        self.flagged = False
        self.title = ""
        self.states = []


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        score = 1
        if (self.states):
            score = 2
        if (self.sol):
            if (self.flagged):
                score = 3
            else:
                score = 4
        return self.title.encode('utf-8') + ", " + str(score) + ", "+ str(self.states)

csol_url = "https://www.border.gov.au/Trav/Work/Work/Skills-assessment-and-assessing-authorities/skilled-occupations-lists/CSOL"
sol_url = 'https://www.border.gov.au/Trav/Work/Work/Skills-assessment-and-assessing-authorities/skilled-occupations-lists/SOL'
vic_url = 'http://www.liveinvictoria.vic.gov.au/visas-and-immigrating/occupation-lists/state-nomination-occupation-list-for-victoria'
sa_url = 'http://www.migration.sa.gov.au/skilled-migrants/lists-of-state-nominated-occupations'
flagged_url = "https://www.education.gov.au/flagged-occupations-sol-2015-2016"

inv_map = {v: k for k, v in categories.items()}
from collections import defaultdict
final_map = defaultdict(list)
occs = defaultdict(Occupation)


def fill(get_url):
    page = requests.get(get_url)
    htmlx = html.fromstring(page.content)
    rows = htmlx.xpath('//tr')

    for e in rows:

        if get_url == csol_url or get_url == sol_url:
            cols = e.xpath('./td')
            if len(cols) == 3:

                oid = cols[1].text.strip()
                links = cols[2].xpath('./a')
                title = cols[0].text.strip()
                if links:

                    url = links[0].text.strip(u'\u200b')
                    key = inv_map.get(url, None)
                    if get_url == csol_url:
                        if key:
                            occs[oid].title = title.lower()
                            final_map[key].append(oid)
                    if get_url == sol_url:
                        occ = occs.get(oid, None)
                        if occ:
                            occ.sol = True
        elif get_url == flagged_url:
            cols = e.xpath('./td/p')
            if len(cols) == 2:
                oid = cols[0].text.strip()
                occ = occs.get(oid, None)
                if occ:
                    occ.flagged = True
        elif get_url == sa_url:
            cols = e.xpath('./td')
            if len(cols) == 5:
                oid = cols[0].text.strip()
                occ = occs.get(oid, None)
                if occ:
                    occ.states.append("sa")
        elif get_url == vic_url:
            cols = e.xpath('./td')
            if len(cols) == 5:
                oid = cols[0].text.strip()
                occ = occs.get(oid, None)
                if occ:
                    occ.states.append("vic")

if __name__ == '__main__':
    fill(csol_url)
    fill(sol_url)
    fill(flagged_url)
    fill(vic_url)
    fill(sa_url)
    for k,v in final_map.items():
        print "*****"
        print k
        print "****"
        for e in v:
            print str(occs[e]) +";",
        print ""
