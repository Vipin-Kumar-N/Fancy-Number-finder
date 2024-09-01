import re
from xml.etree import ElementTree as ET

# Function to extract numbers from CDATA content
def extract_main_numbers(cdata):
    # Extract all 4-digit numbers from the CDATA section
    return re.findall(r'color:#fff!important; font-size: 16px; text-align: center;">([^<]+)</label></td>', cdata)

# Function to extract regnNo values from HTML content
def extract_regn_no(html_content):
    # Find all regnNo values using a regex
    return re.findall(r'<span id="tblAppliedNumber:\d+:regnNo">([^<]+)</span>', html_content)

# Function to process the XML file based on the mode
def process_xml(file_path, mode):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # List to hold extracted data
    extracted_data = []

    # Determine extraction method based on mode
    extract_function = extract_main_numbers if mode == "result" else extract_regn_no

    # Iterate through all <update> elements
    for update in root.findall('.//update'):
        cdata_content = update.text
        if cdata_content:
            extracted_data.extend(extract_function(cdata_content))

    # Determine output file name based on mode
    output_file = 'output/numbers.txt' if mode == "result" else 'output/regnumbers.txt'

    # Write extracted data to the output file
    with open(output_file, 'w') as file:
        file.write('\n'.join(extracted_data))

    print(f"Extracted {len(extracted_data)} items and saved to '{output_file}'")

def xmlparser():
    # Paths to your XML files
    bidding_xml_file_path = 'xml/bidding.xml'
    result_xml_file_path = 'xml/result.xml'

    # Process the XML files
    process_xml(bidding_xml_file_path, "bidding")
    process_xml(result_xml_file_path, "result")