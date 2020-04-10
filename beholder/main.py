from sys import argv
import beholder.argparser as argparser
import beholder.cfg_reader as cfg_reader
import beholder.opts_validator as opts_validator
import beholder.analyzer.state_checker as state_checker


def main():
    opts = argparser.parse(argv[1:])
    opts_validator.validate_opts(opts)
    sites = cfg_reader.parse_file(opts.config_path)
    cfg_reader.validate_websites(sites)
    checker = state_checker.StateChecker(sites, opts)
    checker.run()


if __name__ == '__main__':
    main()
