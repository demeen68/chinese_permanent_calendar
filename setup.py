from setuptools import setup

import chinese_permanent_calendar

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="chinese_permanent_calendar",
    version=chinese_permanent_calendar.__version__,
    keywords=("chinese calendar", "calendar"),
    description="Information about Chinese perpetual calendar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="X.-Q.",
    author_email="https://github.com/demeen68/chinese_permanent_calendar",
    url="https://github.com/",
    license="MIT License",
    packages=["chinese_permanent_calendar"],
    install_requires=['pandas'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={
        'chinese_permanent_calendar': ['cp_calendar.pkl'],
    }
)
