import json
from requests_oauthlib import OAuth1Session

CK = "NdLUYwXcg2OHtJD8byFOyKQN0"
CS = "ERBr9HJ89skYwjXujlFkKqDfPSAcNqhYPysW4Y59UIrsH8EuVm"
AT = "1043020041476685824-ALFMgDTRdjQRClHfYDwpXpiVne0IvL"
ATS = "McMBAa2gx4w9OHAlf1mPWx4LaL4yOXO1QbB3ANccrCYTk"
twitter = OAuth1Session(CK, CS, AT, ATS) #OAuth認証　

TLUrl = "https://api.twitter.com/1.1/statuses/user_timeline.json" #TLを取得するのに必要なJsonらしい

params = {'count' : 1} #取得するツイートの数（最新順）
reqTL = twitter.get(TLUrl, params = params) #リクエスト

if reqTL.status_code == 200:
    timeline = json.loads(reqTL.text) #jsonを読み込む
    for tweet in timeline: #そのうちまとめて取得するかもしれないから一応for文回して
        print(tweet['user']['name'] + ":" + tweet['text']) #取得したツイートをprint
else:
    print("ERROR") #エラーの時用　頻繁に叩くとはじかれるから
