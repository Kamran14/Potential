# Potential Motors - Coding Challenge

# Output
Console output for running Unit tests:
```console
(potential) X:\Documents\Code\Coding Challenges\PotentialMotors>pytest -v testCar.py --junitxml ./report.xml
==================================================================================================================================== test session starts ===================================================================================================================================== 
platform win32 -- Python 3.7.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- x:\documents\code\coding challenges\potentialmotors\potential\scripts\python.exe
cachedir: .pytest_cache
rootdir: X:\Documents\Code\Coding Challenges\PotentialMotors
collected 5 items

testCar.py::Test::test_isMoving PASSED                                                                                                                                                                                                                                                  [ 20%] 
testCar.py::Test::test_isNotMoving PASSED                                                                                                                                                                                                                                               [ 40%] 
testCar.py::Test::test_moveForward PASSED                                                                                                                                                                                                                                               [ 60%] 
testCar.py::Test::test_moveBackward PASSED                                                                                                                                                                                                                                              [ 80%] 
testCar.py::Test::test_stop PASSED                                                                                                                                                                                                                                                      [100%] 

----------------------------------------------------------------------------------------------------- generated xml file: X:\Documents\Code\Coding Challenges\PotentialMotors\report.xml ----------------------------------------------------------------------------------------------------- 
===================================================================================================================================== 5 passed in 0.03s ====================================================================================================================================== 
```
## Screenshots

### Console
![Console Output](https://github.com/Kamran14/Potential/blob/main/screenshots/console.png)

### Jenkins
![Jenkins](https://github.com/Kamran14/Potential/blob/main/screenshots/Jenkin1.png)
![Jenkins](https://github.com/Kamran14/Potential/blob/main/screenshots/Jenkin2.png)
![Jenkins](https://github.com/Kamran14/Potential/blob/main/screenshots/Jenkin3.png)
![Jenkins](https://github.com/Kamran14/Potential/blob/main/screenshots/Jenkin4.png)

### Docker
![Docker](https://github.com/Kamran14/Potential/blob/main/screenshots/docker.png)

### Report.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<testsuites>
    <testsuite errors="0" failures="0" hostname="KamDesktop" name="pytest" skipped="0" tests="5" time="0.028" timestamp="2021-07-23T01:23:44.839209">
        <testcase classname="testCar.Test" name="test_isMoving" time="0.001" />
        <testcase classname="testCar.Test" name="test_isNotMoving" time="0.001" />
        <testcase classname="testCar.Test" name="test_moveForward" time="0.001" />
        <testcase classname="testCar.Test" name="test_moveBackward" time="0.001" />
        <testcase classname="testCar.Test" name="test_stop" time="0.001" />
    </testsuite>
</testsuites>
```



## Running the test
```console
pytest -v testCar.py --junitxml ./report.xml
```

## Instructions to install Jenkins on Docker + Tools
You can download the Jenkins container from this link: https://hub.docker.com/r/jenkins/jenkins
```console
kam@KamDesktop:$ docker pull jenkins/jenkins
kam@KamDesktop:$ docker run -p 8080:8080 -p 50000:50000 jenkins
kam@KamDesktop:$ docker run --name Potential-CodingChallenge -p 8080:8080 -p 50000:50000 -v YourPath:/var/jenkins_home jenkins
```
From here go to your working Jenkins directory that you specified for YourPath and create a file called ```Dockerfile```
```docker
FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get install -y python3 pip3
RUN pip3 install -r requirements.txt
```
Once you are done, open up terminal and write the following in the directory specified in **YourPath**: 
```console
kam@KamDesktop:$ docker build -t myjenkins .
```

## Running new Dockerfile
Now that we've built a new image with python3 and pip3 installed, we can go ahead and launch run the image
```console
kam@KamDesktop:$ docker run -p 8080:8080 --name=CodingChallenge -d --env JAVA_OPTS="-Xmx8192m" --env JENKINS_OPTS=" --handlerCountMax=300" myjenkins
```
You should now be able to connect to http://localhost:8080 and see Jenkins set up. To get the initialAdministrativePassword, open up the CLI for your 'CodingChallenge' image and navigate to ```/var/jenkins_home/secrets/initialAdminPassword``` Or you can just read the file from /:
```console
# cat /var/jenkins_home/secrets/initialAdminPassword 
```
