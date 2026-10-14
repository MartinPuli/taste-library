# Agent packaging decisions

Official documentation checked on October 14, 2026. These are implementation choices for this collection, not a claim that one format works best for every agent.

## Skills

The [Agent Skills specification](https://agentskills.io/specification) defines a SKILL.md entry point with name and description metadata, followed by instructions and optional supporting files. It recommends loading details progressively. This repo keeps the skill short, makes its trigger specific to design-reference selection, and puts access details in one linked reference.

The skill can travel independently of the dataset. It supports both local queries and direct public-file reads, preserving user constraints and distinguishing observations from proposals.

## Repository instructions

[AGENTS.md](https://agents.md/) provides a predictable place for agents to find repository guidance. Our file describes selection, evidence interpretation, and maintenance. It links to detailed procedures rather than embedding hundreds of brand records.

The compact discovery catalog omits raw component descriptions. Detailed catalog entries then point to section files, which include provenance and exact JSON pointers. This keeps a simple search from loading the full collection.

## MCP

The current [MCP tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) describes discoverable tools with input schemas and structured results. [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources) expose addressable content. Those would suit search, section retrieval, and comparison when an agent needs a tool connection.

This delivery uses public files and a local CLI, as requested. It does not require a running MCP service. A future adapter should wrap the same query functions, expose read-only resources, preserve provenance, and validate its outputs through the [official SDK](https://github.com/modelcontextprotocol/python-sdk). The installed SDK checked during research was 2.3.0; no SDK is a runtime dependency of this library.

## Discovery and verification

The [llms.txt v2 proposal](https://llmstxt.org/), updated August 10, 2026, describes a concise index linking to machine-readable content. This repo publishes one with direct raw-file URLs. Client discovery remains client-dependent; the README also gives an explicit entry link.

Validation checks reference coverage, pointers, source hashes, and generated-file consistency. Worked briefs test whether retrieval reaches the evidence needed to make a choice. These checks demonstrate access and consistency, not a universal score for design quality.
