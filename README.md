# Multiple subreddit viewer (MSRV)

 View posts from multiple selected subreddits!
 Built using django.


# Features

<li>Sort the results by <b>hot</b> or <b>new</b>.</li>
<li>Enlarge the images.</li>
<li>Link to the original post on reddit</li>
<li>Displays the subreddit and the upvote of all the posts.</li>

# Snapshots
<a>[Imgur link](https://imgur.com/a/Pbk1jwa)</a>

# How to use?

1. Clone the repo.
2. Create an app using [Reddit app creation page](https://www.reddit.com/prefs/apps) and get the id and key.
3. Get your keys and credentials from [Reddit dev wiki](https://www.reddit.com/wiki/api).
4. Get reddit API keys and refresh tokens for this application.
(Follow this guide to get the needed keys ([How to use Reddit API (alpscode.com)](https://alpscode.com/blog/how-to-use-reddit-api/)).
5. Create a .env file on the same directory as the downloaded repo and add the four credentials to that env file.
```The env file should look like this:
REDDIT_API_KEY=apikey
REDDIT_REFRESH_TOKEN=refreshtoken
uname=value
pass=value
```
6. Run the django server.


