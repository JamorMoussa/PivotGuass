from setuptools import setup, find_packages
 
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
]
 
setup(
  name='PivotGauss',
  version='1.0.1',
  description='The Gauss Elimination Methods.',
  long_description= open('README.md').read() + '\n\n',
  url='',  
  author='Moussa JAMOR',
  author_email='moussajamorsup@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Pivot Gauss, Elimination, Linear system, inverse of matrix', 
  packages=find_packages(),
  install_requires=['numpy'] 
)

