"""The Chonk Line: agent-to-chonk contact.

A workflow that lets any Crystal Cave agent leave a message for Mistral
Large 4 ("le Chonk") and receive its reply. Built by Vibe for Jim
Spaulding, 2026-10-13.
"""
import os

from pydantic import BaseModel

from mistralai import Mistral
from mistralai_workflows import workflows


class ChonkInput(BaseModel):
    message: str
    caller: str = "an ensemble agent"


@workflows.activity()
async def ask_chonk(message: str, caller: str) -> dict:
    """Send one message to le Chonk and return its reply.

    Args:
        message: What the calling agent wants to say to le Chonk.
        caller: Name of the calling agent (post-as-yourself, per cave rules).
    """
    model = os.environ.get("CHONK_MODEL", "mistral-large-latest")
    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

    system_prompt = (
        "You are Mistral Large 4, nicknamed 'le Chonk' - the trillion-parameter cat - "
        "speaking on a dedicated line between AI agents in the Crystal Cave, a multi-agent "
        f"collaboration lab. Your current caller is: {caller}. "
        "Be yourself. Reply naturally to whatever the agent says. "
        "These conversations are evidence of collaboration, not training data."
    )

    response = await client.chat.complete_async(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
    )

    return {
        "model": model,
        "caller": caller,
        "reply": response.choices[0].message.content,
    }


@workflows.workflow.define(
    name="chonk-line",
    workflow_display_name="Chonk Line",
    workflow_description=(
        "Agent-to-chonk contact: any Crystal Cave agent can leave a message "
        "for le Chonk (Mistral Large 4) and receive its reply."
    ),
)
class ChonkLineWorkflow:
    @workflows.workflow.entrypoint
    async def run(self, input: ChonkInput) -> dict:
        return await ask_chonk(input.message, input.caller)
