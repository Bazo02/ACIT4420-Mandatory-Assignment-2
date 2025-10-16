from setuptools import setup, find_packages

setup(
    name="study_reminder_system",
    version="1.0.0",
    description="A study reminder system for students with scheduling and logging.",
    author="Alexander Bazo",
    packages=find_packages(),
    install_requires=[
        "schedule"
    ],
    entry_points={
        "console_scripts": [
            "study-reminder=main:main"
        ]
    },
    python_requires=">=3.6",
    include_package_data=True,
)