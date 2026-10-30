"""
CivicPulse AI — Application Launcher
--------------------------------------
Local dev  : python run.py
Render     : uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT
"""
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0" if os.environ.get("RENDER") else "127.0.0.1"

    print("=" * 65)
    print("   CIVIC PULSE AI — Digital Governance & Public Information")
    print("   Full-Stack GenAI: BLIP Vision + Mistral-7B (Hugging Face)")
    print("=" * 65)
    print(f" * URL:           http://{host}:{port}")
    print(f" * Swagger Docs:  http://{host}:{port}/docs")
    print(f" * Environment:   {'Render Cloud' if os.environ.get('RENDER') else 'Local Dev'}")
    print("=" * 65)

    uvicorn.run(
        "backend.app.main:app",
        host=host,
        port=port,
        reload=not os.environ.get("RENDER"),   # no --reload on Render
    )
