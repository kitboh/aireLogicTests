# aireLogicTests

* I have created a few different variations of testing suites for the Aire Logic cookie clicker application.
* I wanted to try creating a robot framework suite, as this is gaining popularity and I'm interested in getting to know more about it. This can be found in robotTests.
* I also created a Cypress test suite, as this is already very popular, and is a very easy way to setup a frontend testing suite. This can be found in cypressTests.
* Finally, in order to represent an example of a test suite that was the most similar to what I have used in healthcare previously I created a pytest-bdd test suite. I focused more on how I'd set this one up, than on creating a full fledged test suite, so it has a very basic means of loading data from a configuration file, as well as a means of passing data from step to step using a test context, so as to allow for future improvements allowing for parallel runs. Unfortunately, I did not create a way of dynamically generating test user names for fear of filling up my example instance again, and this would be required for parallel test runs to be stable. As it stands though, if user names had a random number applied to the end of them, and then passed through the context, the test suite could run multiple tests at once to greatly improve run speed.

* Each of the test suites should run independently, and they each contain their own README.md file to detail the run commands. Cypress requires NodeJS to run, and Robot uses Python. For the Pytest-BDD suite to run, geckodriver will need to be added to the PATH.

* All in all I spent around 2 hours each creating the Robot test suite and the Cypress Test Suite, and about 4-5 hours creating the Pytest suite.

* Furthermore, I spent around an hour manually testing the application to find bugs. Which I have raised in the /bugs folder.