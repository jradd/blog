import os

# Accepted file formats regex
# markdown accepted
# reStructuredText not accepted for now
ACCEPTED_FILE_FORMATS = "^.*\.md$" # .md

# Git Repo Config
# Fetched via environmental variables
if os.environ.get('POSTS_GIT_REPO') is not None:
  GIT_REPO_URL = os.environ.get('POSTS_GIT_REPO')
else:
  GIT_REPO_URL = "https://github.com/jradd/blogdata.git"

GIT_REPO_DIR_NAME = GIT_REPO_URL.split('/')[-1].replace('.git','')
if os.environ.get('POSTS_GIT_REPO_SECRET') is not None:
  GIT_REPO_SECRET = os.environ.get('POSTS_GIT_REPO_SECRET')
else:
  GIT_REPO_SECRET = "4a23b1b45cdaef7ddb68828627c743574684deba"

# Server Config
PORT=5000
HOST='0.0.0.0'
DEBUG_STATUS=False
