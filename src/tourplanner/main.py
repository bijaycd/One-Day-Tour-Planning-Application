from fastapi import FastAPI
from src.tourplanner.routers import user_interaction, itinerary_generation, optimization, memory, weather, map

app = FastAPI()

# Include routers
app.include_router(user_interaction.router, prefix="/user", tags=["User Interaction"])
app.include_router(itinerary_generation.router, prefix="/itinerary", tags=["Itinerary Generation"])
app.include_router(optimization.router, prefix="/optimize", tags=["Optimization"])
app.include_router(memory.router, prefix="/memory", tags=["Memory"])
app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(map.router, prefix="/map", tags=["Map"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Tour Planning Assistant API!"}