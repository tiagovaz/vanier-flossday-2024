### Add the following environment variables to your .bashrc, so that devscripts can use them for the next steps:
    DEBEMAIL="your@email"
    DEBFULLNAME="Your Name"
    export DEBEMAIL DEBFULLNAME

### Load those variables by re-running your .bashrc:
    $ . ~/.bashrc

### Edit the debian/control file in order to make this hello-flossday-ng package to "conflict" and "replace" the old hello-flossday.

### Build hello-flossday-ng package:
    $ dpkg-buildpackage -b

### Try to install hello-flossday-ng to your system:
    $ sudo dpkg -i ../hello-flossday_0.1-1_all.deb

### Uninstall the old hello-flossday package from your system and try again to install your new package:
    $ sudo apt remove hello-flossday
    $ sudo dpkg -i ../hello-flossday-ng_0.1-1_all.deb

### Edit the debian/control file and add some missing fields in the 'Source' section, such as "Standards-Version:", "Vcs-Git:" and "Vcs-Browser".

### In the "hello-flossday-ng" directory, create a new version of this package and add a new changelog entry using dch tool:
    $ dch -i
Then add one or more entries explaining how you have improved the package for this version.

### Build the new version of hello-flossday-ng package and install it:
    $ dpkg-buildpackage -b
    $ sudo dpkg -i ../hello-flossday_0.1-2_all.deb

### Run hello-flossday from the new package and see if the result is what you expected:
    $ hello-flossday
