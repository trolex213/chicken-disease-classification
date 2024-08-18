import setuptools 

# read the contents of the README file
with open("README.md", "r") as f: 
    long_description = f.read()

# specify version of the package (project in this case)
__version__ = "0.0.0" 

REPO_NAME = 'chicken-disease-classification'
AUTHOR_USER_NAME = 'trolex213'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'troyz0213@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN classification of chicken diseases",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

'''so we specify which directory to look in, in this case "src". And the find_packages function simply looks within the specified "src" directory for all packages inside it as long as there contains __init__.py script inside the directory'''
