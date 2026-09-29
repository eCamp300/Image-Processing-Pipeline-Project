"""
Configuration module for the Digital Card Rendering Pipeline.
Centralizes static file paths and coordinate mapping variables to prevent
hardcoding inside the processing engine.
"""

# File paths for local execution
CSV_PATH = 'card_images.csv'
CARD_TEMPLATE = 'blank_card_mockup.png'

# Mockup coordinate anchors for inner picture area
# Mapped as (X, Y) pixels: top left, top right, bottom left, bottom right
CORNER_TL = (475, 486)
CORNER_TR = (1268, 358)
CORNER_BR = (1430, 862)
CORNER_BL = (677, 1104)

