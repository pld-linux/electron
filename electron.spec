# TODO:
# - build from source (the process and deps look like hell)
#   https://github.com/electron/electron/blob/v1.4.3/docs/development/build-instructions-linux.md
# NOTES:
# - At least 25GB disk space and 8GB RAM.
#

Summary:	Framework cross-platform desktop applications using JavaScript, HTML and CSS
Name:		electron
Version:	1.4.3
Release:	0.1
License:	MIT, BSD
Group:		Applications
URL:		https://github.com/atom/electron
BuildRequires:	GConf2-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	bison
BuildRequires:	clang
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	git-core
BuildRequires:	gperf
BuildRequires:	gtk+2-devel
BuildRequires:	libcap-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	ncurses
BuildRequires:	npm
BuildRequires:	nss-devel
BuildRequires:	python >= 1:2.7
BuildRequires:	xorg-app-iceauth
BuildRequires:	xorg-app-rgb
BuildRequires:	xorg-app-sessreg
BuildRequires:	xorg-app-xgamma
BuildRequires:	xorg-app-xhost
BuildRequires:	xorg-app-xinput
BuildRequires:	xorg-app-xkill
BuildRequires:	xorg-app-xmodmap
BuildRequires:	xorg-app-xrandr
BuildRequires:	xorg-app-xrandr
BuildRequires:	xorg-app-xrefresh
BuildRequires:	xorg-app-xset
BuildRequires:	xorg-app-xsetpointer
BuildRequires:	xorg-app-xsetroot
BuildRequires:	xorg-app-xstdcmap
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
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
git clone https://github.com/atom/electron.git -b v%{version} --depth 1 .

./script/bootstrap.py -v

install -d lib
ln -s %{_libdir}/libncurses.so.5 lib/libtinfo.so.5

%build
export LD_LIBRARY_PATH=`pwd`/lib

./script/build.py -c R

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
