# Fetch System Config

This is the Git Build Package (GBP) repo for Research versions of Fetch/Freight.
All other tools (iso installer, documentation, etc), and the commercial version
of this package, are on the 'master' branch.

# How to Manually Build

```bash
git clone git@github.com:fetchrobotics/fetch_binary_drivers.git # -b melodic-devel
cd fetch_binary_drivers/fetch-system-config
dpkg-buildpackage -us -uc
# Debians are placed in the parent directory
cd ..
ls *system*.deb
```

