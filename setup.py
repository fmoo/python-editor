__VERSION__ = '1.0.2'

from setuptools import setup
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = None

setup(
    name='python-editor',
    version=__VERSION__,
    description="Programmatically open an editor, capture the result.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='editor library vim emacs',
    author='Peter Ruibal',
    author_email='ruibalp@gmail.com',
    url='https://github.com/fmoo/python-editor',
    license='Apache',
    py_modules=[
        'editor',
    ],
    requires=[
        #'six',
    ],
)
