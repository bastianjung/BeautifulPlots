import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    setuptools.setup(
            name="BeautifulPlots",
            version="0.1.0",
            author="Bastian Jung",
            author_email="jungb@student.chalmers.se",
            description="Making matplotlib look a little nicer",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/bastianjung/BeautifulPlots",
            project_urls={},
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                ],
            #package_dir={"": "BeautifulPlots"},
            packages=setuptools.find_packages(),
            python_requires=">=3.6",
            include_package_data=True
            )
