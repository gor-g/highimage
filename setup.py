from setuptools import setup, find_packages

setup(
    name='himage',
    version='0.0.4',
    description='A small library, of high level image processing tools',
    url='https://github.com/mySpecialUsername/highImage/',
    author='Gor G.',
    packages=find_packages(),
    install_requires=['numpy', 'opencv-python', 'matplotlib', 'PyQt6'],
    python_requires='>=3.6',
    zip_safe=False
)
