import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

        setuptools.setup(
                name="pretty_matplotlibstyles",
                version="0.1.0",
                author="Bastian Jung",
                author_email="jungb@student.chalmers.se",
                description="Changes the matplotlib styles to something nicer",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="https://github.com/bastianjung/MPL_Style",
                project_urls={},
                classifiers=[
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent",
                    ],
                package_dir={"": "styles"},
                packages=setuptools.find_packages(where="styles"),
                python_requires=">=3.6",
                )
