users = [
    {
        'username': 'ali',
        'posts': [
            {'likes': 12, 'shares': 5},
            {'likes': 30, 'shares': 15},
            {'likes': 5, 'shares': 0}
        ],
        'friends': ('sara', 'mina', 'hamid')
    },
    {
        'username': 'sara',
        'posts': [
            {'likes': 22, 'shares': 13},
            {'likes': 6, 'shares': 2}
        ],
        'friends': ('ali', 'hamid')
    },
    {
        'username': 'mina',
        'posts': [
            {'likes': 5, 'shares': 1}
        ],
        'friends': ('ali',)
    },
]

def likes_shares(users):
    max = 0
    for user in users:
        total_taamol = sum(post['likes'] + post['shares'] for post in user.get('posts', []))
        if total_taamol > max:
            max = total_taamol
            max_name = user['username']
    return max_name

def most_friends(users):
    friend_groups = {}
    for user in users:
        count = len(user['friends'])
        if count in friend_groups:
            friend_groups[count].append(user['username'])
        else:
            friend_groups[count] = [user['username']]

    return dict(sorted(friend_groups.items(), key=lambda item: item[0], reverse=False))


def active_users(users):
    active_names = []
    for user in users:
        posts = user['posts']
        if len(posts) < 2:
            continue
        for post in posts:
            if post['likes'] > 20:
                active_names.append(user['username'])
                break
    return active_names

def repeated(name):
    for ch in name.lower():
        if name.lower().count(ch) == 2:
            return True
    return False

def name_repeated(users):
    return [user['username'] for user in users if repeated(user['username'])]

def top_by_friend(users,n):
    rates = []
    lst=[]
    for user in users:
        name = user['username']
        num_friends = len(user['friends']) if user['friends'] else 0
        if num_friends == 0:
            continue
        total_taamol = sum(post['likes'] + post['shares'] for post in user.get('posts', []))
        rate = total_taamol / num_friends
        rates.append((name, rate))
    rates.sort(key=lambda x: x[1], reverse=True)
    for i in rates[:n]:
        lst.append(i[0])
    return lst


print(likes_shares(users))
print(most_friends(users))
print(active_users(users))
print(name_repeated(users))
print((top_by_friend(users,3)))