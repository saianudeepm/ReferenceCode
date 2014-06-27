__author__ = 'sai anudeep machavarapu'
#!/usr/bin/python
import sys
import json


def parse_json_data(inputfile, outputfile):
    data_json = []
    with open(inputfile) as file:
        for line in file:
            data_json.append(json.loads(line))

    headers = []
    for head in data_json:
        headers = head.keys()
        break
    _print_as_tsv(headers, data_json, outputfile)


def _print_as_tsv(headers, data_json, outputfile):
    result_file = open(outputfile, 'wb')
    #output the header
    result_file.write('\t'.join(headers).encode('utf-8'))

    for line in data_json:
        data = map(unicode, line.values())
        result_file.write("\t".join(data).replace('\n',' ').encode('utf-8'))
        result_file.write("\n".encode('utf-8'))
    result_file.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception
    parse_json_data(sys.argv[1], sys.argv[2])
