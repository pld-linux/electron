# TODO:
# - build from source (the process and deps look like hell)
#   WIP on 'source' branch

Summary:	Framework cross-platform desktop applications using JavaScript, HTML and CSS
Name:		electron
Version:	1.4.3
Release:	1
License:	MIT, BSD
Group:		Applications
Source1:	https://github.com/atom/electron/releases/download/v%{version}/%{name}-v%{version}-linux-ia32.zip
Source2:	https://github.com/atom/electron/releases/download/v%{version}/%{name}-v%{version}-linux-x64.zip
URL:		https://github.com/atom/electron
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# do not provide SONAME deps from this package
%define		_noautoprovfiles	%{_libdir}/%{name}
# provided by this package itself
%define		_noautoreq		libnode.so libffmpeg.so

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

# remove empty locales
find locales -size 0 | xargs -r rm -v

%install
rm -rf $RPM_BUILD_ROOT

# make install repeatable
rm -f debug*.list

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}
cp -a . $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s %{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/LICENSE*

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
%attr(755,root,root) %{_libdir}/%{name}/libffmpeg.so
%{_libdir}/%{name}/blink_image_resources_200_percent.pak
%{_libdir}/%{name}/content_resources_200_percent.pak
%{_libdir}/%{name}/content_shell.pak
%{_libdir}/%{name}/ui_resources_200_percent.pak
%{_libdir}/%{name}/views_resources_200_percent.pak
%{_libdir}/%{name}/icudtl.dat
%{_libdir}/%{name}/natives_blob.bin
%{_libdir}/%{name}/snapshot_blob.bin
%{_libdir}/%{name}/version
