# TODO:
# - build from source (the process and deps look like hell)
#   https://github.com/atom/electron/blob/v0.36.0/docs/development/build-instructions-linux.md
# NOTES:
# - space considerations: ~25GiB for build
#

Summary:	Framework cross-platform desktop applications using JavaScript, HTML and CSS
Name:		electron
Version:	0.36.0
Release:	0.1
License:	MIT, BSD
Group:		Applications
URL:		https://github.com/atom/electron
BuildRequires:	git-core
BuildRequires:	ncurses
BuildRequires:	npm
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
