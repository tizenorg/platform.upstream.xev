Summary: print contents of X events
Name: xev
Version: 1.2.1
Release: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(dmx) pkgconfig(xext) pkgconfig(xft) pkgconfig(xrandr)
BuildRequires: pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xmu)
BuildRequires: pkgconfig(xpm) pkgconfig(xt) pkgconfig(xtst) pkgconfig(xv)
BuildRequires: pkgconfig(xxf86dga) pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-atom)

%description
Xev creates a window and then asks the X server to  send  it  events  whenever
anything happens to the window (such as it being moved, resized, typed in,
clicked in, etc.).  You can also attach it to an existing window.  It is  use‐ful
for seeing what causes events to occur and to display the information that
they contain; it is essentially a debugging and development tool,  and  should
not be needed in normal usage.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
{
      make install DESTDIR=$RPM_BUILD_ROOT
}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc
%{_bindir}/*
#%{_bindir}/xev
#%{_mandir}/man1/xev.1*
