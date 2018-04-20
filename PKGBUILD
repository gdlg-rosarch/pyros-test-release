# Script generated with Bloom
pkgdesc="ROS - Basic test nodes for Pyros dynamic ROS interface"


pkgname='ros-lunar-pyros-test'
pkgver='0.0.6_2'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.6.18'
'ros-lunar-message-generation>=0.2.10'
'ros-lunar-roslint>=0.10.0'
'ros-lunar-rospy>=1.11.19'
'ros-lunar-rostest>=1.11.19'
'ros-lunar-rostopic>=1.11.19'
'ros-lunar-rosunit>=1.11.12'
'ros-lunar-std-msgs>=0.5.9'
)

depends=('ros-lunar-message-runtime>=0.4.12'
'ros-lunar-rospy>=1.11.19'
'ros-lunar-std-msgs>=0.5.9'
)

conflicts=()
replaces=()

_dir=pyros_test
source=()
md5sums=()

prepare() {
    cp -R $startdir/pyros_test $srcdir/pyros_test
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

