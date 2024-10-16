### Add the following environment variables to your .bashrc, so that devscripts can use them for the next steps:
    DEBEMAIL="your@email"
    DEBFULLNAME="Your Name"
    export DEBEMAIL DEBFULLNAME

### Load those variables by re-running your .bashrc:
    $ . ~/.bashrc

### Edit the debian/control file in order to make the hello-flossday-ng package to "conflict" and "replace" the old hello-flossday. These fields should be added to the "Package" section. See https://www.debian.org/doc/manuals/debian-faq/pkg-basics.en.html#controlfile

### Build hello-flossday-ng package:
    $ dpkg-buildpackage -b

### Install hello-flossday-ng to your system and check the output messages. What happened here?
    $ sudo dpkg -i ../hello-flossday-ng_0.1-1_all.deb

### Edit the debian/control file and add some missing fields in the 'Source' section, such as "Standards-Version:", "Vcs-Git:" and "Vcs-Browser".

### In the "hello-flossday-ng" directory, create a new version of this package and add a new changelog entry using dch tool:
    $ dch -i

### Can you tell what the command "dch -i" did? Now add one or more changelog entries explaining how you have improved the package for this version.

### Build the new version of hello-flossday-ng package and install it:
    $ dpkg-buildpackage -b
    $ sudo dpkg -i ../hello-flossday_0.1-1.1_all.deb

### Run hello-flossday from the new package and see if the result is what you expected:
    $ hello-flossday
