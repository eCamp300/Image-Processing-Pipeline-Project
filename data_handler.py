"""
Network module.
Isolates external API/web requests from the local image processing logic.
"""

import requests

def get_image_from_url(url):
    """
        Fetches an image from a provided web URL.

        Args:
            url (str): The direct URL to the image asset.

        Returns:
            bytes: The raw binary content of the fetched image.

        Raises:
            requests.exceptions.HTTPError: If the network request fails (e.g., 404).
        """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.content