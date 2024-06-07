from setuptools import setup, find_packages

setup(
    name='r_like',
    version='0.1',
    packages=find_packages(),
    description='A Python library mimicking some of R\'s functionality.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/YOUR_GITHUB_USERNAME/r_like',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'matplotlib',  # Required for plotting functionality
gi        # might add, 'numpy', 'pandas', etc.
    ],
)