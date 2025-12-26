## Problem Statement
The challenge is to design and implement a modular, agentic automation system that takes product data  and autonomously generates structured, machine-readable content pages for marketing purposes. The system must demonstrate:

* Multi-agent coordination without monolithic code
* Reusable content logic blocks that compose into multiple pages
* Clear separation with each agent having a single responsibility
* Rule-based transformations that map product data → marketing content → JSON output

The core constraint: all logic must be expressed through agents and reusable blocks, not hardcoded strings.

## Solution Overview
Implemented a multi-agent orchestration system with the following architecture:

Core Design Pattern: Agent-Based Orchestration
Instead of a single content generation function, we created:
* Product Data Model - Single source of data
* Content Logic Blocks - Reusable transformation functions 
* Specialized Agents - Each with single responsibility (FAQAgent, ProductPageAgent, ComparisonAgent)
* Orchestrator - Central hub that coordinates agent execution 
* Template System - Implicit in agent execute() methods

## Why This Architecture?

* Modularity: Each agent is independent, testable, replaceable
* Extensibility: Add new agents without modifying existing code
* Composability: Logic blocks are reused across multiple agents
* Maintainability: Clear responsibilities, no hidden state
* Scalability: Easy to add new products or content types

## Data Flow Diagram
┌─────────────────────┐
│  Product Input      │
│  (GlowBoost data)   │
└──────────┬──────────┘
           │
           ↓
    ┌──────────────┐
    │ Orchestrator │
    │   (DAG Hub)  │
    └──────────────┘
       │   │   │
       │   │   └─────────────────────┐
       │   │                         │
       ↓   ↓                         ↓
    ┌─────────┐  ┌──────────────┐  ┌─────────────┐
    │ FAQAgent│  │ProductPageAgt│  │ComparisonAgt│
    └────┬────┘  └──────┬───────┘  └────┬────────┘
         │              │               │
         ├─→ Uses       ├─→ Uses        ├─→ Uses
         │   Logic      │   Logic       │   Compare
         │   Blocks     │   Blocks      │   Blocks
         │              │               │
         ↓              ↓               ↓
    ┌─────────┐  ┌──────────────┐  ┌─────────────┐
    │faqagent │  │productpage   │  │comparison   │
    │.json    │  │agent.json    │  │agent.json   │
    └─────────┘  └──────────────┘  └─────────────┘

## Scopes & Assumptions
### In Scope 
* Parsing product data into a clean internal model
* Generating 15+ categorized questions (5 categories: Informational, Usage, Safety, Purchase, Comparison)
* Creating 3 content pages (FAQ, Product Description, Comparison)
* Implementing 7+ reusable logic blocks
* Outputting machine-readable JSON files
* Rule-based content generation (no LLM APIs)
* Multi-agent coordination through orchestrator
* Type hints and error handling throughout
* Clean, professional code structure

### Assumptions 
* Product input data is well-formed and complete
* All 8 product fields are provided
* Question generation uses template-based rules
* Content logic blocks are deterministic (same input → same output)
* JSON output is sufficient for evaluation
* Single-threaded sequential execution is acceptable
* Orchestrator manages all inter-agent communication

## System Design
1. Product Model
* Responsibility: Single source of truth for product data
* Normalizes input into typed structure
* Provides to_dict() for serialization
* Contains COMPARISON_PRODUCT for testing


2. Logic Blocks
* Responsibility: Transform product data into marketing copy
* Pure functions (no side effects)
* Composable and reusable
* Registry pattern for discoverability
* Used by multiple agents
* Design Decision: Registry pattern allows:
* Easy discovery via get_block(name)

3. BaseAgent 
* Responsibility: Enforce consistent agent interface
* Input validation contract
* Execution with error handling
* Status tracking (IDLE, RUNNING, COMPLETED, FAILED)

4. Specialized Agents
* Input: Product
* Process:
+ Generate 15+ questions (via QuestionGeneratorAgent)
+ Map each question to answer via logic blocks
+ Categorize by type (Informational, Usage, Safety, Purchase, Comparison)
+ Output: {page_title, product_name, faqs: [{category, question, answer}]}

4. ProductPageAgent 
* Input: Product

* Process:
+ Extract basic fields (name, price, benefits, etc.)
+ Compose full description using all logic blocks
+ Structure for product page display
+ Output: {product_name, price, benefits, ingredients, usage, side_effects, full_description}

5. ComparisonAgent (src/agents/comparison_agent.py)
* Input: Product (+ COMPARISON_PRODUCT injected at init)

* Process:
+ Compare ingredients, benefits, prices
+ Use comparison logic blocks
+ Structure for side-by-side display
+ Output: {title, products, ingredients_comparison, benefits_comparison, price_comparison}

6. QuestionGeneratorAgent (src/agents/question_generator_agent.py)
* Input: Product
* Process: Template-based question generation across 5 categories
* Output: [{category, question}] (15 items)

5. Orchestrator
* Responsibility: Coordinate multi-agent execution
* Register agents without coupling
* Execute sequentially (no agent-to-agent calls)
* Handle output persistence
* Track execution status
* Design Decision: Orchestrator as mediator
* No agent knows about other agents
* All communication through orchestrator
* Easy to swap agents

## Conclusion
This multi-agent content generation system demonstrates:
* Strong system design through agent abstraction and orchestration
* Code reusability via logic blocks 
* Clean architecture with clear separation of concerns
* Production-ready code that is extensible and maintainable

The system successfully transforms minimal product data into comprehensive marketing content through modular, agentic automation.