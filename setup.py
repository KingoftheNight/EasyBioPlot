from setuptools import setup
from easybioplot.__init__ import version

setup(name='easybioplot',
    version=version,
    description='A tool for drawing pictures of biology',
    url='https://github.com/KingoftheNight/EasyBioPlot',
    author='Liang YC',
    author_email='1694822092@qq.com',
    license='BSD 2-Clause',
    packages=['easybioplot'],
    entry_points={
        'console_scripts': [
        'easybioplot=easybioplot.__main__:easybioplot',
            ]
        },
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=True)