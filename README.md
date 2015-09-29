# inez
You'll need to get your local dev environment up and running, below is how.

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Set up Docker:
```
~$ brew tap phinze/homebrew-cask
~$ brew install brew-cask
~$ brew cask install virtualbox
~$ brew install boot2docker
~$ brew install boot
```
Then do:<br>
```
~$ boot2docker init
```
which creates a `boot2docker` VM. Then, start up the VM:<br>
```
~$ boot2docker up
```
Set the docker environment variables:<br>
```
~$ eval "$(boot2docker shellinit)"
```
Make sure docker is working properly:
```
~$ docker version
```
Now, the fun part, build a container:<br>
```
~$ git clone git@github.com:alphamanimal/inez.git
~$ cd inez
~$ docker build -t inez .
```
Run:<br>
```
~$ docker run -d \   
              --name=www \
              -p 8080:5000  \
              -v /path/to/inez/:/src \   
              inez
```
Note: the `-v` flag will map your local directory to the source in the container. This way when you make a change to the source code locally, you don't need to rebuild and run the container<br> 
The above run command will also forward port 5000 to 8080.<br>
Now, you can render the project in your browser:
```
~$ open http://$(boot2docker ip):8080
```
Some other helpful docker stuff, like listing all containers:<br>
```
~$ docker ps -l
```
Stop all running containers:<br>
```
~$ docker stop $(docker ps -a -q)
```
Removing this container:<br>
```
~$ docker rm www
```
