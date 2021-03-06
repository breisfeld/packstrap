from distutils.core import setup

def main():
    setup(
        name = 'packstrap',
        packages=['packstrap'],
        package_dir = {'packstrap':'packstrap'},
        version = open('VERSION.txt').read().strip(),
        author='Mike Thornton',
        author_email='six8@devdetails.com',
        url='http://github.com/six8/packstrap',
        download_url='http://github.com/six8/packstrap',        
        keywords=['packaging'],
        license='MIT',
        description='Bootstrap new Python packages with one simple command',
        classifiers = [
            "Programming Language :: Python",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        long_description=open('README.rst').read(),
        entry_points={
            'console_scripts': [
                'packstrap = packstrap.main:main',
            ]
        },
        install_requires = [
            'Jinja2'
        ]
    )

if __name__ == '__main__':
    main()