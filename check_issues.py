import gitlab
import os

# GitLab private token und Projekt-ID
private_token = os.getenv('GITLAB_PRIVATE_TOKEN')
project_id = os.getenv('GITLAB_PROJECT_ID')

gl = gitlab.Gitlab('https://gitlab.com', private_token=private_token)
project = gl.projects.get(project_id)

# Holt die neuesten Issues
issues = project.issues.list(order_by='created_at', sort='desc', all=True)

for issue in issues:
    # Überprüft die erforderlichen Felder
    if not issue.title or not issue.description:
        print(f"Issue {issue.iid} fehlen erforderliche Informationen: Titel oder Beschreibung fehlen.")
    # Hier könnten weitere Überprüfungen für 'Time Spent', 'Epics', 'Milestones' und 'Due Date' implementiert werden
