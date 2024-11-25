from flask import Blueprint, request, jsonify
from app.models import db, Account

account_bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@account_bp.route('/', methods=['POST'])
def create_account():
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    account = Account(user_id=user_id)
    db.session.add(account)
    db.session.commit()
    return {'message': 'Account created successfully', 'account': {'id': account.id, 'balance': account.balance}}, 201
