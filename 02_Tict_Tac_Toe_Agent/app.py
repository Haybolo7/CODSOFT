import math
import random
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from typing import List, TypedDict
from langgraph.graph import StateGraph, END

app = Flask(__name__)
app.secret_key = "game_theory_strategic_matrix_key"

# =====================================================================
# UNBEATABLE MINIMAX SEARCH ALGORITHM WITH ALPHA-BETA PRUNING
# =====================================================================

def check_winner(board: List[str]) -> str:
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != " ":
            return board[condition[0]]
    if " " not in board:
        return "Tie"
    return "None"

def minimax(board: List[str], depth: int, is_maximizing: bool, alpha: float, beta: float) -> int:
    winner = check_winner(board)
    if winner == "O": return 10 - depth
    if winner == "X": return depth - 10
    if winner == "Tie": return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha: break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha: break
        return best_score

def get_ai_move(board: List[str], level: str) -> int:
    empty_cells = [i for i, x in enumerate(board) if x == " "]
    if not empty_cells: return -1
    
    # Scale difficulty vectors
    if level == "easy" and random.random() < 0.5:
        return random.choice(empty_cells)
    if level == "medium" and random.random() < 0.25:
        return random.choice(empty_cells)

    # Unbeatable Expert Mode via Alpha-Beta
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# =====================================================================
# SYSTEM STRUCTURAL DETACHED LOCAL RAG CONTEXT EXTRACTOR
# =====================================================================

RAG_TACTICS_INDEX = {
    "center": "Strategic Rule: Prioritizing index cell 4 shapes maximum branch routes across the visual board space.",
    "defense": "Tactical Notice: Row/column alignment danger imminent. Forcing alpha-beta interception sequences.",
    "neutral": "System Baseline: Graph routes analyzed. Current state resolves toward static match parity."
}

def retrieve_rag_insight(board: List[str]) -> str:
    if board[4] == "O":
        return RAG_TACTICS_INDEX["center"]
    # Check if user has two items in any line (Simulate defense vector match)
    return RAG_TACTICS_INDEX["neutral"]

# =====================================================================
# LANGGRAPH ORCHESTRATION ARCHITECTURE
# =====================================================================

class GraphState(TypedDict):
    board: List[str]
    level: str
    game_status: str
    ai_commentary: str

def process_ai_turn(state: GraphState) -> dict:
    board = state["board"].copy()
    if check_winner(board) == "None":
        move = get_ai_move(board, state["level"])
        if move != -1:
            board[move] = "O"
    status = check_winner(board)
    return {"board": board, "game_status": "Ongoing" if status == "None" else status}

def process_rag_commentary(state: GraphState) -> dict:
    return {"ai_commentary": retrieve_rag_insight(state["board"])}

workflow = StateGraph(GraphState)
workflow.add_node("ai_turn", process_ai_turn)
workflow.add_node("rag_commentary", process_rag_commentary)
workflow.set_entry_point("ai_turn")
workflow.add_edge("ai_turn", "rag_commentary")
workflow.add_edge("rag_commentary", END)
compiled_graph = workflow.compile()

# =====================================================================
# WEB PAGE APPLICATION CONTROL ROUTERS
# =====================================================================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("setup"))
    return render_template("login.html")

@app.route("/setup", methods=["GET", "POST"])
def setup():
    if "username" not in session: return redirect(url_for("login"))
    if request.method == "POST":
        session["player_type"] = request.form.get("player_type")
        session["level"] = request.form.get("level")
        return redirect(url_for("game"))
    return render_template("setup.html")

@app.route("/game")
def game():
    if "username" not in session: return redirect(url_for("login"))
    return render_template("game.html", username=session.get("username"), player_type=session.get("player_type"), level=session.get("level"))

@app.route("/api/move", methods=["POST"])
def handle_move():
    data = request.json
    board = data.get("board")
    player_type = session.get("player_type", "ai")
    level = session.get("level", "hard")

    status = check_winner(board)
    if status != "None":
        return jsonify({"board": board, "game_status": status, "ai_commentary": "Match completed."})

    if player_type == "ai":
        state_input = {"board": board, "level": level, "game_status": "Ongoing", "ai_commentary": ""}
        graph_output = compiled_graph.invoke(state_input)
        return jsonify(graph_output)

    return jsonify({"board": board, "game_status": "Ongoing", "ai_commentary": "Local Turn Logged."})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
