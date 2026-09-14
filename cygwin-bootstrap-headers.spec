Name:           cygwin-bootstrap-headers
Version:        1.0.0
Release:        1%{?dist}
Summary:        Cygwin headers for cross-compiler bootstrap build

License:        GPL-3.0-or-later
Group:          Development/Libraries
URL:            https://cygwin.com/
BuildArch:      noarch

# downloaded and extracted by get-sources.sh
Source0:        fake-cygwin-includes.patch

BuildRequires:  cygwin32-filesystem >= 7
BuildRequires:  cygwin64-filesystem >= 7
BuildRequires:  cygwin-aarch64-filesystem

%description
Cygwin headers for cross-compiler bootstrap build

%package -n cygwin32-bootstrap-headers
Summary:    Cygwin x86 headers for bootstrap build

%description -n cygwin32-bootstrap-headers
Cygwin x86 headers for bootstrap build


%package -n cygwin64-bootstrap-headers
Summary:    Cygwin x86_64 headers for bootstrap build

%description -n cygwin64-bootstrap-headers
Cygwin x86_64 cross-compiler runtime

%package -n cygwin-aarch64-bootstrap-headers
Summary:    Cygwin aarch64 headers for bootstrap build

%description -n cygwin-aarch64-bootstrap-headers
Cygwin aarch64 headers for bootstrap build

%prep

%build

%install
# Fakery necessary to compile a bootstrap cygwin-gcc and then w32api-runtime and
# minimal cygwin runtime with it. This just fakes the bare minimum we need. (It
# might be better just to use a copy of the real headers here?).
for d in \
    %{cygwin32_includedir} \
    %{cygwin64_includedir} \
    %{cygwin_aarch64_includedir}
do
    mkdir -p $RPM_BUILD_ROOT${d}
    patch -d $RPM_BUILD_ROOT${d} -p1 <%{SOURCE0}
done

%files -n cygwin32-bootstrap-headers
%{cygwin32_includedir}/*

%files -n cygwin64-bootstrap-headers
%{cygwin64_includedir}/*

%files -n cygwin-aarch64-bootstrap-headers
%{cygwin_aarch64_includedir}/*

%changelog
* Mon Sep 14 2026 Jon Turney <jon.turney@dronecode.org.uk> - 1.0.0-1
- initial version
