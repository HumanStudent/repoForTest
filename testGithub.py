from github import Github
from pathlib import Path
from dotenv import load_dotenv

# env_path = Path('.') / '.varFileEnv'
# load_dotenv(dotenv_path=env_path) 
g = Github("ef91c9fec686ec33ad1a9eeabf5cb15ea3da8212")
# GITHUB_ACCESS_TOKEN
# g = Github("HumanStudent", "hellohuman1")

repos = g.get_user().get_repos()
for repo in repos:
    print(repo.name)
