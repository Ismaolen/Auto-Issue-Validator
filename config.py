# GitLab private token and projekt-id
import os

GITLAB_URL = 'https://gitlab.rz.htw-berlin.de/'
GITLAB_PRIVATE_TOKEN = os.getenv('GITLAB_PRIVATE_TOKEN')
GITLAB_PROJECT_ID =  os.getenv('GITLAB_PROJECT_ID')
GITLAB_CI_PIPELINE_URL = os.getenv('CI_PIPELINE_URL', 'Pipeline-URL nicht verfügbar')