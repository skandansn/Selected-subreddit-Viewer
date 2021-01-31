from django.http import response
from django.shortcuts import render

# Create your views here.
 
def home(request):
    return render(request,"home.html")

def searchfields(request):
    from dotenv import load_dotenv
    load_dotenv()
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
    try:
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
        else:
            df=df.sort_values(by=['title'],ascending=False)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)
        df=df.reset_index().to_json(orient='records')
        data=[]
        import json
        data=json.loads(df)

        context={"searches":data}
    except:
        print("renewing token")
        auth = requests.auth.HTTPBasicAuth('fh6MHyar10oWQQ','URbBcNKAorRWSIGPt79MhUto-HY4vg')
        data = {'grant_type': 'refresh_token','refresh_token':str(os.getenv('REDDIT_REFRESH_TOKEN'))}
        headers = {'User-Agent': 'multisubview'}

        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth,data=data, headers=headers)
        TOKEN = res.json()

        f=open(r"C:\Users\godsk\Desktop\multisubreddit\.env","w")
        f.write("REDDIT_API_KEY="+TOKEN['access_token']+"\nREDDIT_REFRESH_TOKEN=-Dyj6IO7m7RwfixhlJb5fTXOj-6bl6w")
        f.close()
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
        else:
            df=df.sort_values(by=['title'],ascending=False)
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
