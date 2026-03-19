import asyncio
import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


async def run_agent(user_request: str):
    """
    Agent that:
    1. Connects to your MCP server
    2. Gets available tools
    3. Uses Gemini to decide what to do
    4. Calls tools automatically
    5. Loops until task is done
    """

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # STEP 1 — get tools from your MCP server
            tools_response = await session.list_tools()
            tools = tools_response.tools

            # STEP 2 — format tools for Gemini
            tool_descriptions = "\n".join(
                f"- {t.name}: {t.description}" for t in tools
            )

            system_prompt = f"""
You are an academic poster generation assistant.

You have access to these tools via MCP server:

{tool_descriptions}

Rules:
- To call a tool, respond with EXACTLY this format:
CALL_TOOL: tool_name
ARGUMENTS: {{"arg1": "value1", "arg2": "value2"}}

- When the task is complete, respond with:
DONE: your final message to the user

- Think step by step.
- Use tools in the right order.
- Always compile after generating or editing.
- Do not add extra text before CALL_TOOL or DONE.
""".strip()

            print(f"\nAgent starting task: {user_request}\n")
            print("=" * 50)

            messages = [{"role": "user", "content": user_request}]
            current_message = user_request

            for step in range(10):
                print(f"\nStep {step + 1}:")

                # Build conversation text
                conversation = "\n".join(
                    f"{msg['role']}: {msg['content']}" for msg in messages
                )

                # New SDK call pattern
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=conversation,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        temperature=0.2,
                    ),
                )

                agent_response = (response.text or "").strip()
                print(f"Agent thinks: {agent_response}")

                messages.append({
                    "role": "assistant",
                    "content": agent_response
                })

                # STEP 5 — check if done
                if agent_response.startswith("DONE:"):
                    final_message = agent_response.replace("DONE:", "", 1).strip()
                    print("\n=== TASK COMPLETE ===")
                    print(final_message)
                    return final_message

                # STEP 6 — parse and call tool
                if "CALL_TOOL:" in agent_response:
                    lines = agent_response.splitlines()
                    tool_name = ""
                    arguments = {}

                    for line in lines:
                        if line.startswith("CALL_TOOL:"):
                            tool_name = line.replace("CALL_TOOL:", "", 1).strip()

                        elif line.startswith("ARGUMENTS:"):
                            args_str = line.replace("ARGUMENTS:", "", 1).strip()
                            try:
                                arguments = json.loads(args_str)
                            except json.JSONDecodeError:
                                print("Could not parse ARGUMENTS as JSON.")
                                arguments = {}

                    if tool_name:
                        print(f"Calling tool: {tool_name}")
                        print(f"Arguments: {arguments}")

                        result = await session.call_tool(
                            tool_name,
                            arguments=arguments
                        )

                        # Safely collect MCP tool output
                        tool_result_parts = []
                        for item in result.content:
                            if hasattr(item, "text"):
                                tool_result_parts.append(item.text)
                            else:
                                tool_result_parts.append(str(item))

                        tool_result = "\n".join(tool_result_parts)
                        print(f"Tool result: {tool_result}")

                        current_message = f"Tool {tool_name} returned: {tool_result}"
                        messages.append({
                            "role": "user",
                            "content": current_message
                        })
                    else:
                        print("No tool name found. Stopping.")
                        break
                else:
                    print("Agent did not call a tool. Stopping.")
                    break

            print("\nReached max steps without completion.")
            return None


if __name__ == "__main__":
    request = input("What poster do you need? ")
    asyncio.run(run_agent(request))