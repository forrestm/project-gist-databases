import requests

def import_gists_to_database(db, username, commit=True):
    API = "https://api.github.com/users/{}/gists".format(username)
    
    SQL_QUERY = """
                INSERT INTO gists
                    (github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url)
                VALUES
                    (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, :comments_url)
                """
    
    gists = requests.get(API)
    gists.raise_for_status()
    json_gist = gists.json()
    
    for gist_data in json_gist:
        params = {
        'github_id': gist_data['id'],
        'html_url': gist_data['html_url'],
        'git_pull_url': gist_data['git_pull_url'],
        'git_push_url': gist_data['git_push_url'],
        'commits_url': gist_data['commits_url'],
        'forks_url': gist_data['forks_url'],
        'public': gist_data['public'],
        'created_at': gist_data['created_at'],
        'updated_at': gist_data['updated_at'],
        'comments': gist_data['comments'],
        'comments_url': gist_data['comments_url']}

        db.execute(SQL_QUERY,params)
        if commit:
            db.commit()
