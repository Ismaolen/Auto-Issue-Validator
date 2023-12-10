

def add_comment_to_issue(project, issue_id, comment):
    """
    Adds a comment to a specific issue.

    This function attempts to add a comment to the issue identified by the given issue ID
    within the specified project. If successful, it prints a confirmation message. If an error
    occurs, it prints an error message.

    Parameters
    ----------
    project : gitlab.v4.objects.Project
        The GitLab project object containing the issue.
    issue_id : int
        The ID of the issue to which the comment will be added.
    comment : str
        The content of the comment to be added.

    """
    try:
        # Attempt to retrieve the issue by its ID
        issue = project.issues.get(issue_id)

        # Create a new note (comment) in the issue with the provided comment text
        issue.notes.create({'body': comment})
        print(f"Comment added to issue {issue_id}.")
    except Exception as e:
        print(f"Error adding a comment to issue {issue_id}: {e}")
