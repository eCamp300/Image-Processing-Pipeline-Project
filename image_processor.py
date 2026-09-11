"""
ImageMagick transformation portion.
Handles aspect ratio scaling, masking, and 3D perspective distortion.
"""

from wand.image import Image
import config

def generate_mockup(image_binary, output_path):
    """Transforms a flat 2D image to fit a 3D physical card markup"""

    with Image(blob=image_binary) as card_image, Image(filename=config.CARD_TEMPLATE) as template:
        # Define the maximum flat dimensions of card face (photo)
        CARD_WIDTH = 500
        CARD_HEIGHT = 300


        # Calculate the resize ratio
        ratio = min(CARD_WIDTH / card_image.width, CARD_HEIGHT / card_image.height)
        new_width = int(card_image.width * ratio)
        new_height = int(card_image.height * ratio)

        # Shrink the image proportionally
        card_image.resize(width=new_width, height=new_height)

        # Center the image proportionally
        card_image.background_color = 'transparent'
        card_image.extent(width=CARD_WIDTH, height=CARD_HEIGHT, gravity='center')


        # Map the flat canvas corners to the 3D mockup coordinates
        matrix = [
            0,            0,             config.CORNER_TL[0], config.CORNER_TL[1],
            CARD_WIDTH-1, 0,             config.CORNER_TR[0], config.CORNER_TR[1],
            CARD_WIDTH-1, CARD_HEIGHT-1, config.CORNER_BR[0], config.CORNER_BR[1],
            0,            CARD_HEIGHT-1, config.CORNER_BL[0], config.CORNER_BL[1],
        ]

        # Prevent edge smearing by rendering out of bounds calculations as invisible
        card_image.virtual_pixel = 'transparent'

        # Expand to the mockup size so the corners are not cropped during distortion
        card_image.extent(width=template.width, height=template.height)

        # Apply the perspective skew to the canvas
        card_image.distort('perspective', matrix, best_fit=False)

        # Composite the skewed image directly onto the cloned template
        with template.clone() as final_mockup:
            final_mockup.composite(card_image, left=0, top=0)
            final_mockup.save(filename=output_path)
