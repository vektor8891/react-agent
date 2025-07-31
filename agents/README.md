# Agents Directory

This directory contains the various LangGraph-based agents for the React Agent project.

## Structure

```text
agents/
├── __init__.py                    # Package initialization
├── currency_exchange_agent.py     # Currency exchange rate agent
├── base/                         # Base classes and utilities
│   ├── __init__.py
│   └── agent_base.py            # Base agent class
└── utils/                       # Agent utilities
    ├── __init__.py
    └── tools.py                 # Common tools and functions
```

## Creating New Agents

When creating a new agent:

1. **Create the agent file** in this directory: `agents/your_agent_name.py`
2. **Follow the naming convention**: Use snake_case for filenames
3. **Import in **init**.py**: Add your agent to the package exports
4. **Use the base class**: Extend from `AgentBase` if available
5. **Document your agent**: Include docstrings and usage examples

## Example Agent Structure

```python
#!/usr/bin/env python3
"""
Your Agent Name

Description of what your agent does.
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

import vertexai
from langchain_google_vertexai import ChatVertexAI
from langgraph.graph import StateGraph, END
from langchain_core.tools import tool

class YourAgent:
    """Your agent implementation."""
    
    def __init__(self):
        """Initialize the agent."""
        load_dotenv()
        self._init_vertex_ai()
        # ... rest of initialization
    
    def _init_vertex_ai(self):
        """Initialize Vertex AI."""
        # Standard Vertex AI initialization
        pass
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Process a user query."""
        # Your agent logic here
        pass

def main():
    """Example usage of the agent."""
    agent = YourAgent()
    result = agent.process_query("Your test query")
    print(result)

if __name__ == "__main__":
    main()
```

## Usage

```python
from agents import CurrencyExchangeAgent

# Initialize and use the agent
agent = CurrencyExchangeAgent()
result = agent.get_exchange_rate("USD to EUR today")
```
