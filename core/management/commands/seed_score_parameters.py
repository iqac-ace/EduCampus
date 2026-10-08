from django.core.management.base import BaseCommand
from core.models import ScoreParameter


class Command(BaseCommand):

    help = "Create the 10 ACE student performance parameters"

    def handle(self, *args, **options):

        parameters = [

            (
                "ACADEMIC",
                "Academic Performance",
                20,
                1
            ),

            (
                "ATTENDANCE",
                "Attendance & Academic Discipline",
                10,
                2
            ),

            (
                "LEARNING",
                "Learning & Certification",
                10,
                3
            ),

            (
                "TECHNICAL",
                "Technical Skills & Projects",
                15,
                4
            ),

            (
                "INTERNSHIP",
                "Internship & Industry Exposure",
                10,
                5
            ),

            (
                "RESEARCH",
                "Research, Innovation & IPR",
                10,
                6
            ),

            (
                "CAREER",
                "Placement & Career Readiness",
                10,
                7
            ),

            (
                "LEADERSHIP",
                "Leadership & Student Engagement",
                5,
                8
            ),

            (
                "SOCIAL",
                "Social Responsibility & Institutional Contribution",
                5,
                9
            ),

            (
                "SPORTS",
                "Sports, Cultural & Achievements",
                5,
                10
            ),
        ]

        valid_codes = [
            item[0]
            for item in parameters
        ]

        # Hide old/unused parameters such as A1, A2, B1 etc.
        # They are not deleted from the database.
        ScoreParameter.objects.exclude(
            code__in=valid_codes
        ).update(
            active=False
        )

        for (
            code,
            name,
            max_points,
            order
        ) in parameters:

            ScoreParameter.objects.update_or_create(

                code=code,

                defaults={

                    "name": name,

                    "max_points": max_points,

                    "order": order,

                    "active": True,
                }
            )

        self.stdout.write(

            self.style.SUCCESS(
                "10 ACE performance parameters created/updated successfully."
            )
        )