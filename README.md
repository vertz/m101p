MongoDB for Developers
=====

Week 1: Introduction & Overview

Week 2: CRUD (Creating, Reading and Updating Data)

Week 3: Schema Design

Week 4: Performance

Week 5: Aggregation Framework 

Week 6: Application Engineering

Week 7: Case Studies 

### <a href = "http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/">Install MongoDB on Ubuntu</a>

The Ubuntu package management tool (i.e. dpkg and apt) ensure package consistency and authenticity by requiring that distributors sign packages with GPG keys. Issue the following command to import the MongoDB public GPG Key:

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
```
Create a /etc/apt/sources.list.d/mongodb.list file using the following command.
```
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
```
Now issue the following command to reload your repository:
```
sudo apt-get update
```

#### Install Packages

Issue the following command to install the latest stable version of MongoDB:
```
sudo apt-get install mongodb-10gen
```
When this command completes, you have successfully installed MongoDB! Continue for configuration and start-up suggestions.

#### Manage Installed Versions

You can use the mongodb-10gen package to install previous versions of MongoDB. To install a specific release, append the version number to the package name, as in the following example:
```
apt-get install mongodb-10gen=2.2.3
```
This will install the 2.2.3 release of MongoDB. You can specify any available version of MongoDB; however apt-get will upgrade the mongodb-10gen package when a newer version becomes available. Use the following pinning procedure to prevent unintended upgrades.

To pin a package, issue the following command at the system prompt to pin the version of MongoDB at the currently installed version:
```
echo "mongodb-10gen hold" | sudo dpkg --set-selections
```

#### Run MongoDB

The MongoDB instance stores its data files in the /var/lib/mongo and its log files in /var/log/mongo, and run using the mongod user account. If you change the user that runs the MongoDB process, you must modify the access control rights to the /var/lib/mongo and /var/log/mongo directories.

##### Start MongoDB
You can start the mongod process by issuing the following command:
```
sudo service mongodb start
```
You can verify that mongod has started successfully by checking the contents of the log file at /var/log/mongodb/mongodb.log.
##### Stop MongoDB
As needed, you may stop the mongod process by issuing the following command:
```
sudo service mongodb stop
```
##### Restart MongoDB
You may restart the mongod process by issuing the following command:
```
sudo service mongodb restart
```

### <a href = "http://www.pip-installer.org/en/latest/installing.html">Install pip on Ubuntu</a>

```
sudo apt-get install python-pip
```

### <a href = "http://api.mongodb.org/python/current/installation.html">Installing / Upgrading — PyMongo</a>

We prefer pip to install pymongo on platforms other than Windows:
```
sudo pip install pymongo
```

To get a specific version of pymongo:
```
sudo pip install pymongo==2.1.1
```

To upgrade using pip:
```
sudo pip install --upgrade pymongo
```

### <a href = "http://bottlepy.org/docs/dev/tutorial.html">Install Bottle on Ubuntu</a>

Bottle does not depend on any external libraries. You can just download bottle.py into your project directory and start coding:
```
$ wget http://bottlepy.org/bottle.py
```

This will get you the latest development snapshot that includes all the new features. If you prefer a more stable environment, you should stick with the stable releases. These are available on PyPI and can be installed via pip (recommended), easy_install or your package manager:
```
$ sudo pip install bottle              # recommended
$ sudo easy_install bottle             # alternative without pip
$ sudo apt-get install python-bottle   # works for debian, ubuntu, ...
```

Either way, you’ll need Python 2.5 or newer (including 3.x) to run bottle applications. If you do not have permissions to install packages system-wide or simply don’t want to, create a virtualenv first:
```
$ virtualenv develop              # Create virtual environment
$ source develop/bin/activate     # Change default python to virtual one
(develop)$ pip install -U bottle  # Install bottle to virtual environment
```

Or, if virtualenv is not installed on your system:
```
$ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
$ python virtualenv.py develop    # Create virtual environment
$ source develop/bin/activate     # Change default python to virtual one
(develop)$ pip install -U bottle  # Install bottle to virtual environment
```

