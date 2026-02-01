from datetime import datetime
from app import db
from typing import Optional

class Transaction(db.Model):
    """Deal Category Model"""
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False) # income | expense
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50))
    date = db.Column(db.Date, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        """轉換成dict, 給API回傳用"""
        return{
            'id': self.id,
            'type': self.type,
            'amount': self.amount,
            'description': self.description,
            'category': self.category,
            'date': self.date.isoformat() if self.date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }