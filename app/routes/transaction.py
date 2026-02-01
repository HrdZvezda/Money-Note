from flask import request, jsonify
from app.routes import main_bp
from app import db
from app.models.transaction import Transaction

@main_bp.route('/transactions', methods=['GET'])
def get_transactions():
    """取得所有交易紀錄"""
    transactions = Transaction.query.all()

    # result = []
    # for t in transactions:
        # result.append(t.to_dict())
    # return jsonify(result)
    return jsonify([t.to_dict() for t in transactions])

@main_bp.route('/transactions/<int:id>', methods=['GET'])
def get_transaction(id: int):
    """取得單筆交易紀錄"""
    transaction = Transaction.query.get_or_404(id)

    return jsonify(transaction.to_dict())

@main_bp.route('/transactions', methods=['POST'])
def create_transaction():
    """新增交易紀錄"""
    data = request.get_json() # 取得前端傳來的JSON

    # 建立新資料
    transaction = Transaction(
        type=data.get('type'),
        amount=data.get('amount'),
        description=data.get('description'),
        category=data.get('category')
    )

    db.session.add(transaction) # 加到資料庫
    db.session.commit() # 確認儲存

    return jsonify(transaction.to_dict()), 201

@main_bp.route('/transactions/<int:id>', methods=['PUT'])
def update_transaction(id: int):
    """修改交易紀錄"""
    transaction = Transaction.query.get_or_404(id)
    data = request.get_json()

    # 有傳就改, 沒傳就保持原值
    transaction.type = data.get('type', transaction.type)
    transaction.amount = data.get('amount', transaction.amount)
    transaction.description = data.get('description', transaction.description)
    transaction.category = data.get('category', transaction.category)

    db.session.commit()

    return jsonify(transaction.to_dict())

@main_bp.route('/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id: int):
    """刪除交易紀錄"""
    transaction = Transaction.query.get_or_404(id)

    db.session.delete(transaction)
    db.session.commit()

    return jsonify({'message': 'delete successful'}), 200





