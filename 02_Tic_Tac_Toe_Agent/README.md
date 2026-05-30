# Tic-Tac-Toe AI Agent Gameplay

An full-stack Tic-Tac-Toe web application that integrates classic game theory search algorithms with modern AI orchestrations. The game engine employs a **Deterministic Minimax Search Tree with Alpha-Beta Pruning** to guarantee perfect play, orchestrated via **LangGraph**, and contextualized with an in-memory **Retrieval-Augmented Generation (RAG)** pipeline for real-time strategy commentary.

---

## 🚀 Key Architectural Features

- **Unbeatable AI Core:** Implements a full-depth Minimax state-space search. Alpha-Beta pruning eliminates redundant game branches, making the computer mathematically impossible to defeat on Expert mode.
- **LangGraph State Orchestration:** Replaces traditional sequential loop logic with a clear state machine graph. The game loop seamlessly transitions from the AI's physical calculation node to a context retrieval node.
- **Localized RAG Pipeline:** Dynamically fetches precise game theory facts and tactical rule advisories from an internal knowledge base according to real-time grid positioning.
- **Premium Split UI Layout:** Designed with a sleek neon-dark responsive layout. Features a canvas layer overlay for uninterrupted, solid winning strike-through lines, adjustable search metrics, and first-turn initiative selections.

---
## ✅ Link for the website
The application has been deployed using render.com. The link for the application is https://codsoft-ai.onrender.com/ .It can be accessed through the given link.

## 🗺️ System Pipeline Architecture

The entire structure handles turn cycles by executing an acyclic workflow graph:

```text
[Human Click Input] 
         │
         ▼
 ┌───────────────┐
 │  HTTP POST    │ ──► Sends 1D array state matrix to /api/move
 └───────────────┘
         │
         ▼
 ┌────────────────────────────────────────────────────────┐
 │                LANGGRAPH ENGINE ROUTING                │
 │                                                        │
 │  ┌─────────────────┐       ┌────────────────────────┐  │
 │  │  ai_turn_node   │ ────► │  rag_commentary_node   │  │
 │  │ (Alpha-Beta MM) │       │ (Contextual Retrieval) │  │
 │  └─────────────────┘       └────────────────────────┘  │
 └────────────────────────────────────────────────────────┘
         │
         ▼
 ┌───────────────┐
 │ JSON Response │ ──► Contains updated matrix grid & strategy advice
 └───────────────┘
         │
         ▼
[UI Canvas Render & Paced Delay Processing]
