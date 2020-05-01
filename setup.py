import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pylayers_gis',
     version='0.3',
     author="Bernard Uguen",
     author_email="bernard.uguen@univ-rennes1.fr",
     description="A pylayers set of gis and osm classes',
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=['pylayers_project','pylayers_project.tests'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
