from fastapi import FastAPI

from app import routers

app = FastAPI(
    title="🦖 Dynamo App",
    description="⚡️Fast API + 🦖 DynamoDB",
    version="1.0.0",
    contact={
        "name": "Anthony Caliani",
        "url": "https://github.com/avcaliani",
        "email": "anthony@github.com",
    },
    license_info={"name": "MIT License", "url": "https://opensource.org/licenses/MIT"},
)

# 👇 Routers
app.include_router(routers.user)


@app.get("/")
async def root() -> dict:
    return {
        "title": f"{app.title} - v{app.version}",
        "description": app.description,
        "contact": app.contact,
        "license": app.license_info
    }
