Name: intel-graphics-compiler
Version: 1.0
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/ArturHarasimiuk/intel-graphics-compiler
Source0: https://github.com/intel/intel-graphics-compiler/archive/65bbbe3ea8afb2d40ef759a51a358b4795860ce0/igc.tar.gz
Source1: https://github.com/intel/opencl-clang/archive/9b2473dc76bca8e58bf90e859a87f97ed1ca962c/opencl-clang.tar.gz
Source2: https://github.com/intel/llvm-patches/archive/7ac2c8a04178cf90365eeba15c63028a26409de0/llvm-patches.tar.gz
Source3: https://github.com/llvm-mirror/llvm/archive/release_40/llvm-40.tar.gz
Source4: https://github.com/llvm-mirror/clang/archive/release_40/clang-40.tar.gz
Source5: https://github.com/KhronosGroup/OpenCL-Headers/archive/master/opencl-headers.tar.gz

BuildRequires: cmake clang gcc-c++ ninja-build make procps flex bison python2
# Requires:

%description


%prep
echo $RPM_BUILD_DIR
echo $RPM_SOURCE_DIR

nproc
free -h

# %setup -q


%build
echo "==== BUILD ===="
rm -rf *

mkdir intel-graphics-compiler common_clang llvm_patches opencl_headers llvm_source clang_source
tar xzf $RPM_SOURCE_DIR/igc.tar.gz -C intel-graphics-compiler --strip-components=1
tar xzf $RPM_SOURCE_DIR/opencl-clang.tar.gz -C common_clang --strip-components=1
tar xzf $RPM_SOURCE_DIR/llvm-patches.tar.gz -C llvm_patches --strip-components=1
tar xzf $RPM_SOURCE_DIR/opencl-headers.tar.gz -C opencl_headers --strip-components=1
tar xzf $RPM_SOURCE_DIR/llvm-40.tar.gz -C llvm_source --strip-components=1
tar xzf $RPM_SOURCE_DIR/clang-40.tar.gz -C clang_source --strip-components=1

mkdir build
cd build
cmake ../intel-graphics-compiler -DCMAKE_BUILD_TYPE=Release
make -j`nproc` igc_dll fcl_dll


%install
echo "==== INSTALL ===="

mkdir -p $RPM_BUILD_ROOT/usr/lib64
find $RPM_BUILD_DIR/dump64 -name lib\*.so | xargs -t -n 1 -I {} cp {} $RPM_BUILD_ROOT/usr/lib64

# %make_install
echo "==== DONE ===="

%files
%defattr(-,root,root)
/usr/lib64/libiga64.so
/usr/lib64/libigc.so
/usr/lib64/libigdfcl.so
/usr/lib64/libopencl_clang.so


# %doc


# %changelog
