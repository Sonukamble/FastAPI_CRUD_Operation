from setuptools import setup, find_packages

# Load the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jwt_token",  # Replace with your own project name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A FastAPI project with JWT token authentication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fastapi_project",  # Replace with your own project URL
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "SQLAlchemy",
        "mysql-connector-python",
        "python-dotenv",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "fastapi_project=main:app",  # Replace with the entry point of your application
        ],
    },
)
