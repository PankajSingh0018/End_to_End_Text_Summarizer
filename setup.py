# local package installation 

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ ="0.0.1"

REPO_NAME= "End_to_End_Text_Summarizer"
AUTHOR_USER_NAME ="PankajSingh0018"
SRC_REPO= "Text-Summarizer"
AUTHOR_EMAIL= "singh.pankaj0018@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,  
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where="src"),


)