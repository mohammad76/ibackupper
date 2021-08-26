import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='backupper',
    version='0.3',
    scripts=['backupper'],
    author="Mohammad Abdi",
    author_email="mohammad_abdi76@yahoo.com",
    description="A backup helper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    py_modules=['ecs_helper', 'docker_helper', 'slack_api'],
    install_requires=[
        'requests', 'click', 'configparser'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
