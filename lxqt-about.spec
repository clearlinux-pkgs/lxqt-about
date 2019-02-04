#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x42C9C8D3AF5EA5E3 (agaida@siduction.org)
#
Name     : lxqt-about
Version  : 0.14.0
Release  : 1
URL      : https://downloads.lxqt.org/downloads/lxqt-about/0.14.0/lxqt-about-0.14.0.tar.xz
Source0  : https://downloads.lxqt.org/downloads/lxqt-about/0.14.0/lxqt-about-0.14.0.tar.xz
Source99 : https://downloads.lxqt.org/downloads/lxqt-about/0.14.0/lxqt-about-0.14.0.tar.xz.asc
Summary  : LXQt about dialog.
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-about-bin = %{version}-%{release}
Requires: lxqt-about-data = %{version}-%{release}
Requires: lxqt-about-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools

%description
# lxqt-about
## Overview
`lxqt-about` is a dialogue window providing information about LXQt and the
system it's running on.

%package bin
Summary: bin components for the lxqt-about package.
Group: Binaries
Requires: lxqt-about-data = %{version}-%{release}
Requires: lxqt-about-license = %{version}-%{release}

%description bin
bin components for the lxqt-about package.


%package data
Summary: data components for the lxqt-about package.
Group: Data

%description data
data components for the lxqt-about package.


%package license
Summary: license components for the lxqt-about package.
Group: Default

%description license
license components for the lxqt-about package.


%prep
%setup -q -n lxqt-about-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549313579
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549313579
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-about
cp COPYING %{buildroot}/usr/share/package-licenses/lxqt-about/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-about

%files data
%defattr(-,root,root,-)
/usr/share/applications/lxqt-about.desktop
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ar.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ca.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_cs.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_cy.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_da.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_de.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_el.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_eo.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_es.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_es_VE.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_eu.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_fi.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_fr.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_gl.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_he.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_hu.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ia.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_id.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_it.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ja.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ko.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_lt.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_lv.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_nb_NO.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_nl.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_pl.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_pt.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_pt_BR.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ro_RO.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_ru.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_sk_SK.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_sl.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_sr@latin.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_sr_RS.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_th_TH.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_tr.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_uk.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_zh_CN.qm
/usr/share/lxqt/translations/lxqt-about/lxqt-about_zh_TW.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-about/COPYING
