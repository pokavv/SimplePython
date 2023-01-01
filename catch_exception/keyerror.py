posts = [
    {'like': 21, 'comment': 2},
    {'like': 13, 'comment': 2, 'share': 1},
    {'like': 33, 'comment': 8, 'share': 3},
    {'like': 4, 'comment': 2},
    {'like': 1, 'comment': 1},
    {'like': 19, 'comment': 3}
]

total_likes = 0
for post in posts:
    try:
        total_likes = total_likes + post['like']
    except KeyError:
        pass

print(total_likes)