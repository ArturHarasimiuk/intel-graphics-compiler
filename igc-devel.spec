Name: intel-graphics-compiler-devel
Version: 1.0
Release: 1%{?dist}
Summary: Development package for Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: https://github.com/intel/intel-graphics-compiler/archive/65bbbe3ea8afb2d40ef759a51a358b4795860ce0/igc.tar.gz
# Source1: https://github.com/intel/opencl-clang/archive/9b2473dc76bca8e58bf90e859a87f97ed1ca962c/opencl-clang.tar.gz
# Source2: https://github.com/intel/llvm-patches/archive/7ac2c8a04178cf90365eeba15c63028a26409de0/llvm-patches.tar.gz
# Source3: https://github.com/llvm-mirror/llvm/archive/release_40/llvm-40.tar.gz
# Source4: https://github.com/llvm-mirror/clang/archive/release_40/clang-40.tar.gz
# Source5: https://github.com/KhronosGroup/OpenCL-Headers/archive/master/opencl-headers.tar.gz

BuildRequires: cmake clang gcc-c++ ninja-build make procps flex bison python2
# Requires:

%description


%prep


%build
echo "==== BUILD ===="
rm -rf *

mkdir intel-graphics-compiler common_clang llvm_patches opencl_headers llvm_source clang_source
tar xzf $RPM_SOURCE_DIR/igc.tar.gz -C intel-graphics-compiler --strip-components=1
# tar xzf $RPM_SOURCE_DIR/opencl-clang.tar.gz -C common_clang --strip-components=1
# tar xzf $RPM_SOURCE_DIR/llvm-patches.tar.gz -C llvm_patches --strip-components=1
# tar xzf $RPM_SOURCE_DIR/opencl-headers.tar.gz -C opencl_headers --strip-components=1
# tar xzf $RPM_SOURCE_DIR/llvm-40.tar.gz -C llvm_source --strip-components=1
# tar xzf $RPM_SOURCE_DIR/clang-40.tar.gz -C clang_source --strip-components=1

mkdir build
cd build
# cmake ../intel-graphics-compiler -DCMAKE_BUILD_TYPE=Release
# make -j`nproc` igc_dll fcl_dll


%install
echo "==== INSTALL ===="

mkdir -p $RPM_BUILD_ROOT/usr/include/igc
cp -av $RPM_BUILD_DIR/intel-graphics-compiler/IGC/AdaptorOCL/* $RPM_BUILD_ROOT/usr/include/igc/
find $RPM_BUILD_ROOT/usr/include/igc/ -type f \! -iname \*.h | xargs -n 1 rm -f
rm -rf $RPM_BUILD_ROOT/usr/include/igc/CLElfLib

find $RPM_BUILD_ROOT/usr/include/igc -type d 

echo "==== DONE ===="

%files
%defattr(-,root,root)
/usr/include/igc/*


# %doc


# %changelog
