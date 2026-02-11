import json
from app import app
import io

def test_word_download():
    client = app.test_client()
    data = {
        "query": "ax ai",
        "results": [
            {"title": "Test Word News 1", "snippet": "Snippet 1", "source": "Source 1", "link": "http://test1.com"},
            {"title": "Test Word News 2", "snippet": "Snippet 2", "source": "Source 2", "link": "http://test2.com"}
        ],
        "head_message": "Editorial Summary Test"
    }
    response = client.post('/download_word', 
                           data=json.dumps(data),
                           content_type='application/json')
    
    assert response.status_code == 200
    assert response.mimetype == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    assert len(response.data) > 0
    print("Word download test passed!")

if __name__ == "__main__":
    try:
        test_word_download()
    except Exception as e:
        print(f"Test failed: {e}")
