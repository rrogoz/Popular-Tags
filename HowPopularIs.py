
import requests
import json
from datetime import datetime, timedelta
import functions
# User input
link = 'https://api.stackexchange.com/2.3/questions'
startdate = int((datetime.today()-timedelta(minutes=15)).timestamp())
enddate = int(datetime.today().timestamp())
params = {
    "site": "stackoverflow",
    "order": "desc",
    "fromdate": startdate,
    "todate": enddate,
    "pagesize": 100
}

# main
r = requests.get(link, params=params)
try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('error')
else:
    dictTagCount = functions.group_and_count_tags(questions)
    dictTagNormalizedCount = functions.get_normalized_count(dictTagCount)
    mostPopularTags_10 = functions.get_highest_record(dictTagNormalizedCount)
    functions.print_bar_chart(mostPopularTags_10, [
                              '', 'Frequency distribution [%]'],
                              yAxisFactor=100,
                              chartTitle='The most popular tags on stackoverflow')
