from fastapi import FastAPI
from urllib.parse import urlparse, urlunparse, parse_qsl

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Link Cleaner API is Active"}

@app.get("/clean")
def clean_url(url: str):
    parsed = urlparse(url)
    # The "Boring" list of tracking junk to remove
    bad_params = {'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'ref', 'qid', 's', 'fbclid', 'gclid'}
    
    query_params = parse_qsl(parsed.query)
    clean_params = [p for p in query_params if p[0].lower() not in bad_params]
    
    new_query = "&".join([f"{k}={v}" for k, v in clean_params])
    return {"cleaned_url": urlunparse(parsed._replace(query=new_query))}
