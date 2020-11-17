from setuptools import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()



setup(
    name="makedalytics",
    version='0.0.7',
    description="Python library for reproducible data analytics of dataframes, text and images",
    long_description=readme,
    long_description_content_type='text/markdown',
    author='doctormakeda@gmail.com',
    author_email='doctormakeda@gmail.com',
    maintainer='doctormakeda@gmail.com',
    maintainer_email= 'doctormakeda@gmail.com',
    url="https://github.com/drcandacemakedamoore/makedalytics",
    license="MIT",
    py_modules=["makedalytics"],
    install_requires=["pip"]
    
)
