from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def Home():
    return {
        'Message' : "Judge route is working"
    }



@router.get('/Health')
def health():
    return {
        'message' : "Health is stable"
    }