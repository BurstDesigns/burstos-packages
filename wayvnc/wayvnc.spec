%global aml_version 1.0.0
%global nvnc_version 1.0.4

Name:           wayvnc
Version:        0.10.2
Release:        1%{?dist}
Summary:        A VNC server for wlroots based Wayland compositors
License:        ISC AND BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/any1/wayvnc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/any1/aml/archive/v%{aml_version}/aml-%{aml_version}.tar.gz
Source2:        https://github.com/any1/neatvnc/archive/v%{nvnc_version}/neatvnc-%{nvnc_version}.tar.gz
Patch0:         force-wlr-screencopy.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  scdoc
BuildRequires:  turbojpeg-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon) >= 1.0.0
BuildRequires:  pkgconfig(zlib)

Requires:       (sway >= 1.6 if sway)
Provides:       bundled(aml) = %{aml_version}
Provides:       bundled(neatvnc) = %{nvnc_version}

%description
VNC server for wlroots-based Wayland compositors.
neatvnc %{nvnc_version} and aml %{aml_version} built in (static).
Patched to force wlr-screencopy over ext-image-copy-capture.

%prep
%autosetup -p1
mkdir -p subprojects/aml subprojects/neatvnc
tar -xzf %{SOURCE1} -C subprojects/aml --strip-components=1
tar -xzf %{SOURCE2} -C subprojects/neatvnc --strip-components=1
cp -p subprojects/aml/COPYING COPYING.aml
cp -p subprojects/neatvnc/COPYING COPYING.neatvnc

%build
%meson \
    -Daml:default_library=static \
    -Dneatvnc:default_library=static
%meson_build

%install
%meson_install --skip-subprojects

%check
%meson_test

%files
%license COPYING COPYING.aml COPYING.neatvnc
%doc README.md FAQ.md
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}ctl.1.*

%changelog
* Fri Nov 13 2026 <Maxime Rouleau-Villeneuve> - 0.10.2-1
- Force wlr-screencopy over ext-image-copy-capture (MangoWM compat)
