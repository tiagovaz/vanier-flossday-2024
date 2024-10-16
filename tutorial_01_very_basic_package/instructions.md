### Install the basic tools for this tutorial:
    $ sudo apt install build-essential devscripts debhelper tree git

### Check the content of all files in debian/ and ask questions if there's anything you don't understand.

### Build the package using dpkg-buildpackage:
    $ cd hello-flossday
    $ dpkg-buildpackage -b

### Check the content of the binary package in debian/hello-flossday
    $ tree debian/hello-flossday

### Install the generated .deb file:
    $ sudo dpkg -i ../hello-flossday_0.1-1_all.deb

### Execute a few times the tool that you have just installed:
    $ hello-flossday

### Check the content of the installed package in your system:
    $ dpkg -L hello-flossday

### Check the metadata of the installed package in your system:
    $ apt show hello-flossday
