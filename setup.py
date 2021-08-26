import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ibackupper',
    version='0.3',
    scripts=['ibackupper'],
    author="Mohammad Abdi",
    author_email="mohammad_abdi76@yahoo.com",
    description="A backup helper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mohammad76/ibackupper",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests', 'click', 'boto3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
