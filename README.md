<div align="center">
  <img  src="./images/logo.png" width="300" height="300" />
</div>

<br>

> A minimal framework to automate web Actions/Plans, and run them in a containerized fashion. 

![build status](https://github.com/ayoubeddafali/sind/workflows/Python%20application/badge.svg)

### Structure

The project is composed of : 

 - **drivers/** : Contains the webdrivers for both chrome & firefox. 
 - **tests/** : Where you puts your tests. 
 - **downloads/** : An optional folder in case your selenium script will need to download/save something for the web. 
 - **Dockerfile.chrome** : Dockerfile with necessary prerequisite for chrome browser.
 - **main.py** : Entry file.
 - **Pipefile** : Dev Packages. 
 - **plan.py** : Example plan file. 
 - **start.sh** : bash script used as entrypoint for the docker image.

### Example Scenario

You will find in the current structure an example plan in the `plan.py` file. 

You can start and override the file directly, or create your custom plans in separate files. 

Don't forget to import your plan in the `main.py` file. 

```python
from plan import ExecutionPlan
..
..
..

executionPlan = ExecutionPlan(browser=driver, display=display, login=LOGIN, password=PASSWORD)
executionPlan.run(URL)
```

### Development

While on development phase, you might need to run the plan locally and see your selenium script. 

Make sure to have the following points marked. 

1. Install some tools :

```bash
$ sudo apt-get install -y xvfb xserver-xephyr
$ sudo apt-get install scrot -y
```

2. Setup environment & dependencies

```bash
$ pip install pipenv 
$ make shell
$ make install
```

3. Run your app : 

```
$ make run
```

### Run your tests 

```bash
$ make test
```

### Production

Once you've finished writing your scenario, you will then start by building a docker image : 

```bash
$ IMAGE_TAG=custom_image:1.0  make image
```

And run it like : 

```bash
$ docker run custom_image:1.0 
# Or 
$ docker run -v /tmp/screens:/home/agent/screenshots custom_image:1.0 
# Or
$ docker run -v /tmp/screens:/home/agent/screenshots -v /tmp/downloads:/home/agent/screenshots custom_image:1.0 
# You can also pass environments variables at runtime
# List can be found on the dockerfile
```

### Available Tools : 

 - selenium : Trivial
 - pyautogui : When selenium is no longer enough for slightly complex actions
 - pyscreenshot : To screen the execution state.


&copy; 2020, Ayoub Ed-dafali.

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

