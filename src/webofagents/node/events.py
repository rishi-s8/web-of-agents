from fastapi import FastAPI

async def startup_event():
    print("Starting Web of Agents server...")

async def shutdown_event():
    print("Shutting down Web of Agents server...")
