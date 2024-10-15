### Download the source package 'screen-message'. Go to https://tracker.debian.org/ and look for 'screen-message'. Find the DSC link, copy it and use dget to download the package source.

### Choose one of the following tasks that will help improving the 'screen-message' package:

#### [EASY] Another needed fix for this package is that it depends on a deprecated package 'pkg-config'. This package has been renamed to 'pkgconf'. You can modify the 'control' file and apply this fix easily.

#### [INTERMEDIATE] This package needs someone to convert its 'copyright' file to a machine-readable one as described in https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/

#### [ADVANCED] The package should be updated to follow the last version of Debian Policy (Standards-Version 4.7.0 instead of 4.6.0.1). Before updating the Standards-Version value in the 'control' file, you need to check the Policy changelog and see if the package is affected by one of them. See https://www.debian.org/doc/debian-policy/

### Create a new version of this package adding your changes in 'changelog' file using the dch tool.

### Build, install and test the new version of the package.

### If you feel confident with your changes, send a patch to the Debian BTS or open and attach your patch to a gitlab issue at https://salsa.debian.org/debian/sm
