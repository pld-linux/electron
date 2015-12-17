# TODO:
# - build from source (the process and deps look like hell)
#   https://github.com/atom/electron/blob/v0.36.0/docs/development/build-instructions-linux.md

Summary:	Framework cross-platform desktop applications using JavaScript, HTML and CSS
Name:		electron
Version:	0.36.0
Release:	0.1
License:	MIT, BSD
Group:		Applications
#Source0:	https://github.com/atom/electron/archive/v%{version}/%{name}-%{version}.tar.gz
## Source0-md5:	0c20e4676d7aef091521c9264d58939a
Source1:	https://github.com/atom/electron/releases/download/v%{version}/%{name}-v%{version}-linux-ia32.zip
# Source1-md5:	1272f2a7330341f86cd8be1cce14afc9
Source2:	https://github.com/atom/electron/releases/download/v%{version}/%{name}-v%{version}-linux-x64.zip
# Source2-md5:	1c77028a12330b4883fe93eea82c0b63
URL:		https://github.com/atom/electron
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/%{name}
%define		_noautoreq		libnode.so libnotify.so

%description
The Electron framework lets you write cross-platform desktop
applications using JavaScript, HTML and CSS. It is based on Node.js
and Chromium and is used in the Atom editor.

%prep
%setup -qcT
%ifarch %{ix86}
%{__unzip} %{SOURCE1}
%endif
%ifarch %{x8664}
%{__unzip} %{SOURCE2}
%endif

%install
rm -rf $RPM_BUILD_ROOT

# make install repeatable
rm -f debug*.list

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}
cp -a . $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s %{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/LICENSE*
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/libgcrypt*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/locales
%{_libdir}/%{name}/resources
%attr(755,root,root) %{_libdir}/%{name}/electron
%attr(755,root,root) %{_libdir}/%{name}/libnode.so
%attr(755,root,root) %{_libdir}/%{name}/libnotify.so.4
%{_libdir}/%{name}/content_shell.pak
%{_libdir}/%{name}/icudtl.dat
%{_libdir}/%{name}/natives_blob.bin
%{_libdir}/%{name}/snapshot_blob.bin
%{_libdir}/%{name}/version
