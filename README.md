# Potential Motors - Coding Challenge

# Running the test
```console
pytest testCar.py --junitxml ./report.xml
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
Once you are done, open up terminal and write the following in the specified directory: 
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
