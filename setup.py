from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'UniversalWrapper',
  packages = ['universalwrapper', 'uw'],
  version = '2.4',
  license='MIT',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Bas de Bruijne',
  author_email = 'basdbruijne@gmail.com',
  url = 'https://github.com/Basdbruijne/UniversalWrapper',
  keywords = ['wrapper', 'cli', 'subprocess'],
  install_requires = ['autothread', 'pyyaml'],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/ Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
