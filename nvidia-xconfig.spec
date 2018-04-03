Name:           nvidia-xconfig
Version:        390.48
Release:        1%{?dist}
Summary:        NVIDIA X configuration file editor
Epoch:          3
License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  %{ix86} x86_64

Source0:        https://github.com/NVIDIA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.0-default.patch

BuildRequires:  m4

%description
%{name} is a command line tool intended to provide basic control over
configuration options available in the NVIDIA X driver.

%prep
%setup -q
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
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Tue Apr 03 2018 Simone Caronni <negativo17@gmail.com> - 3:390.48-1
- Update to 390.48.

* Thu Mar 15 2018 Simone Caronni <negativo17@gmail.com> - 3:390.42-1
- Update to 390.42.

* Tue Feb 27 2018 Simone Caronni <negativo17@gmail.com> - 3:390.25-2
- Align Epoch with other components.

* Tue Jan 30 2018 Simone Caronni <negativo17@gmail.com> - 2:390.25-1
- Update to 390.25.

* Fri Jan 19 2018 Simone Caronni <negativo17@gmail.com> - 2:390.12-1
- Update to 390.12.

* Tue Nov 28 2017 Simone Caronni <negativo17@gmail.com> - 2:387.34-1
- Update to 387.34.

* Tue Oct 31 2017 Simone Caronni <negativo17@gmail.com> - 2:387.22-1
- Update to 387.22.

* Thu Oct 05 2017 Simone Caronni <negativo17@gmail.com> - 2:387.12-1
- Update to 387.12.

* Fri Sep 22 2017 Simone Caronni <negativo17@gmail.com> - 2:384.90-1
- Update to 384.90.

* Wed Aug 30 2017 Simone Caronni <negativo17@gmail.com> - 2:384.69-1
- Update to 384.69.
- Update SPEC file to get the proper flags on Fedora 27.

* Tue Jul 25 2017 Simone Caronni <negativo17@gmail.com> - 2:384.59-1
- Update to 384.59.

* Wed May 10 2017 Simone Caronni <negativo17@gmail.com> - 2:381.22-1
- Update to 381.22.

* Fri Apr 07 2017 Simone Caronni <negativo17@gmail.com> - 2:381.09-1
- Update to 381.09.

* Wed Feb 15 2017 Simone Caronni <negativo17@gmail.com> - 2:378.13-1
- Update to 378.13.

* Thu Jan 19 2017 Simone Caronni <negativo17@gmail.com> - 2:378.09-1
- Update to 378.09.

* Thu Dec 15 2016 Simone Caronni <negativo17@gmail.com> - 2:375.26-1
- Update to 375.26.

* Sat Nov 19 2016 Simone Caronni <negativo17@gmail.com> - 2:375.20-1
- Update to 375.20.

* Sat Oct 22 2016 Simone Caronni <negativo17@gmail.com> - 2:375.10-1
- Update to 375.10.

* Fri Sep 09 2016 Simone Caronni <negativo17@gmail.com> - 2:370.28-1
- Update to 370.28.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 2:370.23-1
- Update to 370.23.

* Fri Jul 22 2016 Simone Caronni <negativo17@gmail.com> - 2:367.35-1
- Update to 367.35.

* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 2:367.27-1
- Update to 367.27.

* Thu May 26 2016 Simone Caronni <negativo17@gmail.com> - 2:367.18-1
- Update to 367.18.

* Mon May 02 2016 Simone Caronni <negativo17@gmail.com> - 2:364.19-1
- Update to 364.19.

* Fri Apr 08 2016 Simone Caronni <negativo17@gmail.com> - 2:364.15-1
- Update to 364.15.

* Tue Mar 22 2016 Simone Caronni <negativo17@gmail.com> - 2:364.12-1
- Update to 364.12.
- Update make parameters.

* Tue Feb 09 2016 Simone Caronni <negativo17@gmail.com> - 2:361.28-1
- Update to 361.28.

* Thu Jan 14 2016 Simone Caronni <negativo17@gmail.com> - 2:361.18-1
- Update to 361.18.

* Tue Jan 05 2016 Simone Caronni <negativo17@gmail.com> - 2:361.16-1
- Update to 361.16.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 2:358.16-1
- Update to 358.16.

* Tue Oct 13 2015 Simone Caronni <negativo17@gmail.com> - 2:358.09-1
- Update to 358.09.

