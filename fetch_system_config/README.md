# Fetch System Config

This is the Git Build Package (GBP) repo for Research versions of Fetch/Freight.
All other tools (iso installer, documentation, etc), and the commercial version
of this package, are on the 'master' branch.

# How to Manually Build

```bash
git clone git@github.com:fetchrobotics/fetch_robots.git # -b melodic-devel
cd fetch_robots/fetch_system_config
# Optionally auto-update changelog via git commits
gbp dch --release
dpkg-buildpackage -us -uc
# Debians are placed in the parent directory
cd ..
ls *system*.deb
```

# TODO: catkin/standardize

This isn't a GBP anymore, it will be published to:

https://github.com/fetchrobotics-gbp/fetch_robots-release
