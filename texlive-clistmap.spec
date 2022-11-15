Name:		texlive-clistmap
Version:	61811
Release:	1
Summary:	Map and iterate over LaTeX3 clists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clistmap
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clistmap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clistmap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clistmap.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a key-based interface for defining
templates whose job is to partition LaTeX3 clists and map
differentiatedly across its components.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/clistmap
%{_texmfdistdir}/tex/latex/clistmap
%doc %{_texmfdistdir}/doc/latex/clistmap

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
