import setuptools

setuptools.setup(
   name='flake8-picky',
   license='MIT',
   version='0.0.1',
   description='Plugin to comply with my picky standards',
   author='Valdir Stumm Junior',
   author_email='stummjr@gmail.com',
   url='http://github.com/stummjr/flake8-picky',
   py_modules=['flake8_picky'],
   entry_points={
       'flake8.extension': [
           'PCK0 = picky_checker:PickyChecker',
       ],
   },
   install_requires=['flake8'],
   classifiers=[
       'Topic :: Software Development :: Quality Assurance',
   ],
)
