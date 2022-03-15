import setuptools
from ran import fs

setuptools.setup(
    name='typejson',
    version='0.0.1',
    description='yet a type json library.',
    long_description=fs.load('readme.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/chenshenchao/typejson',
    keywords='type json library',
    license='MIT',
    author='chenshenchao',
    author_email='chenshenchao@outlook.com',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=setuptools.find_packages(
        exclude=['demos', 'tests']
    ),
    extras_require={
        'mysql': [
            'pymysql>=1.0.2',
        ],
        'mongo': [
            'pymongo>=4.0.2',
        ],
    }
)