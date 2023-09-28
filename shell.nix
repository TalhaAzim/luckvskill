{ pkgs ? import <nixpkgs> {} }:

let
  libraries = [ pkgs.stdenv.cc.cc.lib ];
in
  pkgs.mkShell {
    buildInputs = [
      pkgs.python311
      pkgs.pipenv
      #pkgs.stdenv.cc.cc.lib
    ];
  
    LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath libraries}";

    shellHook = ''
      echo "Env var: $LD_LIBRARY_PATH"
      echo "Library Path: ${pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib ]}"
    '';

}

