let
  pkgs = import (fetchTarball("channel:nixpkgs-unstable")) {};
in
  pkgs.mkShell {
    buildInputs = with pkgs; [
      python312
      python312Packages.flask
      python312Packages.requests
    ];
  }
