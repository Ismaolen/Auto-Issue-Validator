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

try:
    # Holt die neuesten Issues
    issues = project.issues.list(order_by='created_at', sort='desc', all=True)
    print(f"Gefundene Issues: {len(issues)}")
except Exception as e:
    print(f"Fehler beim Abrufen der Issues: {e}")
    exit(1)

print("\ns5\n")

for issue in issues:
    print(f"Issue-ID: {issue.iid}")
    print(f"Titel: {issue.title}")
    print(f"Beschreibung: {issue.description}")
    print(f"Status: {issue.state}")
    print(f"Autor: {issue.author['username']}")
    print(f"Erstellt am: {issue.created_at}")
    print("--------------------------------------")

print("\nÜberprüfung der Issues abgeschlossen.")




print("\ns6\n")

try:
    # Holt alle Boards des Projekts
    boards = project.boards.list()
    if boards:
        # Nimmt das erste Board
        board = boards[0]
        print(f"Board: {board.name}")

        # Holt alle Listen des Boards und ruft jedes Objekt einzeln ab, um alle Daten zu erhalten
        board_lists = board.lists.list()
        for bl in board_lists:
            board_list = board.lists.get(bl.id)  # Ruft jedes Listenobjekt einzeln ab
            print(f"Liste: {board_list.name}, ID: {board_list.id}")
    else:
        print("Keine Boards gefunden.")
except Exception as e:
    print(f"Fehler beim Abrufen der Boards: {e}")

print("\nÜberprüfung der Boards und Listen abgeschlossen.")




