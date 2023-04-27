#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-checkmate
Version  : 2.2.0
Release  : 52
URL      : https://cran.r-project.org/src/contrib/checkmate_2.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/checkmate_2.2.0.tar.gz
Summary  : Fast and Versatile Argument Checks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-checkmate-lib = %{version}-%{release}
Requires: R-backports
BuildRequires : R-backports
BuildRequires : R-data.table
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
substantial part of the package was written in C to minimize any worries
    about execution time overhead.

%package lib
Summary: lib components for the R-checkmate package.
Group: Libraries

%description lib
lib components for the R-checkmate package.


%prep
%setup -q -n checkmate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682609485

%install
export SOURCE_DATE_EPOCH=1682609485
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/checkmate/doc/tinytest.R
/usr/lib64/R/library/checkmate/doc/tinytest.Rmd
/usr/lib64/R/library/checkmate/doc/tinytest.html
/usr/lib64/R/library/checkmate/help/AnIndex
/usr/lib64/R/library/checkmate/help/aliases.rds
/usr/lib64/R/library/checkmate/help/checkmate.rdb
/usr/lib64/R/library/checkmate/help/checkmate.rdx
/usr/lib64/R/library/checkmate/help/paths.rds
/usr/lib64/R/library/checkmate/html/00Index.html
/usr/lib64/R/library/checkmate/html/R.css
/usr/lib64/R/library/checkmate/include/checkmate.h
/usr/lib64/R/library/checkmate/include/checkmate_stub.c
/usr/lib64/R/library/checkmate/tests/test-all.R
/usr/lib64/R/library/checkmate/tests/testthat/helper.R
/usr/lib64/R/library/checkmate/tests/testthat/setup.R
/usr/lib64/R/library/checkmate/tests/testthat/teardown.R
/usr/lib64/R/library/checkmate/tests/testthat/test_AssertCollection.R
/usr/lib64/R/library/checkmate/tests/testthat/test_altreps.R
/usr/lib64/R/library/checkmate/tests/testthat/test_anyInfinite.R
/usr/lib64/R/library/checkmate/tests/testthat/test_anyMissing.R
/usr/lib64/R/library/checkmate/tests/testthat/test_anyNaN.R
/usr/lib64/R/library/checkmate/tests/testthat/test_asType.R
/usr/lib64/R/library/checkmate/tests/testthat/test_assert.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkArray.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkAtomic.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkAtomicVector.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkCharacter.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkChoice.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkClass.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkComplex.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkCount.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkDataFrame.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkDataTable.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkDate.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkDisjunct.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkDouble.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkEnvironment.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkFALSE.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkFactor.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkFilesystem.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkFlag.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkFormula.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkFunction.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkInt.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkInteger.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkIntegerish.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkList.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkLogical.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkMatrix.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkMultiClass.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkNames.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkNull.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkNumber.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkNumeric.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkOS.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkPOSIXct.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkPermutation.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkR6.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkRaw.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkScalar.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkScalarNA.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkSetEqual.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkString.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkSubset.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkTRUE.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkTibble.R
/usr/lib64/R/library/checkmate/tests/testthat/test_checkVector.R
/usr/lib64/R/library/checkmate/tests/testthat/test_deparse.R
/usr/lib64/R/library/checkmate/tests/testthat/test_guessType.R
/usr/lib64/R/library/checkmate/tests/testthat/test_include.R
/usr/lib64/R/library/checkmate/tests/testthat/test_interoperability.R
/usr/lib64/R/library/checkmate/tests/testthat/test_makeFunction.R
/usr/lib64/R/library/checkmate/tests/testthat/test_matchArg.R
/usr/lib64/R/library/checkmate/tests/testthat/test_messages.R
/usr/lib64/R/library/checkmate/tests/testthat/test_qassert.R
/usr/lib64/R/library/checkmate/tests/testthat/test_qassertr.R
/usr/lib64/R/library/checkmate/tests/testthat/test_wf.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/checkmate/libs/checkmate.so
/usr/lib64/R/library/checkmate/libs/checkmate.so.avx2
/usr/lib64/R/library/checkmate/libs/checkmate.so.avx512
