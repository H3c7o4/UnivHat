from rest_framework import routers
from courses.views import Courseviewset, Evaluationviewset, Classroommviewset

router = routers.DefaultRouter()
router.register('courses', Courseviewset)
router.register('Evaluations', Evaluationviewset)
router.register('classrooms', Classroommviewset)