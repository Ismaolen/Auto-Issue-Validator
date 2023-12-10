from Issue_comments import add_comment_to_issue
from config import GITLAB_CI_PIPELINE_URL


def check_title(issue):
    """
    Checks whether the issue has a title.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Title missing" if the title is absent, otherwise None.
    """
    # Check if the title attribute of the issue is set (not None or empty)
    if not issue.title:
        return "Title missing"  # Return a message if the title is missing
    return None  # Return None if the title is present


def check_description(issue):
    """
    Checks whether the issue has a description.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Description missing" if the description
        is absent, otherwise None.
    """
    # Check if the description attribute of the issue is set (not None or empty)
    if not issue.description:
        return "Description missing"  # Return a message if the description is missing
    return None  # Return None if the description is present


def check_assignees(issue):
    """
    Checks whether the issue has assignees.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Assignees missing" if no assignees
        are set for the issue, otherwise None.
    """
    # Check if the assignees attribute of the issue is set (not None or empty)
    if not issue.assignees:
        return "Assignees missing"  # Return a message if assignees are missing
    return None  # Return None if assignees are present


def check_milestone(issue):
    """
    Checks whether the issue is associated with a milestone.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Milestone missing" if no milestone is
        associated with the issue, otherwise None.
    """
    # Check if the milestone attribute of the issue is set (not None)
    if not issue.milestone:
        return "Milestone missing"  # Return a message if the milestone is missing
    return None  # Return None if a milestone is set


def check_due_date(issue):
    """
    Checks whether the issue has a due date.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Due date missing" if no due date
        is set for the issue, otherwise None.
    """
    # Check if the due_date attribute of the issue is set (not None)
    if not issue.due_date:
        return "Due date missing"  # Return a message if the due date is missing
    return None  # Return None if a due date is set


def check_epic(issue):
    """
    Checks whether the issue is associated with an epic.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Epic missing" if no epic is associated with the issue, otherwise None.
    """
    # Check if the epic attribute of the issue is set (not None)
    if not issue.epic:
        return "Epic missing"  # Return a message if the epic is missing
    return None  # Return None if an epic is set


def check_time_estimate(issue):
    """
    Checks whether a time estimate is set for the issue.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns "Time estimate missing" if no time estimate is set for the issue, otherwise None.
    """
    # Retrieve time_stats object and check if the human_time_estimate attribute is set
    time_stats = issue.time_stats()
    if not time_stats['human_time_estimate']:
        return "Time estimate missing"  # Return a message if the time estimate is missing
    return None  # Return None if a time estimate is set


def check_time_spent_is_not_set(issue):
    """
    Checks that no time spent has been logged for the issue, as required for new issues.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    str or None
        Returns a message if time spent is specified, otherwise None.
    """
    # Retrieve time_stats object and check if the human_total_time_spent attribute is not None
    time_stats = issue.time_stats()
    if time_stats['human_total_time_spent'] is not None:
        return "No time spent may be specified for new issues"  # Return a message if time spent is logged
    return None  # Return None if no time is logged


def check_issue_information(issue):
    """
    Consolidates the checks for required information in an issue.

    This function aggregates the results from various checks, including title,
    description, assignees, milestone, due date, epic, time estimate, and
    whether time spent is not set. It returns a list of all missing information.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object to be checked.

    Returns
    -------
    list of str
        A list containing messages about each missing piece of information.
        If all information is present, the list will be empty.
    """
    # List of functions to check various aspects of the issue
    checks = [
        check_title, check_description, check_assignees,
        check_milestone, check_due_date, check_epic, check_time_estimate, check_time_spent_is_not_set
    ]

    # Apply each check function to the issue and compile a list of missing information
    missing_info = [check(issue) for check in checks if check(issue)]
    return missing_info


def display_issue_details(issue, missing_info, label_set):
    """
    Displays the details, missing information, and labels of an issue.

    This function prints out the ID, title, and labels of the issue. It also lists
    any missing information that was identified during the checks. If no information
    is missing, it indicates that the issue meets all requirements.

    Parameters
    ----------
    issue : gitlab.v4.objects.ProjectIssue
        The GitLab issue object whose details are to be displayed.
    missing_info : list of str
        A list of messages indicating what information is missing from the issue.
    label_set : str
        A string representing the labels assigned to the issue.

    """
    # Print a divider for clarity
    print("--------------------------------------")
    # Print issue ID and title
    print(f"Issue ID: {issue.iid}, Title: {issue.title}")
    # Print the labels assigned to the issue
    print(f"Labeled as: {label_set}")

    # Check if there is any missing information and print it out
    if missing_info:
        print("Missing Information:")
        for info in missing_info:
            print(f"- {info}")  # Print each missing piece of information
    else:
        print("The issue meets all requirements.")  # Message when all checks are passed


def process_issues(issues, project):
    """
    Processes a list of issues.

    This function iterates through each issue in the provided list, checks for missing information,
    sets appropriate labels based on the checks, and adds a comment if there are missing details.
    It labels the issue as 'Issue::Not_Valid' if any information is missing,
    and as 'Issue::Ready' and 'Valid' if not.
    It also displays the details of each issue, including the set labels.

    Parameters
    ----------
    issues : list of gitlab.v4.objects.ProjectIssue
        The list of GitLab issues to be processed.
    project : gitlab.v4.objects.Project
        The GitLab project object to which the issues belong.

    """
    print(f"Found Issues in Open-List: {len(issues)}")
    for issue in issues:
        # Check the issue for missing information
        missing_info = check_issue_information(issue)

        if missing_info:
            # If missing information is found, label the issue as 'Issue::Not_Valid'
            issue.labels = ['Issue::Not_Valid']
            label_set = 'Issue::Not_Valid'
            # Create a comment with the missing information and the pipeline link
            comment = f"## Missing Information\n" + "\n".join(
                f"- {info}" for info in missing_info) + f"\n\n[View Pipeline]({GITLAB_CI_PIPELINE_URL})"
            # Display the issue details, including the set labels
            display_issue_details(issue, missing_info, label_set)

            add_comment_to_issue(project, issue.iid, comment)
        else:
            # If no information is missing, label the issue as 'Issue::Ready' and 'Valid'
            issue.labels = ['Issue::Ready', 'Valid']
            label_set = 'Issue::Ready, Valid'
            # Display the issue details, including the set labels
            display_issue_details(issue, missing_info, label_set)

        # Save the updated labels to the issue
        issue.save()


'''
boards = project.boards.list()
if boards:
    board = boards[0]
    b_lists = board.lists.list()
    for b_list in b_lists:
        print(f"Liste ID: {b_list}")
        print(f"Lable: {b_list.label['name']}")
else:
    print("Keine Boards gefunden.")
'''