* Tue Sep 01 2015 Simone Caronni <negativo17@gmail.com> - 2:355.11-1
- Update to 355.11.

* Tue Aug 04 2015 Simone Caronni <negativo17@gmail.com> - 2:355.06-1
- Update to 355.06.

* Wed Jul 29 2015 Simone Caronni <negativo17@gmail.com> - 2:352.30-1
- Update to 352.30.

* Wed Jun 17 2015 Simone Caronni <negativo17@gmail.com> - 2:352.21-1
- Update to 352.21.

* Tue May 19 2015 Simone Caronni <negativo17@gmail.com> - 2:352.09-1
- Update to 352.09.

* Wed May 13 2015 Simone Caronni <negativo17@gmail.com> - 2:346.72-1
- Update to 346.72.

* Tue Apr 07 2015 Simone Caronni <negativo17@gmail.com> - 2:346.59-1
- Update to 346.59.

* Wed Feb 25 2015 Simone Caronni <negativo17@gmail.com> - 2:346.47-1
- Update to 346.47.
- Add license macro.

* Sat Jan 17 2015 Simone Caronni <negativo17@gmail.com> - 2:346.35-1
- Update to 346.35.

* Tue Dec 09 2014 Simone Caronni <negativo17@gmail.com> - 2:346.22-1
- Update to 346.22.

* Fri Nov 14 2014 Simone Caronni <negativo17@gmail.com> - 2:346.16-1
- Update to 346.16.

* Mon Sep 22 2014 Simone Caronni <negativo17@gmail.com> - 2:343.22-1
- Update to 343.22.

* Thu Aug 07 2014 Simone Caronni <negativo17@gmail.com> - 2:343.13-1
- Update to 343.13.

* Tue Jul 08 2014 Simone Caronni <negativo17@gmail.com> - 2:340.24-1
- Update to 340.24.

* Mon Jun 09 2014 Simone Caronni <negativo17@gmail.com> - 2:340.17-1
- Update to 340.17.

* Mon Jun 02 2014 Simone Caronni <negativo17@gmail.com> - 2:337.25-1
- Update to 337.25.

* Tue May 06 2014 Simone Caronni <negativo17@gmail.com> - 2:337.19-1
- Update to 337.19.

* Tue Apr 08 2014 Simone Caronni <negativo17@gmail.com> - 2:337.12-1
- Update to 337.12.

* Tue Mar 04 2014 Simone Caronni <negativo17@gmail.com> - 2:334.21-1
- Update to 334.21.

* Wed Feb 19 2014 Simone Caronni <negativo17@gmail.com> - 2:331.49-1
- Update to 331.49.

* Tue Jan 14 2014 Simone Caronni <negativo17@gmail.com> - 2:331.38-1
- Update to 331.38.

* Mon Dec 23 2013 Simone Caronni <negativo17@gmail.com> - 2:331.20-2
- Do not strip binaries during build, let rpm generate debuginfo files.

* Thu Nov 07 2013 Simone Caronni <negativo17@gmail.com> - 2:331.20-1
- Update to 331.20.

* Wed Oct 23 2013 Simone Caronni <negativo17@gmail.com> - 2:331.17-1
- Updated to 331.17.

* Fri Oct 04 2013 Simone Caronni <negativo17@gmail.com> - 2:331.13-1
- Update to 331.13.

* Mon Sep 09 2013 Simone Caronni <negativo17@gmail.com> - 2:325.15-1
- Update to 325.15.

* Wed Aug 21 2013 Simone Caronni <negativo17@gmail.com> - 2:319.49-1
- Updated to 319.49.

* Wed Jul 03 2013 Simone Caronni <negativo17@gmail.com> - 2:319.32-2
- Add armv7hl support.

* Fri Jun 28 2013 Simone Caronni <negativo17@gmail.com> - 1:319.32-1
- Update to 319.32.

* Fri May 24 2013 Simone Caronni <negativo17@gmail.com> - 1:319.23.1
- Update to 319.23.

* Thu May 02 2013 Simone Caronni <negativo17@gmail.com> - 1:319.17-1
- Update to 319.17.
- Switch to ftp://download.nvidia.com/ sources.

* Wed Apr 10 2013 Simone Caronni <negativo17@gmail.com> - 1:319.12-1
- Started off from rpmfusion-nonfree packages.
- Updated to 319.12.
- Simplify spec file; move version to official version.
