from setuptools import setup, find_packages


setup(
    name='Ideal Django',
    version='0.1',
    license='MIT',
    author="Amir Shahsafi",
    author_email='meshahsafi@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mrShahsafi/ideal-django',
    keywords='Ideal Dj project template for lazies like me :D',
    install_requires=[
      ],

)