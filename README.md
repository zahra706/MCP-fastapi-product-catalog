# 🤖 Lab: Building an AI-Ready Product Catalog with FastAPI and MCP

## 🧭 Overview

This lab guides you through the process of **creating a Product Catalog API** using **FastAPI**, and then transforming it into an **AI-accessible service** using the **Model Context Protocol (MCP)** with **FastMCP**.

You’ll build a RESTful backend in **Part 1**, and in **Part 2**, you’ll connect it to an MCP server — enabling **AI agents** (like Claude) to call your API directly.

---

## 🎯 Objectives

- Build and test a FastAPI-based Product Catalog API.
- Expose the API as AI-callable tools via FastMCP.
- Learn to integrate AI-ready endpoints using the MCP standard.

---

## 🧩 Prerequisites

- **Python 3.10+** installed  
- Basic understanding of **Python**, **REST APIs**, and **JSON**  
- Familiarity with terminal commands and virtual environments  
- Installed packages: `fastapi[all]`, `fastmcp`, and `uvicorn` (via `pip` or `uv`)  
- Optional: **Claude Desktop** (for AI tool testing)  
- Code editor (e.g., **VS Code**)  
- Project directory (e.g., `product-catalog-lab`)  

⏱️ **Estimated Duration:** 90 minutes  

---

## 🧱 Part 1 – Building the FastAPI Product Catalog API

### 🎯 Objective
Create a FastAPI application with endpoints to list all products and retrieve a product by ID, using **Pydantic models** for validation and a mock in-memory database.

### 🧰 Step 1.1: Set Up Your Environment

```bash
mkdir product-catalog-lab
cd product-catalog-lab
python -m venv venv
# Activate
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # macOS/Linux
pip install fastapi[all] uvicorn
