
## Badges

Add badges from shields.io to display build status, test coverage, and more. For example:

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-80%25-yellow)
![GitLab](https://img.shields.io/badge/GitLab-auto--issue--validator-blue)

# Auto Issue Validator

The Auto Issue Validator is a custom tool designed for GitLab projects to automate 
the validation of newly created issues. It ensures that all issues meet predefined 
criteria for completeness and clarity before being processed further. This tool 
significantly improves the issue management workflow by reducing manual 
review time and enhancing the quality of issue submissions.

## Features

- **Automated Validation**: Automatically checks each new issue against a set of 
predefined rules to ensure that all necessary information is included.
- **Immediate Feedback**: Posts comments on issues that fail validation, 
specifying what information is missing or inadequate.
- **Customizable Checklist**: Allows project maintainers to define their 
own validation criteria based on the project's requirements.
- **Labeling System**: Automatically labels issues as `validation-passed` 
or `validation-failed` based on the outcome of the validation.

## Getting Started

### Prerequisites

- GitLab account with maintainer access to the target repository.
- Basic understanding of GitLab CI/CD pipelines.

## Installation

Follow these steps to set up and configure the Auto Issue Validator in your project:

### 1. Clone the Repository

Start by cloning the Auto Issue Validator repository to your local machine:

```bash
git clone https://gitlab.rz.htw-berlin.de/your-group/auto-issue-validator.git
cd auto-issue-validator
```

### 2. Configure the Validation Script

Edit the `check_issue.py` file within the Auto Issue Validator directory to 
define the validation criteria for new issues based on your project's needs.

### 3. Establish Communication Through the GitLab API

To enable communication with your specific GitLab instance via the GitLab API, 
set up the necessary variables in the `config.py` script with appropriate values. 
This configuration is crucial for the script to interact with your GitLab projects and issues.

### 4. Set Up the CI/CD Pipeline

You have two options to integrate the validation script into your project's CI/CD pipeline.

#### Option A: Direct Execution

Add the validation script directly to your `.gitlab-ci.yml` in the target repository:

```yaml
stages:
  - validate_issues

validate_new_issues:
  stage: validate_issues
  image: python:3.8
  script:
    - python path/to/auto-issue-validator/main.py
  only:
    - schedules
```

#### Option B: Using as a Submodule

Alternatively, if you prefer to use the validator as a submodule:

1. **Create a `.gitmodules` File**

   Define the submodule in your project with the correct URL in a `.gitmodules` file:

   ```plaintext
   [submodule "extern/submodule"]
     path = extern/submodule
     url = https://[gitlab.instance.url]/your-group/issue-template.git
   ```

2. **Update Your `.gitlab-ci.yml`**

   Configure the CI/CD pipeline to include the submodule, 
 ensuring you replace `[gitlab.instance.url]` with the 
actual URL of your GitLab instance:

   ```yaml
   stages:
     - check_issues
   
   check_issue_template:
     stage: check_issues
     image: python:3.8
     tags: [Linux]
     before_script:
       - sed -i "s|https://[gitlab.instance.url]|https://gitlab-ci-token:$CI_JOB_TOKEN@[gitlab.instance.url]|" .gitmodules
       - git submodule sync
       - git submodule update --init --recursive
       - pip install python-gitlab
     script:
       - python extern/submodule/main.py
     only:
       - schedules
   ```

### Note on Triggering Validation

GitLab does not support triggering a pipeline when a new issue is created. 
To circumvent this limitation, create a scheduled pipeline that periodically 
checks for new issues to validate. This approach ensures 
that new issues are validated regularly.

Please replace `[your-group]`, `[gitlab.instance.url]`, and `path/to/auto-issue-validator/main.py` 
with your actual values. 


### Usage

- **Creating a New Issue**: Simply create a new issue in your GitLab project 
as usual. The Auto Issue Validator will automatically check the issue and provide feedback.
- **Reviewing Validation Feedback**: Check the comments posted by the 
validator on the issue for any required actions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the repository or contact the project maintainers directly.

## Acknowledgments

- Special thanks to GitLab for providing the platform that inspired this tool.


## Roadmap

- **Q1 2024**: Implement basic validation checks for issue titles and descriptions.
- **Q2 2024**: Add support for custom validation rules specified by the project maintainers.
- **Q3 2024**: Integrate a feedback system that allows issue creators to see validation results directly in the issue comments.
- **Q4 2024**: Expand the tool to support validation of merge requests.

## Support

For support, please open an issue in the repository or contact the project maintainers directly through GitLab.

## Authors and Acknowledgment

Developed by Ismail Al Shuaybi.

## Project Status

The project is currently in the development phase, with basic issue validation 
functionality available. Future updates will focus on enhancing features and incorporating user feedback.
