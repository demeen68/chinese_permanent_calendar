from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="chinese_permanent_calendar",
    version='0.1.0',
    keywords=["chinese calendar", "calendar"],
    description="Information about Chinese perpetual calendar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="X.-Q.",
    url="https://github.com/demeen68/chinese_permanent_calendar",
    license="MIT License",
    packages=["chinese_permanent_calendar"],
    install_requires=['pandas'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={
        'chinese_permanent_calendar': ['cp_calendar.csv.gz'],
    }
)
