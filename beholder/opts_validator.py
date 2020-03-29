from argparse import Namespace
import beholder.const as const


def validate_opts(opts: Namespace) -> None:
    if opts.time < const.T_MIN:
        raise ValueError(f"Checking interval must be at least {const.T_MIN} sec.")
    out_path = opts.output_path
    if out_path and out_path.is_file():
        raise FileExistsError(f"File {out_path.resolve()} exists. It would be overwritten.")
    cfg_path = opts.config_path.resolve()
    if not cfg_path.is_file():
        raise FileNotFoundError(f"{cfg_path} does not exist or is not a file.")
