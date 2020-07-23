# Fetch System Config

This is the Git Build Package (GBP) repo for Research versions of Fetch/Freight.
All other tools (iso installer, documentation, etc), and the commercial version
of this package, are on the 'master' branch.

The latest tested fetch and freight system config debians are available from:

- http://packages.fetchrobotics/binaries/fetch-melodic-config.deb
- http://packages.fetchrobotics/binaries/freight-melodic-config.deb

However, for best results in upgrading, please follow
http://docs.fetchrobotics.com/care_and_feeding.html#updating-your-robot

# How the .debs are generated (but please use .debs above)

```bash
git clone git@github.com:fetchrobotics/fetch_robots.git # -b melodic-devel
cd fetch_robots/fetch_system_config
# If prepparing for a new release, update changelog
dch
# Bump version
dch --release
dpkg-buildpackage -us -uc
# Debians are placed in the parent directory
cd ..
ls *system*.deb
```

# TODO: catkin/standardize

This isn't a GBP anymore, it will be published to:

https://github.com/fetchrobotics-gbp/fetch_robots-release
