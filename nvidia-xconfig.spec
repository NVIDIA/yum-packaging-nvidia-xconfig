%define _tar_end %{?extension}%{?!extension:bz2}

Name:           nvidia-xconfig
Version:        %{?version}%{?!version:550.70}
Release:        2%{?dist}
Summary:        NVIDIA X configuration file editor
Epoch:          3
License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  %{ix86} x86_64 ppc64le aarch64

Source0:        https://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.%{_tar_end}

BuildRequires:  gcc
BuildRequires:  m4

Requires:       nvidia-driver%{?_isa} = %{?epoch:%{epoch}:}%{version}

%description
%{name} is a command line tool intended to provide basic control over
configuration options available in the NVIDIA X driver.

%prep
%setup -q -n nvidia-xconfig-%{version}
# Remove additional CFLAGS added when enabling DEBUG
sed -i '/+= -O0 -g/d' utils.mk

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags} \
    DEBUG=1 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%install
%make_install \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%files
%if 0%{?rhel} == 6
%doc COPYING
%else
%license COPYING
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
