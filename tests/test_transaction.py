import json

def test_create_transaction(client):
    """測試新增交易"""
    response = client.post('/transactions',
        # 把 data 轉成 JSON 字串
        data = json.dumps({ 
            'type': 'expense',
            'amount': 100,
            'description': 'test',
            'category': '餐飲'
        }),
        content_type = 'application/json'
    )

    # assert True 測試通過
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['amount'] == 100 # 確認金額正確
    assert data['type'] == 'expense' # 確認type正確

def test_get_transactions(client):
    """測試取得所有交易"""
    response = client.get('/transactions')
    assert response.status_code == 200

def test_get_transactions_not_found(client):
    """測試查詢不存在的紀錄"""
    response = client.get('/transactions/9999')
    assert response.status_code == 404