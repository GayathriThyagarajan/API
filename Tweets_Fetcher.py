{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tweet Retriever based on Keyword"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tweepy\n",
    "import csv\n",
    "import pandas as pd\n",
    "####input your credentials here\n",
    "consumer_key = ''\n",
    "consumer_secret = ''\n",
    "access_token = ''\n",
    "access_token_secret = ''\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
   "source": [
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth,wait_on_rate_limit=True)\n",
    "#####United Airlines\n",
    "# Open/Create a file to append data\n",
    "csvFile = open('Brexit_new.csv', 'a')\n",
    "csvFile.truncate()\n",
    "#Use csv Writer\n",
    "csvWriter = csv.writer(csvFile)\n",
    "csvWriter.writerow([\"date\", \"tweet\"])\n",
    "\n",
    "for tweet in tweepy.Cursor(api.search,q=\"#brexit\", count = 100,\n",
    "                           lang=\"en\",\n",
    "                           since=\"2019-02-01\").items():\n",
    "    print (tweet.created_at, tweet.text)\n",
    "    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])\n",
    "csvWriter.close()\n",
    "csvFile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "date     94339\n",
       "tweet    94339\n",
       "dtype: int64"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('Brexit_new.csv')\n",
    "data.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}