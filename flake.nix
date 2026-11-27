{
  description = "Starflake ontology development shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { nixpkgs, ... }:
    {
      devShells =
        nixpkgs.lib.genAttrs
          [
            "x86_64-linux"
            "aarch64-linux"
          ]
          (
            system:
            let
              pkgs = nixpkgs.legacyPackages.${system};
            in
            {
              default = pkgs.mkShell {
                packages = [
                  pkgs.uv
                  pkgs.python314
                  pkgs.just
                  (pkgs.writeShellScriptBin "gen-erdiagram" ''
                    exec ${pkgs.uv}/bin/uv run --locked -m linkml.generators.erdiagramgen "$@"
                  '')
                ];
                # PyOxigraph's PyPI wheel needs the C++ runtime at import time.
                shellHook = ''
                  export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib ]}''${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
                '';
                # uv's downloaded interpreters cannot run on NixOS: use the one above.
                UV_PYTHON_DOWNLOADS = "never";
              };
            }
          );
    };
}
