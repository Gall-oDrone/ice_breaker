import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile: str, mock: bool = False):
    """
        Scrape information from LinkedIn profiles,
        Manually scrape the information from LinkedIn profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Gall-oDrone/e9c0853d6b7d9e46ce4c7ab0c9ba022f/raw/2903594cd8868da7dc8a08abbd5e0ba9e2afc5a8/del-gal.json"
        response = requests.get(
            linkedin_profile,
            timeout=10,
        )
    else:
        api_endpoint ="https://nubela.co/proxycurl/api/linkedin/person/profile-picture"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )


if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile="https://www.linkedin.com/in/del-gal-9ba824244/", mock=True
        )
    )
