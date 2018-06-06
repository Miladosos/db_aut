import csv
import json


class YagoExtractor:

    def __init__(self):

        # Loading Config file
        with open('config.json') as configFile:
            config = json.load(configFile)
            self.yago_files = config['yagoFiles']
            self.extract_dir = config['extracted_dir']

    def label(self, name=None, label_tag=None):
        """
        Searching Yago Labels to find matching lines with name or label_tag based on function input


        :param name: search Labels for it's tag
        :param label_tag: Search Yago labels for matching tags

        :return: name's label tag or None if not found or 0 for wrong input
        """

        if (name is None) and (label_tag is None):
            return 0

        # Loading Yago labels
        with open(self.yago_files['Labels'], encoding='utf-8') as LabelFile:
            yago_labels = csv.reader(LabelFile, delimiter="\t")

            if name:
                for label in yago_labels:
                    if name in label[3]:  # Match found !
                        label_tag = label[1]
                        break

            if label_tag:
                for label in yago_labels:  # Search Tago_labels from beginning to write matched lines into label's file
                    if label_tag == label[1]:
                        with open(file="{}[label]{}.tsv".format(self.extract_dir, label_tag), mode='a') as label_file:
                            label_file.write(str(label) + '\n')

        return label_tag

    def type(self, tag1, tag2=None):
        """
        Searching Yago type to find matched types and tags

        :param tag1: a type tag to search
        :param tag2: Optional tag
        :return: Nothing
        """

        # Loading Yago types
        with open(self.yago_files['Types'], encoding='utf-8') as LabelFile:
            yago_types = csv.reader(LabelFile, delimiter="\t")

            for line in yago_types:  # Searching Yago types
                if tag2:
                    if (tag1 in line) and (tag2 in line):
                        with open(file="{}[type]{}_{}.tsv".format(self.extract_dir, tag1[1:-1], tag2[1:-1]),
                                  mode='a') as type_file:  # Writing matched tag and type to file
                            type_file.write(str(line) + '\n')
                else:
                    if tag1 in line:
                        with open(file="{}[type]{}.tsv".format(self.extract_dir, tag1),
                                  mode='a') as type_file:  # Writing matched tag and type to file
                            type_file.write(str(line) + '\n')

    def fact(self, tag1, tag2=None):
        """
        Searching yago facts to find matched facts and tag

        :param tag1: a tag to search in facts
        :param tag2: Optional tag
        :return: Nothing
        """

        # Loading Yago facts
        with open(self.yago_files['Facts'], encoding='utf-8') as LabelFile:
            yago_facts = csv.reader(LabelFile, delimiter="\t")

            for line in yago_facts:  # Searching Yago facts
                if tag2:
                    if (tag1 in line) and (tag2 in line):
                        with open(file="{}[fact]{}_{}.tsv".format(self.extract_dir, tag1[1:-1], tag2[1:-1]),
                                  mode='a') as fact_file:  # Writing matched tag and fact to file
                            fact_file.write(str(line) + '\n')
                else:
                    if tag1 in line:
                        with open(file="{}[fact]{}.tsv".format(self.extract_dir, tag1[1:-1]),
                                  mode='a') as fact_file:  # Writing matched tag and fact to file
                            fact_file.write(str(line) + '\n')
