# GitHub Action with Allure Report

This repository demonstrates how to generate an Allure report using GitHub Actions. By leveraging GitHub Actions, you can automate the process of generating and publishing Allure reports for your projects.

## Usage

To use this example repository and generate Allure reports for your own projects, follow these steps:

### 1. Fork this Repository

Fork this repository to your own GitHub account by clicking the ["Fork"](https://github.com/ashikkumar23/github-action-with-allure-report/fork) button at the top-right corner of the page. This will create a copy of the repository under your account.

### 2. Enable GitHub Actions

Go to the "Actions" tab in your forked repository and click on the "I understand my workflows, go ahead and enable them" button to enable GitHub Actions for your repository. This will allow the automated execution of workflows defined in the repository.

### 3. Configure Repository Settings

To enable Allure report generation and publishing, you need to configure the following settings in your repository:

#### 3.1. Set Up the `ALLURE_RESULTS_PATH` Variable

1. Go to the "Settings" tab in your forked repository.
2. Click on the "Secrets and variables" option in the left sidebar.
3. Click on the "Actions", Select "Variables" from Actions secrets and variables page and then Click on the "New repository variable" button.
4. In the "Name" field, enter `ALLURE_RESULTS_PATH`.
5. In the "Value" field, enter the desired path where Allure results will be saved during the workflow execution (e.g., `allure-results`).
6. Click on the "Add variable" button to save the secret.

#### 3.2. Configure GitHub Pages

To publish the generated Allure report, you can leverage GitHub Pages. Follow these steps to configure GitHub Pages for your repository:

1. Go to the "Settings" tab in your forked repository.
2. Scroll down to the "GitHub Pages" section under "Code and automation"
3. Under "Source" dropdown, select "Deploy from a branch".
4. Under the "Branch" dropdown, select the branch that contains the Allure report artifacts (e.g., `gh-pages`).
5. Click on the "Save" button.
6. For more information, refer https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-from-a-branch

### 4. Run the Workflow

Once you have forked the repository, enabled GitHub Actions, and configured the necessary settings, you can run the workflow to generate the Allure report:

1. Go to the "Actions" tab in your forked repository.
2. Click on the workflow named "Allure Report Generation" on the left sidebar.
3. Click on the "Run workflow" button.
4. Select the branch on which you want to run the workflow (e.g., `master`).
5. Click on the "Run workflow" button to start the execution.

The workflow will execute, generate the Allure report based on the provided configurations, and publish it using GitHub Pages. You can then access the published report by visiting the GitHub Pages URL of your repository. i.e, `https://<your_github_username>.github.io/<your_github_repo>/`

Sample report @ https://ashikkumar23.github.io/github-action-with-allure-report/

## Additional Resources

For more information on configuring and customizing the Allure report generation process, refer to the following resources:

- [Allure Official Documentation](https://docs.qameta.io/allure/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

Feel free to explore the repository's code and workflows to understand the implementation details of generating Allure reports using GitHub Actions.

If you have any questions or encounter any issues, please [open an issue](https://github.com/ashikkumar23/github-action-with-allure-report/issues) in this repository.

Happy testing and reporting! 🚀
