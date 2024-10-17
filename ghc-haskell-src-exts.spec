%global debug_package %{nil}
%define module haskell-src-exts

Summary:	Manipulating Haskell source: abstract syntax, lexer, parser, and pretty-printer
Name:		ghc-%{module}
Version:	1.14.0.1
Release:	2
License:	BSD
Group:		Development/Other
Url:		https://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(cpphs)
BuildRequires:	haskell(happy)
Requires(post,preun):	ghc
Requires(pre):	haskell(cpphs)
Requires(pre):	haskell(happy)
Obsoletes:	%{module} < 1.14.0.1

%description
Haskell-Source with Extensions (HSE, haskell-src-exts) is an extension of the
standard haskell-src package, and handles most registered syntactic extensions
to Haskell, including:
* Multi-parameter type classes with functional dependencies
* Indexed type families (including associated types)
* Empty data declarations
* GADTs
* Implicit parameters
* Template Haskell
and a few more. All extensions implemented in GHC are supported.
Apart from these standard extensions, it also handles regular patterns as per
the HaRP extension as well as HSX-style embedded XML syntax.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

