"""
Version 1.0 : Proof of Concept.
Reads the input database, triggers the network fetch, and executes the transformation.
"""

import pandas as pd
import config
from data_handler import get_image_from_url
from image_processor import generate_mockup


def run_image_program():
    """
    Iterates through the target CSV processes each URL, and handles execution errors.
    """
    df = pd.read_csv(config.CSV_PATH)

    # process the 3 images for test run
    # iterate through the images
    for idx, row in df.head(3).iterrows():
        url = row['image_url']
        output_filename = f'final_card_{idx + 1}.png'

        try:
            # Isolate the network layer
            image_binary = get_image_from_url(url)

            # Execute the Wand/ImageMagick layer
            generate_mockup(image_binary, output_filename)
            print(f"Successfully generated: {output_filename}.")

        except Exception as e:
            # Log failed attempts without crashing the entire batch loop
            print(f"Failed on row {idx + 1}: {e}")


if __name__ == '__main__':
    run_image_program()

