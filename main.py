import argparse
from module.request_info import get_ex_info
from module import percolator


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get URL')
    parser.add_argument('-u',type=str,default=None)
    arg = parser.parse_args()
    url = arg.u
    if url:
        response = get_ex_info(url)
        comic_info = percolator.filter(response)
        print('''
======================
Title: %s
Artist: %s
Category: %s
Rating: %s
Tags: %s
Thumb_URL: %s
======================
        '''
        % (
            comic_info.title, 
            comic_info.artist,
            comic_info.category,
            comic_info.rating,
            comic_info.tags,
            comic_info.thumb
        )
        )
    else:
        print("Need An URL!!\nUsage: -u 'https://example.com'")

