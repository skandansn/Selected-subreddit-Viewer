from django.http import response
from django.shortcuts import render

# Create your views here.
 
def home(request):
    return render(request,"home.html")

def searchfields(request):
    try:
        if(request.POST['fields']==''):
            return render(request,'home.html')
    except:
        return render(request,'home.html')


    x=[]
    x=request.POST['fields'].split()
    sort=request.POST['sort']

    
    import requests,os
    import requests.auth

    headers = {"Authorization": "bearer "+str(os.getenv('REDDIT_API_KEY')), "User-Agent": "multisubview"}
    searchlist=[]
    for i in x:
        searchlist.append(requests.get("https://oauth.reddit.com/r/"+i+"/"+sort, headers=headers,params={'limit':'100'}))

    import pandas as pd
    df=pd.DataFrame()

    for i in searchlist:
        for post in (i.json()['data']['children']):
            df = df.append({
            'score':post['data']['score'],
            'title': post['data']['title'],
            'permalink': post['data']['permalink'],
            'subreddit': post['data']['subreddit'],
            'url': post['data']['url']
        }, ignore_index=True)
       

    if sort=='hot':
        df=df.sort_values(by=['score'],ascending=False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    df=df.reset_index().to_json(orient='records')
    data=[]
    import json
    data=json.loads(df)

    context={"searches":data}

    return render(request,"home.html",context)
