from fastapi import FastAPI, HTTPException, Response
from data_handler import get_image_from_url
from image_processor import generate_mockup

#Initialized the FastAPI environment to replace the local batch script.
app = FastAPI()

@app.get("/api/render")
def render_card(image_url: str):
    try:
        image_binary = get_image_from_url(image_url)
        rendered_buffer = generate_mockup(image_binary)

        #Returns the PNG directly to the web browser
        return Response(content=rendered_buffer, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))