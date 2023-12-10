import os

from check_issue import process_issues
from config import *
from connection import connect_to_gitlab, access_project


def main():
    # Establish connection to GitLab
    gl = connect_to_gitlab(GITLAB_URL, GITLAB_PRIVATE_TOKEN)

    # Access the specified project
    project = access_project(gl, GITLAB_PROJECT_ID)

    try:
        # Retrieve the latest open issues without any specific label
        issues = project.issues.list(state='opened', labels=[None])
        # Process each issue for checking and updating
        process_issues(issues, project)
    except Exception as e:
        # Print out an error message if there's an issue retrieving the issues
        print(f"Error retrieving issues: {e}")
        exit(1)


# Hauptfunktion ausführen
if __name__ == "__main__":
    main()
