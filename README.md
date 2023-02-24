# UGRC Python Starter Tempalate

![Build Status](https://github.com/agrc/python/workflows/Build%20and%20Test/badge.svg)
[![codecov](https://codecov.io/gh/agrc/python/branch/main/graph/badge.svg)](https://codecov.io/gh/agrc/python)

UGRC's default Python project configuration/template

## Installation

1. Create new environment for the project
   - With python 3 (without arcpy)
     - `python -m venv .env`
     - activate the environment `source .env/bin/activate`
   - With conda
     - `conda create --name PROJECT_NAME python=3.9`
1. Rename `src/projectname` folder to your desired project name
1. Edit the `setup.py:name, url, project_urls, keywords, and entry_points` to reflect your new project name
1. Edit the `test_projectname.py` to match your project name.
   - You will have one `test_filename.py` file for each file in your `src` directory and you will write tests for the specific file in the `test_filename.py` file
   - If you are using arcpy, you should mock out the arcpy module in any test that directly imports arcpy or tests any of your code that imports arcpy. Add `import mock_arcpy` to the imports in your test file before importing arcpy or any of your modules that you're testing. This effectively replaces all of arcpy in the test environment with a Mock object; you can then create custom `return_value`s and `side_effects` for whatever functions you need, and the tests will run appropriately in GitHub Actions (which doesn't have arcpy installed).
1. Set up Codecov to create coverage reports from GitHub Actions:
   - Navigate to [codecov.io](https://codecov.io/gh/agrc/python), logging in with your GitHub account if necessary.
   - Select your new repo and and copy the Upload Token.
   - Create a new repository secret (github repository Settings -> Secrets -> Actions secrets -> New repository secret) named `CODECOV_TOKEN` and paste the Upload Token as the Value
1. Install an editable package for development
   - `pip install -e ".[tests]"`
   - Add any project requirements to the `setup.py:install_requires` array
   - If you specify `arcgis` version 2.0.0 or greater, uncomment the section in `.github/workflows/ci.yml` so that GitHub Actions installs the necessary dependencies.
1. Run the tests
   - VSCode -> `Python: Run All Tests` or `Python: Debug All Tests`
   - `ptw`
     - **P**y**t**est **W**atch will restart the tests every time you save a file
1. Bring your test code coverage to 80% or above!
1. Replace `python` in the badge links at the top of this page with your new repository name.

### Publishing to PyPI with GitHub Actions

The `release.yml` GitHub action will publish a [GitHub release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) to PyPI. Publishing from GitHub ensures that files in your `.gitignore` file (such as secrets files and other credentials) won't accidentally be uploaded to PyPI because they won't (or at least shouldn't) be in your GitHub repository.

**NOTE:** Make sure your README.md is fit for public consumption. It will be uploaded to PyPI and displayed as your project's main page for the version you upload.

1. Update `src/projectname/version.py` in the sed command in `release.yml` to point to the proper version file in your project structure.
1. Create a [PyPI API token](https://pypi.org/help/#apitoken) for your project.
   - Limit its scope to just this one project—you'll create a new token for every individual project
1. Create a new repository secret (github repository Settings -> Secrets -> Actions secrets -> New repository secret) named `PYPI_API_TOKEN` and paste the token as the value.

This action will be triggered whenever you cut a new release on GitHub:

1. Draft a new release in your GitHub repo.
1. Choose the appropriate [tag](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/managing-tags) to specify which version/code state should be released
   a. If you've been adding tags via the desktop client as linked above, or through VSCode, select the appropriate tag.
   a. If you haven't already added a tag, type in a new version and select "Create a new tag." Select the proper target branch (main, dev, etc) to apply the tag to.
   a. Version numbers should use PEP 440-compliant [semantic versioning](https://semver.org/) in the form `x.y.z`, where major version `x` increases whenever you make a breaking change, minor version `y` increases whenever you make a substantial but non-breaking change (adding new features, etc), and patch `z` changes whenever you make a small, non-breaking quick fix or change.
1. Make sure "Set as a pre-release" is left unchecked. Pre-releases will fail to publish.
1. Publish the release. This will kick off the publish action, and if all goes well your package will be available on PyPI.
