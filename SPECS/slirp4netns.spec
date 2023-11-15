%global git0 https://github.com/rootless-containers/%{name}

Name: slirp4netns
Version: 1.2.1
Release: 1%{?dist}
Summary: slirp for network namespaces
License: GPLv2
URL: %{git0}
# build fails on i686 with: No matching package to install: 'go-md2man'
ExcludeArch: i686
Source0: %{git0}/archive/v%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: git
BuildRequires: /usr/bin/go-md2man
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: make
BuildRequires: libslirp-devel

%description
slirp for network namespaces, without copying buffers across the namespaces.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -Sgit

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man

%install
make DESTDIR=%{buildroot} install install-man

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Aug 22 2023 Jindrich Novy <jnovy@redhat.com> - 1.2.1-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.2.1
- Related: #2176055

* Thu Mar 09 2023 Jindrich Novy <jnovy@redhat.com> - 1.2.0-3
- BuildRequires: /usr/bin/go-md2man
- Related: #2176055

* Wed May 11 2022 Jindrich Novy <jnovy@redhat.com> - 1.2.0-2
- BuildRequires: /usr/bin/go-md2man
- Related: #2061390

* Tue May 03 2022 Jindrich Novy <jnovy@redhat.com> - 1.2.0-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.2.0
- Related: #2061390

* Tue Feb 15 2022 Jindrich Novy <jnovy@redhat.com> - 1.1.8-2
- fix gating - don't use insecure functions - thanks to Marc-André Lureau
- Related: #2001445

* Fri Dec 04 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.8-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.8
- Related: #1883490

* Thu Dec 03 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.7-2
- exclude i686 because of build failures
- Related: #1883490

* Thu Nov 26 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.7-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.7
- Related: #1883490

* Mon Nov 09 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.6-2
- - be sure to harden the linked binary
- Related: #1883490

* Thu Nov 05 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.6-1
- update to
  https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.6
- Related: #1883490

* Tue Aug 11 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.4-2
- use proper CFLAGS
- Related: #1821193

* Mon Jul 13 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.4-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.4
- Related: #1821193

* Thu Jul 09 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.3-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.3
- Related: #1821193

* Mon Jul 06 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.2-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.2
- Related: #1821193

* Fri Jun 05 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.1-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.1
- Related: #1821193

* Fri Jun 05 2020 Jindrich Novy <jnovy@redhat.com> - 1.1.0-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.1.0
- Related: #1821193

* Tue May 12 2020 Jindrich Novy <jnovy@redhat.com> - 1.0.1-1
- update to https://github.com/rootless-containers/slirp4netns/archive/v1.0.1.tar.gz
- Related: #1821193

* Thu Feb 06 2020 Jindrich Novy <jnovy@redhat.com> - 0.4.2-3.git21fdece
- Fix CVE-2020-8608
- Resolves: #1798979

* Thu Jan 16 2020 Jindrich Novy <jnovy@redhat.com> - 0.4.2-2.git21fdece
- Fix CVE-2020-7039.
Resolves: #1791576

* Mon Nov 25 2019 Jindrich Novy <jnovy@redhat.com> - 0.4.2-1.git21fdece
- update to latest 0.4.2, fixes bug 1763454
- Related: RHELPLAN-25139

* Thu Oct 31 2019 Jindrich Novy <jnovy@redhat.com> - 0.4.0-2
- add new BR: libseccomp-devel
- Related: #1766774

* Wed Oct 30 2019 Jindrich Novy <jnovy@redhat.com> - 0.4.0-1
- update to v.0.4.0
- sync with fedora spec
- drop applied CVE-2019-14378 patch
- Resolves: #1766774

* Thu Sep 26 2019 Jindrich Novy <jnovy@redhat.com> - 0.3.0-4
- Fix CVE-2019-14378 (#1755595).

* Fri Jun 07 2019 Lokesh Mandvekar <lsm5@redhat.com> - 0.3.0-3
- Resolves: #1683217 - BR: glib2-devel

* Fri Jun 07 2019 Lokesh Mandvekar <lsm5@redhat.com> - 0.3.0-2
- Resolves: #1683217 - bump slirp4netns to v0.3.0

* Thu Feb 28 2019 Lokesh Mandvekar <lsm5@redhat.com> - 0.3.0-1.alpha.2.git30883b5
- bump to v0.3.0-alpha.2

* Fri Nov 16 2018 Frantisek Kluknavsky <fkluknav@redhat.com> - 0.1-2.dev.gitc4e1bc5
- changed summary

* Fri Aug 10 2018 Lokesh Mandvekar <lsm5@redhat.com> - 0.1-1.dev.gitc4e1bc5
- First package for RHEL 8
- import from Fedora rawhide
- Exclude ix86 and ppc64
