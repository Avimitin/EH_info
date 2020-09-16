# author: avimitin
import collections
import json
import re


# 生成一个简单的类
comic_info = collections.namedtuple(
    typename='comic',
    field_names=[
        "category",
        "artist",
        "rating",
        "title",
        "thumb",
        "tags"
    ]
)


def filter(file):
    '''
    Help filtrating those useless message. Need a dict type object.
    :param file: dict type object from the response JSON
    '''
    meta = file['gmetadata'][0]
    tags = tags_filter(meta['tags'])['tags']
    artist = tags_filter(meta['tags'])['artist']
    comic = comic_info(
        category = meta['category'],
        rating = meta['rating'],
        title = meta['title_jpn'],
        thumb = meta['thumb'],
        tags = tags,
        artist = artist
    )
    return comic


def tags_filter(tags):
    '''
    Help filtrating useless tags
    :param tags: tags from response JSON
    '''
    new_tags = []
    artist="Unknown Artist"
    for tag in tags:
        if re.match("artist:", tag):
            artist = tag.split(':')[1]

        if re.match("female:", tag):
            tag = tag.split(':')[1]
            new_tags.append(tag)
    
    return {"tags": new_tags, "artist": artist}


'''
if __name__ == "__main__":
    with open('resource/test.json', 'r', encoding='utf-8') as json_f:
        f = json.load(json_f)

    print(filter(f).artist)
'''
