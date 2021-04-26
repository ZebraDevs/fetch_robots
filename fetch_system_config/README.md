# Fetch System Config

This is the Git Build Package (GBP) folder the OS-level config package
for research versions of Fetch/Freight.

The latest tested fetch and freight system config debians are available from:

- http://packages.fetchrobotics/binaries/fetch-noetic-config.deb
- http://packages.fetchrobotics/binaries/freight-noetic-config.deb

However, for best results in upgrading, please follow
http://docs.fetchrobotics.com/care_and_feeding.html#updating-your-robot

# How the .debs are generated (but please use the .debs above)

```bash
git clone git@github.com:fetchrobotics/fetch_robots.git -b ros1
cd fetch_robots/fetch_system_config
# If preparing for a new release, update changelog
dch
# Bump version
dch --release
# Commit changelog
# Build the debian (which we upload to packages.fetchrobotics.com, per above)
dpkg-buildpackage -us -uc
# Debians are placed in the parent directory
cd ..
ls *system*.deb
```

# TODO: catkin/standardize

This isn't a GBP anymore, it will be published to:

https://github.com/fetchrobotics-gbp/fetch_robots-release
