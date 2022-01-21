# from setuptools import setup, find_packages
#
#
# # with open("/Volumes/HARRISDRIVE/GitHub/OpenPIL/README.md", "r") as readme_file:
# #     readme = readme_file.read()
#
# requirements = []
#
# setup(
#     name="OpenPIL_AI",
#     version="1.0.1",
#     author="Malik Ahmed",
#     author_email="malik@openpil.org",
#     description="AI that extracts clinical drug information from Summary of Product Characteristics pdf documents. This includes information on active-substances, active-excipients, formulation, drug-drug-interactions and drug-class-interactions.",
#     long_description= "LONG_DESCRIPTION_TBC",
#     long_description_content_type="text/markdown",
#     url="https://github.com/OpenPIL/OpenPIL",
#     packages=find_packages(),
#     install_requires=requirements,
#     classifiers=[
#         # "Programming Language :: C",
#         "Programming Language :: Python :: 3",
#         "Programming Language :: Python :: 3.6",
#         "Programming Language :: Python :: 3.7",
#         "License :: OSI Approved :: Apache Software License",
#         "Programming Language :: Python :: 3.8",
#         "Programming Language :: Python :: 3.9",
#     ],
# )
#




import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content
#
#
def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]



setup(
    name="OpenPIL_AI",
    version="0.1.1",
    description="AI that extracts clinical drug information from Summary of Product Characteristics pdf documents. This includes information on active-substances, active-excipients, formulation, drug-drug-interactions and drug-class-interactions.",
    url="https://github.com/OpenPIL/OpenPIL",
    long_description=read("/Volumes/HARRISDRIVE/GitHub/OpenPIL/README.md"),
    long_description_content_type="text/markdown",
    author="Malik Ahmed",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements_dev.txt"),
    entry_points={
        "console_scripts": ["OpenPIL_AI = OpenPIL_AI.__main__:main"]
    }
    # extras_require={"test": read_requirements("requirements-test.txt")},
)

