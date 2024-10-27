import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "chicken-disease-classification-Project"
AUTHOUR_USER_NAME = "Sp9406828091patil"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "s06.patil@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    description = "A small python package for cnn app",
    long_description = long_description,
    long_description_content_type= "text/markdown",
    author = AUTHOUR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    url = f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)