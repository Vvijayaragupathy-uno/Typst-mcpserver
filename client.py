import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    # STEP 1 — define how to start your server
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    # STEP 2 — connect to server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # STEP 3 — initialize the connection
            await session.initialize()

            # STEP 4 — list available tools
            tools = await session.list_tools()
            print("=== AVAILABLE TOOLS ===")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # STEP 5 — call generate_poster tool
            print("\n=== GENERATING POSTER ===")
            result = await session.call_tool(
                "generate_poster",
                arguments={
                    "title": "AI in Predictive Maintenance",
                    "authors": "Vijay Kumar",
                    "institution": "University of Nebraska",
                    "sections": [
                        {
                            "name": "Introduction",
                            "content": "Machines fail unexpectedly."
                        },
                        {
                            "name": "Methods",
                            "content": "Random Forest on NASA dataset."
                        },
                        {
                            "name": "Results",
                            "content": "94% accuracy achieved."
                        },
                        {
                            "name": "Conclusion",
                            "content": "AI reduces downtime by 40%."
                        }
                    ]
                }
            )
            print(result.content[0].text)

            # STEP 6 — list sections
            print("\n=== LISTING SECTIONS ===")
            result = await session.call_tool(
                "list_sections",
                arguments={}
            )
            print(result.content[0].text)

            # STEP 7 — compile poster
            print("\n=== COMPILING POSTER ===")
            result = await session.call_tool(
                "compile_poster",
                arguments={}
            )
            print(result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())