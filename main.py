import argparse
from scripts.etl_process import etl_process

def main():
     # Parse command-line ticker argument
    parser = argparse.ArgumentParser(description='Run ETL process with parameter')
    parser.add_argument('param', type=str, help='Parameter to pass to ETL process')
    args = parser.parse_args()

    # Call etl_process with the parameter
    etl_process(args.param)

if __name__ == "__main__":
    main()
