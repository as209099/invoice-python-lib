from setuptools import setup

def get_readme():
   with open('README.md', 'r') as file:
      return file.read()

setup(
   name='invoice',
   version='1.0.1',
   description='中華民國財政部統一發票',
   long_description=get_readme(),
   long_description_content_type="text/markdown",
   author='as209099',
   author_email='as209099@gmail.com',
   packages=['invoice'],
   python_requires='>=3.6',
   url='https://github.com/as209099/invoice-python-lib',
   license='MIT',
   install_requires=['aiohttp', 'beautifulsoup4'],
   classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
   ],
)