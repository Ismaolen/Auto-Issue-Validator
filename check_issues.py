import gitlab
import os

# GitLab private token und Projekt-ID
private_token = os.getenv('GITLAB_PRIVATE_TOKEN')

project_id = os.getenv('GITLAB_PROJECT_ID')
print(project_id)
print(private_token)


# Verbindung zu GitLab herstellen
try:
    gl = gitlab.Gitlab('https://gitlab.rz.htw-berlin.de/', private_token=private_token)
    gl.auth()
except Exception as e:
    print("Fehler bei der Verbindung zu GitLab:", e)
    exit(1)


# Versuchen, auf das Projekt zuzugreifen
try:
    project = gl.projects.get(project_id)
    print(f"Zugriff auf Projekt {project_id} erfolgreich.")
except gitlab.exceptions.GitlabGetError as e:
    print(f"Fehler beim Zugriff auf das Projekt {project_id}: {e}")
    exit(1)
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    exit(1)


# Versuchen, auf das Projekt zuzugreifen
try:
    project = gl.projects.get(project_id)
    print(f"Zugriff auf Projekt {project_id} erfolgreich.")
    print(f"Pfad zum Projekt: {project.path_with_namespace}")
except gitlab.exceptions.GitlabGetError as e:
    print(f"Fehler beim Zugriff auf das Projekt {project_id}: {e}")
    exit(1)
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    exit(1)












print("\ns4\n")
# Holt die neuesten Issues
issues = project.issues.list(order_by='created_at', sort='desc', all=True)

print("\ns5\n")
for issue in issues:
    # Überprüft die erforderlichen Felder
    if not issue.title or not issue.description:
        print(f"Issue {issue.iid} fehlen erforderliche Informationen: Titel oder Beschreibung fehlen.")
    # Hier könnten weitere Überprüfungen für 'Time Spent', 'Epics', 'Milestones' und 'Due Date' implementiert werden
