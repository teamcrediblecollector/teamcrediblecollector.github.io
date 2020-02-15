import ads
import json
ADS_DEV_KEY = 'CY3aZ8lY2kkFvk3qrUoFICHpP1yHl6IS7dmwmohv'

def main():

    with open( 'papers.json', 'w' ) as f:
        ads.config.token = ADS_DEV_KEY
        papers = ads.SearchQuery( q ="supernova", sort='citation_count', fl=['title','citation_count'])
        foundPapers = {};
        for paper in papers:
            print(paper.title)
            foundPapers[str(paper.title)] = str(paper.citation_count)

    with open( 'papers.json', 'w' ) as f:
        json.dump( foundPapers, f )


if __name__== "__main__":
        main()
