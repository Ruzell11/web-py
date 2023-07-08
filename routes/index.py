from fastapi import APIRouter
from controller.generalController import firstController
router = APIRouter()

@router.get('/test')
def testEndpoint():
    return firstController()