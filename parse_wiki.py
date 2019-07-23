import collections
import requests
import re

def return_uri_html(uri):
    return requests.get(uri).text

def return_wiki_html(topic):
    wiki_request = requests.get(f'https://ru.wikipedia.org/wiki/{topic.capitalize()}')
    return wiki_request.text

def return_words(wiki_html):
    #wiki_html = return_wiki_html(topic)
    words = re.findall('[а-яА-Я]{4,}', wiki_html)
    words_counter = collections.Counter()
    for word in words:
        words_counter[word] += 1
    return words_counter.most_common(50)

def get_first_link_data(topic):
    wiki_html = return_wiki_html(topic)
    link=re.search('<a href="(http[^"]+)"', wiki_html)
    return link.group(1)


stats=return_words(return_uri_html(get_first_link_data('Трям!_Здравствуйте!')))

with open('stats_from_page_first_link.txt', 'w') as f:
    for item in stats:
        f.write(f"{item[0]} - {item[1]}\n")

print('done')
