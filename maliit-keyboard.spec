%define date 20200820

Name:          maliit-keyboard
Version:       0.0.0
Release:       %{?date:0.%{date}.}1
Summary:       Virtual keyboard for the maliit input framework

Group:         System/Libraries
License:       BSD
URL:           http://maliit.github.io/
Source0:       https://github.com/maliit/keyboard/archive/master.tar.gz

BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(maliit-framework)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Feedback)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(libpinyin)
BuildRequires: pkgconfig(anthy)
BuildRequires: pkgconfig(chewing)
BuildRequires: %{_lib}presage-devel
BuildRequires: doxygen
BuildRequires: presage-text2ngram

Requires:	maliit

%description
Maliit provides a flexible and cross-platform input method plugins. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%prep
%autosetup -p1 -n keyboard-master
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc %{_docdir}/maliit-keyboard
%{_bindir}/maliit-keyboard*
%{_libdir}/maliit/plugins/libmaliit-keyboard-plugin.so
%{_datadir}/maliit/plugins
%{_datadir}/glib-2.0/schemas/org.maliit.keyboard.maliit.gschema.xml
