#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-checkmate
Version  : 1.8.5
Release  : 4
URL      : https://cran.r-project.org/src/contrib/checkmate_1.8.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/checkmate_1.8.5.tar.gz
Summary  : Fast and Versatile Argument Checks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-checkmate-lib
Requires: R-backports
Requires: R-evaluate
Requires: R-fastmatch
Requires: R-markdown
Requires: R-stringi
BuildRequires : R-backports
BuildRequires : R-evaluate
BuildRequires : R-fastmatch
BuildRequires : R-markdown
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
substantial part of the package was written in C to minimize any worries
    about execution time overhead.

%package lib
Summary: lib components for the R-checkmate package.
Group: Libraries

%description lib
lib components for the R-checkmate package.


%prep
%setup -q -c -n checkmate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523293856

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523293856
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library checkmate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library checkmate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library checkmate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library checkmate|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/checkmate/CITATION
/usr/lib64/R/library/checkmate/DESCRIPTION
/usr/lib64/R/library/checkmate/INDEX
/usr/lib64/R/library/checkmate/LICENSE
/usr/lib64/R/library/checkmate/Meta/Rd.rds
/usr/lib64/R/library/checkmate/Meta/features.rds
/usr/lib64/R/library/checkmate/Meta/hsearch.rds
/usr/lib64/R/library/checkmate/Meta/links.rds
/usr/lib64/R/library/checkmate/Meta/nsInfo.rds
/usr/lib64/R/library/checkmate/Meta/package.rds
/usr/lib64/R/library/checkmate/Meta/vignette.rds
/usr/lib64/R/library/checkmate/NAMESPACE
/usr/lib64/R/library/checkmate/NEWS.md
/usr/lib64/R/library/checkmate/R/checkmate
/usr/lib64/R/library/checkmate/R/checkmate.rdb
/usr/lib64/R/library/checkmate/R/checkmate.rdx
/usr/lib64/R/library/checkmate/doc/checkmate.R
/usr/lib64/R/library/checkmate/doc/checkmate.Rmd
/usr/lib64/R/library/checkmate/doc/checkmate.html
/usr/lib64/R/library/checkmate/doc/index.html
/usr/lib64/R/library/checkmate/help/AnIndex
/usr/lib64/R/library/checkmate/help/aliases.rds
/usr/lib64/R/library/checkmate/help/checkmate.rdb
/usr/lib64/R/library/checkmate/help/checkmate.rdx
/usr/lib64/R/library/checkmate/help/paths.rds
/usr/lib64/R/library/checkmate/html/00Index.html
/usr/lib64/R/library/checkmate/html/R.css
/usr/lib64/R/library/checkmate/include/checkmate.h
/usr/lib64/R/library/checkmate/include/checkmate_stub.c
/usr/lib64/R/library/checkmate/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/checkmate/libs/checkmate.so
/usr/lib64/R/library/checkmate/libs/checkmate.so.avx2
/usr/lib64/R/library/checkmate/libs/checkmate.so.avx512
