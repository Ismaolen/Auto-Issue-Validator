import gitlab


def connect_to_gitlab(url, private_token):
    """
    Establishes a connection to GitLab.

    Parameters
    ----------
    url : str
        The URL of the GitLab instance.
    private_token : str
        The private token for GitLab authentication.

    Returns
    -------
    gitlab.Gitlab
        An authenticated GitLab object.

    """
    print("Configuring environment variables")
    print("--------------------------------------")
    try:
        # Establish a connection to the GitLab instance
        gl = gitlab.Gitlab(url, private_token=private_token)
        gl.auth()
        print("Connected to GitLab successfully.")
        print("--------------------------------------")
        return gl
    except Exception as e:
        # Handle errors during connection
        print(f"Error connecting to GitLab: {e}")
        exit(1)


def access_project(gl, project_id):
    """
    Attempts to access a specific project in GitLab.

    Parameters
    ----------
    gl : gitlab.Gitlab
        An authenticated GitLab object.
    project_id : int
        The ID of the project to access.

    Returns
    -------
    gitlab.v4.objects.Project
        The GitLab project object.

    """
    try:
        # Attempt to retrieve the project by its ID
        project = gl.projects.get(project_id)
        print(f"Access to project {project_id} successful.")
        print("--------------------------------------")
        return project
    except gitlab.exceptions.GitlabGetError as e:
        # Handle errors during project access
        print(f"Error accessing the project {project_id}: {e}")
        exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        exit(1)
