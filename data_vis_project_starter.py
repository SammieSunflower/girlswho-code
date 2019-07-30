'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)


polar = []
subj = []
bigtweet = ""
for tweet in tweetData:
    k = tweet["text"]
    tb = TextBlob(k)
    pol = tb.polarity
    polar.append(pol)
    sub = tb.subjectivity
    subj.append(sub)
    bigtweet += k
wordd = ["a", "of", "the", "was", "them", "then", "and", "but", "if" ".", "!", "?", ","]
bigblob = TextBlob(bigtweet)
filtd = {}
wordlist = bigblob.words
for word in wordlist:
    bigtweet.isalpha()
    if wordlist == wordd:
        continue

    filtd[word] = bigblob.word_counts[word]




wordcloud = WordCloud().generate_from_frequencies(filtd)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

plt.title("Tweet Histogram")
plt.hist(polar, bins=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
#plt.axis([-1.1, 1.1, 1, 100])
plt.xlabel("Polarity")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


plt.xlabel("Subjectivity")
plt.ylabel("Frequency")
plt.hist(subj, bins=[0, 0.25, 0.5, 0.75, 1], alpha = 0.5)
plt.title("Tweets Histogram")
plt.grid(True)
plt.show()
