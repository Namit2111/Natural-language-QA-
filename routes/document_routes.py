import os
from flask import Blueprint, request, jsonify
from utils.file_loader import load_file
from utils.creat_embeddings import create_embeddings
from utils.store_embeddings import initialize_chromadb,store_embeddings,get_or_create_collection
from config.config import UPLOAD_FOLDER,ALLOWED_EXTENSIONS
import uuid



document_bp = Blueprint('document', __name__)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@document_bp.route('/api/documents/process', methods=['POST'])
def process_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    asserID = str(uuid.uuid4())
    documents = load_file(file_path)
    document_list , embeddings_list , ids_list , metadata_list = create_embeddings(documents=documents, metadata={"assertID": asserID},id=asserID)
    chroma_client = initialize_chromadb()
    collection = get_or_create_collection(chroma_client,collection_name="prompts")
    store_embeddings(collection, document_list, embeddings_list, ids_list, metadata_list)

    return jsonify({"asset_id": asserID, "file_path": file_path})
