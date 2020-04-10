from sys import argv
import beholder.argparser as parser
import beholder.cfg_reader as reader
import beholder.opts_validator as validator
import beholder.analyzer.state_checker as checker
import beholder.file_comparator.comparison_types as types


def main():
    args = parser.parse(argv[1:])
    validator.validate_opts(args)
    sites = reader.parse_file(args.config_path)
    reader.validate_websites(sites)
    if args.show_diffs:
        new_checker = checker.StateChecker(types.WithDiffsComparison())
    else:
        new_checker = checker.StateChecker(types.SimpleComparison())
    new_checker.run(str(args.output_path), args.time, sites)


if __name__ == '__main__':
    main()
