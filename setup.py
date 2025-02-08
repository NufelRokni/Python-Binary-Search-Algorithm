from setuptools import setup, find_packages

setup(
    name="binary_search_project",
    version="0.1",
    packages=find_packages(where="src"),  # Looks for packages inside src/
    package_dir={"": "src"},  # src/ is the package root
    install_requires=[],  # Add dependencies here if needed
    python_requires=">=3.6",
)
