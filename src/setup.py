from setuptools import setup

setup(name="tableconvert",
      version="1.0",
      description="This package simply converts pasted spreadsheet data into a numpy array",
      url="https://github.com/padix-key/tableconvert",
      author="Patrick Kunzmann",
      license="MIT",
      packages=["tableconvert"],
      install_requires=["numpy"],
      zip_safe=False)