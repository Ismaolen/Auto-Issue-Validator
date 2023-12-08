import gitlab
import os

# GitLab private token und Projekt-ID
print("\ns1\n")
private_token = os.getenv('GITLAB_PRIVATE_TOKEN')

project_id = os.getenv('GITLAB_PROJECT_ID')
print(project_id)
print(private_token)

print("\ns2\n")
gl = gitlab.Gitlab('https://gitlab.rz.htw-berlin.de/', private_token=private_token)
print("\ns3\n")
project = gl.projects.get(project_id)

print("\ns4\n")
# Holt die neuesten Issues
issues = project.issues.list(order_by='created_at', sort='desc', all=True)

print("\ns5\n")
for issue in issues:
    # Überprüft die erforderlichen Felder
    if not issue.title or not issue.description:
        print(f"Issue {issue.iid} fehlen erforderliche Informationen: Titel oder Beschreibung fehlen.")
    # Hier könnten weitere Überprüfungen für 'Time Spent', 'Epics', 'Milestones' und 'Due Date' implementiert werden
