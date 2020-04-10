from sys import argv
import beholder.argparser as argparser
import beholder.cfg_reader as cfg_reader
import beholder.opts_validator as opts_validator
import beholder.analyzer.state_checker as state_checker
import beholder.file_comparator.comparison_types as comparison_types


def main():
    opts = argparser.parse(argv[1:])
    opts_validator.validate_opts(opts)
    sites = cfg_reader.parse_file(opts.config_path)
    cfg_reader.validate_websites(sites)
    if opts.show_diffs:
        checker = state_checker.StateChecker(comparison_types.WithDiffsComparison())
    else:
        checker = state_checker.StateChecker(comparison_types.SimpleComparison())
    checker.run(opts, sites)


if __name__ == '__main__':
    main()
