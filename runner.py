if __name__ == '__main__':
    from sys import exit
    from mk60.app import main
    exit(main())
else:
    raise RuntimeError("runner must be run, not imported")
