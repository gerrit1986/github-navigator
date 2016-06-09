import requests


def get_latest_commit_detail(commits_url, commit_detail):
    """
    Helper function that returns commit details based on a given url and detail specification.
    :param commits_url: url to retrieve
    :param commit_detail: detail to choose
    :return:
    """
    commits_url = commits_url[:-6]
    request = requests.get(commits_url)
    response = request.json()
    try:
        if commit_detail == 'sha':
            result = response[0]['sha']
        elif commit_detail == 'message':
            result = response[0]['commit']['message']
        elif commit_detail == 'author':
            result = response[0]['commit']['author']['name']
        else:
            result = "Error: No commit_detail known."
    except KeyError:
        result = 'Error: Could not get commit details.'
    return result


def get_results(search_term):
    """
    Main function to get the results, sort and return retrieved repositories.
    """
    url = 'https://api.github.com/search/repositories?q={}'.format(search_term)
    request = requests.get(url)
    response = request.json()

    items = response['items']
    sorted_items = sorted(items, key=lambda item: item['created_at'], reverse=True)
    sliced_items = sorted_items[:5]

    repositories = []
    for result in sliced_items:
        commits_url = result['commits_url']
        last_commit_sha = get_latest_commit_detail(commits_url, commit_detail='sha')
        last_commit_message = get_latest_commit_detail(commits_url, commit_detail='message')
        last_commit_author = get_latest_commit_detail(commits_url, commit_detail='author')

        repositories.append({'created_at': result['created_at'],
                             'name': result['name'],
                             'owner_url': result['owner']['html_url'],
                             'avatar_url': result['owner']['avatar_url'],
                             'owner_login': result['owner']['login'],
                             'sha': last_commit_sha,
                             'commit_message': last_commit_message,
                             'commit_author_name': last_commit_author,})
    return repositories
