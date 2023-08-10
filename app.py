import os
from flask import Flask, render_template, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random
from backend.auth import requires_auth
from backend.models import setup_db, Genre, Prompt



app = Flask(__name__)
setup_db(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

PROMPOTS_PER_PAGE = 10

@app.route('/')
def index():
    return render_template('index.html')


'''''PROMOTS'''''

# Listing or creating prompts
@app.route('/prompts', methods =['GET'])
def get_all_prompts():
    page = request.args.get('page', 1, type=int)
    if page <= 0:
        page = 1

    prompts = Prompt.query.all()
    start = (page - 1) * PROMPOTS_PER_PAGE
    end = start + PROMPOTS_PER_PAGE

    formated_result = [p.format() for p in prompts]
    paginate_result = formated_result[start:end]

    if len(paginate_result) == 0:
        abort(404)

    return jsonify({"success" : True, "prompts" : paginate_result, "total_prompts" : len(formated_result)})

# Insert prompts
@app.route('/prompts', methods =['POST'])
@requires_auth(permission='add:prompt')
def add_prompt(payload):
    try:
        body = request.get_json()
        title = body.get('title', None)
        content = body.get('content', None)
        genre_id  =  body.get('genre_id', None)

        if not title or not content or not genre_id:
            abort(400)

        prompt = Prompt(title, str(content), genre_id)
        prompt.insert()
        return jsonify({"success": True, "Prompts" : len(Prompt.query.all())})
    except:
        abort(422)

# Get prompt by id   
@app.route('/prompts/<int:id>', methods =['GET'])
def get_prompt_by_id(id):
    prompt = Prompt.query.get_or_404(id)
    return jsonify({"success":True, "prompt":prompt.format()})

# delete prompt by id   
@app.route('/prompts/<int:id>', methods =['DELETE'])
@requires_auth(permission='delete:prompt')
def delete_prompt_by_id(payload, id):
    prompt = Prompt.query.get_or_404(id)
    try:
        prompt.delete()
        return jsonify({"success":True, "prompt_id":id})
    except:
        abort(422)

# update prompt by id   
@app.route('/prompts/<int:id>', methods =['PATCH'])
@requires_auth(permission='update:prompt')
def update_prompt_by_id(payload, id):
    prompt = Prompt.query.get_or_404(id)
    try:
        body = request.get_json()
        if(not body):
            abort(400)

        title = body.get('title', None)
        content = body.get('content', None)
        genre_id  =  body.get('genre_id', None)

        if not title and not content and not genre_id:
            abort(400)

        if title is not None:
            prompt.title = title
        if content is not None:
            prompt.content = content
        if genre_id is not None:
            prompt.genre_id = genre_id

        prompt.update()
        return jsonify({"success": True, "prompt_id":id })
    except:
        abort(422)


''''' GENRES'''''

# Listing or creating genres
@app.route('/genres', methods =['GET'])
def get_all_genres():
    page = request.args.get('page', 1, type=int)
    if page <= 0:
        page = 1

    prompts = Genre.query.all()
    start = (page - 1) * PROMPOTS_PER_PAGE
    end = start + PROMPOTS_PER_PAGE

    formated_result = [p.format() for p in prompts]
    paginate_result = formated_result[start:end]

    if len(paginate_result) == 0:
        abort(404)

    return jsonify({"success" : True, "genres" : paginate_result, "total_genres" : len(formated_result)})

# Insert genres
@app.route('/genres', methods =['POST'])
@requires_auth(permission='add:genre')
def add_genre(payload):
    try:
        body = request.get_json()
        name = body['name']
        description = body['description']

        g = Genre(name=name, description=description)
        g.insert()
        return jsonify({"success": True, "total_genres" : len(Genre.query.all())})
    except:
        abort(422)

# Get genre by id   
@app.route('/genres/<int:id>', methods =['GET'])
def get_genre_by_id(id):
    genre = Genre.query.get_or_404(id)
    return jsonify({"success":True, "genre":genre.format()})

# delete genre by id   
@app.route('/genres/<int:id>', methods =['DELETE'])
@requires_auth(permission='delete:genre')
def delete_genre_by_id(payload, id):
    genre = Genre.query.get_or_404(id)
    try:
        genre.delete()
        return jsonify({"success":True, "genre_id":id})
    except:
        abort(422)

# update genre by id   
@app.route('/genres/<int:id>', methods =['PATCH'])
@requires_auth(permission='update:genre')
def update_genre_by_id(payload, id):
    genre = Genre.query.get_or_404(id)
    try:
        body = request.get_json()
        if(not body):
            abort(400)

        name = body.get('name', None)
        description = body.get('description', None)

        if not name and not description:
            abort(400)

        if name is not None:
            genre.name = name
        if description is not None:
            genre.description = description

        genre.update()
        return jsonify({"success": True, "genre_id":id })
    except:
        abort(422)



''''' ERRORS HANDLER'''''

@app.errorhandler(404)
def not_found(error):
    return (
        jsonify({"success": False, "error": 404, "message": "resource not found"}),
        404,
    )

@app.errorhandler(422)
def unprocessable(error):
    return (
        jsonify({"success": False, "error": 422, "message": "unprocessable"}),
        422,
    )

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

@app.errorhandler(405)
def not_found(error):
    return (
        jsonify({"success": False, "error": 405, "message": "method not allowed"}),
        405,
    )
            
