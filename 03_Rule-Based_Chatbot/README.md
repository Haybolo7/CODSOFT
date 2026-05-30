# Blinkit Rule-Based Chatbot

A lightweight, efficient command-line conversational agent implemented in Python. This chatbot mimics a real-time quick-commerce support desk (inspired by Blinkit), using deterministic rule-based logic to process client text queries regarding order statuses, policy scopes, refunds, and simple engagements.

##  ✨ Key Features
1. Order Management & Logistics Simulation: Handles critical e-commerce flows including conditional state processing for active order tracking, tracking cancellations, and managing damaged or missing items.


2. Token Optimization Strategy: Leverages logical membership expressions (any(keyword in user_input...)) to evaluate array intersections efficiently, allowing multi-token synonyms (e.g., missing, damaged, spoiled) to map onto single deterministic return vectors.


3. State-isolated Chronological Validation: Isolates a capture initialization sequence (time.ctime()) to provide invariant terminal time reflections within an active evaluation scope.

## 🚀 Deployment Instructions

Prerequisites-

-> Python 3.x environment installed.

-> No external third-party dependencies required (Standard Library only).

## 💬 Example Usage

BLINKIT RULE-BASED CUSTOMER TERMINAL ASSISTANT

Chatbot: Hi! I'm a simple chatbot, I'm here to assist you with Blinkit support!

Me: Where is my order?

Chatbot: Your order is packed and the delivery partner is on the way. Arriving in 8 minutes!

Me: help

Chatbot:   **You may ask me about the following queries:

  -> Check active order tracking status ('track')...
  
Me: bye

Chatbot: Goodbye! Have a great day!


## 🛠️ System Architecture & Workflow

The assistant operates as a state-free sequential evaluation pipeline within an infinite execution loop:

```text
[ User Input Vector ] ──> [ Case Insensitivity Normalization ]
                                      │
                                      ▼
                      [ Conditional Keyword Parsing ]
                                      │
           ┌──────────────────────────┼──────────────────────────┐
           ▼                          ▼                          ▼
   [ Core Logistics ]       [ Contextual Support ]     [ System Fallbacks ]
   - Order Tracking         - Greeting Handlers        - Help Menu Display
   - Damage Reporting       - Identity/Capabilities    - Static Date/Time
   - Refund Matrix          - Entertainment Rules      - Default Exception
