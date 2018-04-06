from django.contrib.auth import authenticate
from django.forms.models import model_to_dict
from django.http import JsonResponse

from dashboard.logic import student_logic, educator_logic, general_logic

user = authenticate(username='student', password='1#lklsaK313')


def index(request):
    # Student Advices
    student_advices = student_logic.get_student_advices(student_id=user.id)

    # Student Predictions
    predictions = student_logic.get_student_predictions(student_id=user.id)

    # Student Recommendations
    recommendations = student_logic.get_student_recommendations(student_id=user.id)

    # For Testing Only
    result = {
        'student_advices': list(student_advices.values()),
        'student_predictions': predictions,
        'student_recommendations': recommendations
    }

    return JsonResponse(result, safe=False)


def student_courses(request):
    # Student Courses
    courses = student_logic.get_student_courses(student_id=user.id)

    # For Testing Only
    result = {
        'student_courses': courses
    }

    return JsonResponse(result, safe=False)


def educator_profile(request, educator_id):
    # Educator Info
    educator_info = educator_logic.get_educator_info(educator_id)

    # Educator Accounts
    educator_accounts = educator_logic.get_educator_accounts(educator_id)

    # Review Items
    review_items = general_logic.get_review_items()

    # For Testing Only
    result = {
        'educator_info': model_to_dict(educator_info),
        'educator_accounts': list(educator_accounts.values()),
        'review_items': list(review_items.values())
    }

    return JsonResponse(result, safe=False)
