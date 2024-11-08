from flask import Blueprint, request, jsonify
import uuid  
from utils.gemini import chat
from utils.search_embeddings import search_embeddings
from utils.store_embeddings import initialize_chromadb, get_or_create_collection



chat_bp = Blueprint('chat', __name__)
chat_threads = {}
chroma_client = initialize_chromadb()
collection = get_or_create_collection(chroma_client,collection_name="prompts")
def get_asset_by_chat_thread(chat_id):
    """
    Retrieve the asset ID associated with a given chat thread ID.
    Expects 'chat_thread_id' as a query parameter.
    """
    chat_thread_id = chat_id

    if not chat_thread_id:
        return jsonify({"error": "Chat thread ID is required"}), 400

    if chat_thread_id not in chat_threads:
        
        return jsonify({"error": "Invalid chat thread ID"}), 404

    asset_id = chat_threads[chat_thread_id]["asset_id"]
    
    return asset_id

def generate_chat_thread_id():
    """Generates a unique chat thread ID."""
    return str(uuid.uuid4())

@chat_bp.route('/api/chat/start', methods=['POST'])
def start_chat():
    """
    Start a new chat thread for a given asset.
    Expects JSON body containing 'asset_id'.
    """
    data = request.json or {}
    asset_id = data.get('asset_id')

    if not asset_id:
        return jsonify({"error": "Asset ID is required"}), 400
    
    chat_thread_id = generate_chat_thread_id()
    chat_threads[chat_thread_id] = {
        "asset_id": asset_id,
        "messages": [{"sender": "system", "message": "Chat started"}]
    }

    return jsonify({"chat_thread_id": chat_thread_id}), 201


@chat_bp.route('/api/chat/message', methods=['POST'])
def send_message():
    """
    Send a message to an existing chat thread.
    Expects JSON body containing 'chat_thread_id' and 'message'.
    """
    data = request.json or {}
    chat_thread_id = data.get('chat_thread_id')
    user_message = data.get('message')

    if not chat_thread_id or not user_message:
        return jsonify({"error": "Chat thread ID and user message are required"}), 400

    if chat_thread_id not in chat_threads:
        return jsonify({"error": "Invalid chat thread ID"}), 404
    assertID = get_asset_by_chat_thread(chat_id=chat_thread_id)
    # Store user message
    chat_threads[chat_thread_id]["messages"].append({"sender": "user", "message": user_message})
    
    result = search_embeddings(collection=collection, query=user_message, assertID=assertID)
    match_text = result['documents'][0][0]
    prompts = "given the context and user query answer user query with the context userquery:{} , context:{} ".format(user_message,match_text)
    agent_response = chat(query=prompts)
    chat_threads[chat_thread_id]["messages"].append({"sender": "agent", "message": agent_response})

    return jsonify({"agent_response": agent_response})


@chat_bp.route('/api/chat/history', methods=['GET'])
def get_chat_history():
    """
    Retrieve chat history for a given chat thread.
    Expects 'chat_thread_id' as a query parameter.
    """
    chat_thread_id = request.args.get('chat_thread_id')

    if not chat_thread_id:
        return jsonify({"error": "Chat thread ID is required"}), 400

    if chat_thread_id not in chat_threads:
        return jsonify({"error": "Invalid chat thread ID"}), 404

    chat_history = chat_threads[chat_thread_id]["messages"]
    return jsonify({"chat_history": chat_history})


