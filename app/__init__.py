from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="AI Productivity Assistant", version="1.0.0")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    tasks: list[str] = Field(default_factory=list)


class ChatResponse(BaseModel):
    reply: str
    suggestions: list[str] = Field(default_factory=list)


def generate_reply(message: str, tasks: list[str]) -> ChatResponse:
    text = message.strip()
    if not text:
        return ChatResponse(reply="I’m ready to help. Tell me what you want to do today.", suggestions=["Plan my day", "Summarize my notes", "Draft an email"])

    lower = text.lower()
    suggestions: list[str] = []

    if "plan" in lower or "schedule" in lower or "today" in lower:
        task_block = ", ".join(tasks) if tasks else "your top priorities"
        reply = (
            "Here’s a focused plan for today: "
            f"1) Start with the highest-impact task, 2) Block 25 minutes for deep work, 3) Review {task_block}, "
            "4) Keep a 10-minute buffer for unexpected work."
        )
        suggestions = ["Break this into steps", "Add a deadline", "Suggest a better order"]
    elif "email" in lower or "message" in lower:
        reply = (
            "Draft a concise, professional message: "
            "'Hi team, I’ve reviewed the current priorities and will focus on the most urgent items first. "
            "I’ll share updates by end of day and flag any blockers early.'"
        )
        suggestions = ["Make it more friendly", "Shorten it", "Draft a follow-up version"]
    elif "summary" in lower or "note" in lower or "research" in lower:
        reply = (
            "Summary approach: identify the main goal, list key findings, highlight risks, and create a next-step checklist. "
            "If you share your notes, I can turn them into a polished summary."
        )
        suggestions = ["Turn this into bullets", "Create a meeting summary", "Draft an action list"]
    elif "brainstorm" in lower or "idea" in lower:
        reply = (
            "Brainstorming prompt: start with the user need, then list 3 potential solutions, compare trade-offs, and choose the simplest option that delivers the most value."
        )
        suggestions = ["Generate 5 ideas", "Weigh pros and cons", "Turn into a roadmap"]
    elif "task" in lower or "todo" in lower or "reminder" in lower:
        reply = (
            "I’d organize your work into: urgent, important, and routine. "
            "Then I’d schedule the urgent tasks first, protect time for important work, and batch small admin tasks together."
        )
        suggestions = ["Create a 7-day plan", "Set priority levels", "List blockers"]
    else:
        reply = (
            f"I can help with: '{text}'. "
            "For productivity, the best next step is to break this into a clear objective, 2-3 action steps, and a timeline."
        )
        suggestions = ["Turn this into a task list", "Explain the steps", "Write a quick plan"]

    if tasks:
        reply += "\n\nCurrent priorities: " + "; ".join(tasks)

    return ChatResponse(reply=reply, suggestions=suggestions)


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "ai-productivity-assistant"}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Optional OpenAI integration. If no API key is set, we fall back to a smart local assistant.
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=api_key)
            prompt = (
                "You are a productivity assistant. Produce a concise, actionable response. "
                f"User request: {request.message}. "
                f"Current tasks: {', '.join(request.tasks) if request.tasks else 'None'}."
            )
            completion = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                messages=[
                    {"role": "system", "content": "You are a highly practical productivity coach."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=300,
            )
            answer = completion.choices[0].message.content.strip()
            return ChatResponse(reply=answer, suggestions=["Break this into tasks", "Create a timeline", "Draft a summary"])
        except Exception:
            pass

    return generate_reply(request.message, request.tasks)


@app.get("/")
async def root():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(BASE_DIR / "static" / "favicon.svg")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
