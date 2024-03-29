from django.db import connection
from django.db.models import Count, DateField, IntegerField
from django.db.models.functions import Cast, TruncDate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from one_big_thing.api_serializers import (
    DateJoinedSerializer,
    DepartmentBreakdownSerializer,
    JwtTokenObtainPairSerializer,
)
from one_big_thing.learning import models
from one_big_thing.learning.api_permissions import IsAPIUser


class UserSignupStatsView(APIView):
    """
    Endpoint used by 10DS to get information about user signups per date
    """

    permission_classes = (
        IsAuthenticated,
        IsAPIUser,
    )

    def get(self, request):
        signups = get_signups_by_date()
        serializer = DateJoinedSerializer(
            signups,
            many=True,
        )
        serialized_data = serializer.data
        return Response(serialized_data)


class UserStatisticsView(APIView):
    """
    Endpoint used by 10DS to get information about department signups
    """

    permission_classes = (
        IsAuthenticated,
        IsAPIUser,
    )

    def get(self, request):
        department_dict = get_learning_breakdown_data()
        serializer = DepartmentBreakdownSerializer(department_dict, many=True, partial=True, allow_null=True)
        serialized_data = serializer.data
        return Response(serialized_data)


def get_signups_by_date():
    """
    Calculates the number of signups per day
    @return: A dictionary containing a key for date, and value of number of signups
    """
    signups = (
        models.User.objects.annotate(signup_date=TruncDate("date_joined"))
        .values("signup_date")
        .annotate(
            count=Count("id", distinct=True),
            date_joined=Cast("signup_date", output_field=DateField()),
            number_of_signups=Cast("count", output_field=IntegerField()),
        )
        .values("date_joined", "number_of_signups")
    )

    return signups


def get_learning_breakdown_data():
    """
    Calculates the number of signups per combination of department/grade/profession
    @return: A queryset that contains a list of each grouping
    """

    with connection.cursor() as cursor:
        # Define your SQL query
        sql_query = """
SELECT
    DATE(date_joined) as date_joined,
    department,
    grade,
    profession,
    count(*) as number_of_sign_ups,
    count(CASE WHEN u.has_completed_pre_survey THEN 1 END) as completed_first_evaluation,
    count(CASE WHEN u.has_completed_post_survey THEN 1 END) as completed_second_evaluation,
    sum(l.completed_1_hours_of_learning) as completed_1_hours_of_learning,
    sum(l.completed_2_hours_of_learning) as completed_2_hours_of_learning,
    sum(l.completed_3_hours_of_learning) as completed_3_hours_of_learning,
    sum(l.completed_4_hours_of_learning) as completed_4_hours_of_learning,
    sum(l.completed_5_hours_of_learning) as completed_5_hours_of_learning,
    sum(l.completed_6_hours_of_learning) as completed_6_hours_of_learning,
    sum(l.completed_7_plus_hours_of_learning) as completed_7_plus_hours_of_learning
FROM public.learning_user as u
LEFT JOIN (
    SELECT
    user_id,
    CASE
        WHEN hours_learning > 1  THEN 1
        ELSE 0
        END as completed_1_hours_of_learning,
    CASE
        WHEN hours_learning > 2  THEN 1
        ELSE 0
    END as completed_2_hours_of_learning,
    CASE
        WHEN hours_learning > 3  THEN 1
        ELSE 0
    END as completed_3_hours_of_learning,
    CASE
        WHEN hours_learning > 4  THEN 1
        ELSE 0
    END as completed_4_hours_of_learning,
    CASE
        WHEN hours_learning > 5  THEN 1
        ELSE 0
    END as completed_5_hours_of_learning,
    CASE
        WHEN hours_learning > 6  THEN 1
        ELSE 0
    END as completed_6_hours_of_learning,
    CASE
        WHEN hours_learning > 7  THEN 1
        ELSE 0
    END as completed_7_plus_hours_of_learning
    FROM (
        SELECT
            sum(time_to_complete)/60 as hours_learning,
            user_id
        FROM public.learning_learning
        GROUP BY user_id
    ) inner_l
) l
ON l.user_id = u.id
GROUP BY department,
grade,
profession,
date_joined;"""

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch results, e.g., fetch all rows
        results = cursor.fetchall()

    field_names = [
        "date_joined",
        "department",
        "grade",
        "profession",
        "number_of_sign_ups",
        "completed_first_evaluation",
        "completed_second_evaluation",
        "completed_1_hours_of_learning",
        "completed_2_hours_of_learning",
        "completed_3_hours_of_learning",
        "completed_4_hours_of_learning",
        "completed_5_hours_of_learning",
        "completed_6_hours_of_learning",
        "completed_7_plus_hours_of_learning",
    ]

    # Process the results
    for row in results:
        yield dict(zip(field_names, row))


class JwtTokenObtainPairView(TokenObtainPairView):
    serializer_class = JwtTokenObtainPairSerializer
