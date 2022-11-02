#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gitcreds
Version  : 0.1.2
Release  : 7
URL      : https://cran.r-project.org/src/contrib/gitcreds_0.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gitcreds_0.1.2.tar.gz
Summary  : Query 'git' Credentials from 'R'
Group    : Development/Tools
License  : MIT
BuildRequires : R-mockery
BuildRequires : buildreq-R

%description
store. Manage 'GitHub' tokens and other 'git' credentials. This
    package is to be used by other packages that need to authenticate to
    'GitHub' and/or other 'git' repositories.

%prep
%setup -q -n gitcreds
cd %{_builddir}/gitcreds

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662659028

%install
export SOURCE_DATE_EPOCH=1662659028
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
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
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
/usr/lib64/R/library/gitcreds/DESCRIPTION
/usr/lib64/R/library/gitcreds/INDEX
/usr/lib64/R/library/gitcreds/LICENSE
/usr/lib64/R/library/gitcreds/Meta/Rd.rds
/usr/lib64/R/library/gitcreds/Meta/features.rds
/usr/lib64/R/library/gitcreds/Meta/hsearch.rds
/usr/lib64/R/library/gitcreds/Meta/links.rds
/usr/lib64/R/library/gitcreds/Meta/nsInfo.rds
/usr/lib64/R/library/gitcreds/Meta/package.rds
/usr/lib64/R/library/gitcreds/Meta/vignette.rds
/usr/lib64/R/library/gitcreds/NAMESPACE
/usr/lib64/R/library/gitcreds/NEWS.md
/usr/lib64/R/library/gitcreds/R/gitcreds
/usr/lib64/R/library/gitcreds/R/gitcreds.rdb
/usr/lib64/R/library/gitcreds/R/gitcreds.rdx
/usr/lib64/R/library/gitcreds/doc/helper-survey.Rmd
/usr/lib64/R/library/gitcreds/doc/helper-survey.html
/usr/lib64/R/library/gitcreds/doc/index.html
/usr/lib64/R/library/gitcreds/doc/package.R
/usr/lib64/R/library/gitcreds/doc/package.Rmd
/usr/lib64/R/library/gitcreds/doc/package.html
/usr/lib64/R/library/gitcreds/help/AnIndex
/usr/lib64/R/library/gitcreds/help/aliases.rds
/usr/lib64/R/library/gitcreds/help/gitcreds.rdb
/usr/lib64/R/library/gitcreds/help/gitcreds.rdx
/usr/lib64/R/library/gitcreds/help/paths.rds
/usr/lib64/R/library/gitcreds/html/00Index.html
/usr/lib64/R/library/gitcreds/html/R.css
/usr/lib64/R/library/gitcreds/tests/testthat.R
/usr/lib64/R/library/gitcreds/tests/testthat/helper.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-cache.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-format.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-gitcreds-delete.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-gitcreds-get.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-gitcreds-list.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-gitcreds-set.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-list-helpers.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-standalone.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-username.R
/usr/lib64/R/library/gitcreds/tests/testthat/test-utils.R
