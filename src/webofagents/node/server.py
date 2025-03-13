from fastapi import FastAPI
from webofagents.node.routes import router
from webofagents.node.events import startup_event, shutdown_event

app = FastAPI(title="Web of AI Agents")

# Register startup and shutdown event handlers
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

# Include modular routes
app.include_router(router)

# Run server if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("webofagents.node.server:app", host="0.0.0.0", port=8000, reload=True)
