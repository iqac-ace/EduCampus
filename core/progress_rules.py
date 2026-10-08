PROGRESS_RULES = {

    # =========================================================
    # 1. ACADEMIC PERFORMANCE /20
    # =========================================================

    "ACADEMIC": {

        "name": "Academic Performance",
        "max_points": 20,

        "subtopics": {

            "PLUS2": {

                "label":
                    "+2 / 12th Standard Performance "
                    "(First-Year Provisional)",

                # Score is calculated from percentage
                "points": None,

                "requirements": [
                    "Board",
                    "School",
                    "Year of Passing",
                    "Group",
                    "12th Percentage",
                ]
            },

            "CGPA_9": {

                "label":
                    "CGPA / SGPA ≥ 9.0",

                "points": 20,

                "requirements": [
                    "Basis (CGPA or SGPA)",
                    "CGPA / SGPA",
                ]
            },

            "CGPA_8": {

                "label":
                    "CGPA / SGPA 8.0 - 8.99",

                "points": 17,

                "requirements": [
                    "Basis (CGPA or SGPA)",
                    "CGPA / SGPA",
                ]
            },

            "CGPA_7": {

                "label":
                    "CGPA / SGPA 7.0 - 7.99",

                "points": 14,

                "requirements": [
                    "Basis (CGPA or SGPA)",
                    "CGPA / SGPA",
                ]
            },

            "CGPA_6": {

                "label":
                    "CGPA / SGPA 6.0 - 6.99",

                "points": 10,

                "requirements": [
                    "Basis (CGPA or SGPA)",
                    "CGPA / SGPA",
                ]
            },

            "CGPA_5": {

                "label":
                    "CGPA / SGPA 5.0 - 5.99",

                "points": 6,

                "requirements": [
                    "Basis (CGPA or SGPA)",
                    "CGPA / SGPA",
                ]
            },

            "CGPA_LOW": {

                "label":
                    "CGPA / SGPA Below 5.0",

                "points": 3,

                "requirements": [
                    "Basis (CGPA or SGPA)",
                    "CGPA / SGPA",
                ]
            },
        }
    },


    # =========================================================
    # 2. ATTENDANCE /10
    # =========================================================

    "ATTENDANCE": {

        "name":
            "Attendance & Academic Discipline",

        "max_points": 10,

        "subtopics": {

            "ATT_95": {

                "label":
                    "Attendance ≥ 95%",

                "points": 10,

                "requirements": [
                    "Attendance Percentage",
                    "Semester / Period",
                ]
            },

            "ATT_90": {

                "label":
                    "Attendance 90 - 94%",

                "points": 8,

                "requirements": [
                    "Attendance Percentage",
                    "Semester / Period",
                ]
            },

            "ATT_85": {

                "label":
                    "Attendance 85 - 89%",

                "points": 6,

                "requirements": [
                    "Attendance Percentage",
                    "Semester / Period",
                ]
            },

            "ATT_80": {

                "label":
                    "Attendance 80 - 84%",

                "points": 4,

                "requirements": [
                    "Attendance Percentage",
                    "Semester / Period",
                ]
            },

            "ATT_LOW": {

                "label":
                    "Attendance Below 80%",

                "points": 0,

                "requirements": [
                    "Attendance Percentage",
                    "Semester / Period",
                ]
            },
        }
    },


    # =========================================================
    # 3. LEARNING & CERTIFICATION /10
    # =========================================================

    "LEARNING": {

        "name":
            "Learning & Certification",

        "max_points": 10,

        "subtopics": {

            "CERT_3_PLUS": {

                "label":
                    "3 or More Recognized Certifications",

                "points": 10,

                "requirements": [
                    "Certificate / Course Details",
                    "Provider / Institution",
                    "Completion Date / Year",
                ]
            },

            "CERT_2": {

                "label":
                    "2 Certifications",

                "points": 8,

                "requirements": [
                    "Certificate Details",
                    "Provider / Institution",
                    "Completion Date / Year",
                ]
            },

            "CERT_1": {

                "label":
                    "1 Certification",

                "points": 6,

                "requirements": [
                    "Certificate Name",
                    "Provider / Institution",
                    "Completion Date / Year",
                ]
            },

            "MOOC": {

                "label":
                    "Completed MOOCs / NPTEL / "
                    "SWAYAM / ODL Course",

                "points": 4,

                "requirements": [
                    "Course Name",
                    "Platform",
                    "Completion Details",
                ]
            },

            "STRUCTURED": {

                "label":
                    "Participated in Structured "
                    "Learning Programme",

                "points": 2,

                "requirements": [
                    "Programme Name",
                    "Organising Institution",
                    "Programme Date",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 4. TECHNICAL SKILLS & PROJECTS /15
    # =========================================================

    "TECHNICAL": {

        "name":
            "Technical Skills & Projects",

        "max_points": 15,

        "subtopics": {

            "NATIONAL_INTL": {

                "label":
                    "National / International Technical "
                    "Achievement or Exceptional Project",

                "points": 15,

                "requirements": [
                    "Project / Competition Name",
                    "Level",
                    "Achievement",
                ]
            },

            "MAJOR_ACHIEVEMENT": {

                "label":
                    "Major Hackathon / Technical "
                    "Competition Achievement",

                "points": 12,

                "requirements": [
                    "Event Name",
                    "Organiser",
                    "Achievement",
                ]
            },

            "FUNCTIONAL_PROJECT": {

                "label":
                    "Functional Industry / "
                    "Technical Project",

                "points": 10,

                "requirements": [
                    "Project Title",
                    "Technology / Tools Used",
                    "Project Description",
                ]
            },

            "ENGINEERING_EXPLORATION": {

                "label":
                    "Engineering Exploration / "
                    "Substantial Technical Project",

                "points": 8,

                "requirements": [
                    "Project Title",
                    "Technology / Tools Used",
                    "Project Description",
                ]
            },

            "PARTICIPATION": {

                "label":
                    "Participation in Hackathon / "
                    "Technical Competition",

                "points": 5,

                "requirements": [
                    "Event Name",
                    "Organiser",
                    "Participation Details",
                ]
            },

            "BASIC": {

                "label":
                    "Basic Technical Project / Activity",

                "points": 3,

                "requirements": [
                    "Project / Activity Name",
                    "Technology / Skill Used",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 5. INTERNSHIP & INDUSTRY EXPOSURE /10
    # =========================================================

    "INTERNSHIP": {

        "name":
            "Internship & Industry Exposure",

        "max_points": 10,

        "subtopics": {

            "EXCELLENT_PPO": {

                "label":
                    "Internship + Excellent Industry "
                    "Evaluation / PPO",

                "points": 10,

                "requirements": [
                    "Company / Organisation",
                    "Internship Title",
                    "Duration",
                    "Evaluation / PPO Details",
                ]
            },

            "SIX_PLUS_WEEKS": {

                "label":
                    "Internship ≥ 6 Weeks",

                "points": 8,

                "requirements": [
                    "Company / Organisation",
                    "Internship Title",
                    "Duration",
                ]
            },

            "FOUR_FIVE_WEEKS": {

                "label":
                    "Internship 4 - 5 Weeks",

                "points": 6,

                "requirements": [
                    "Company / Organisation",
                    "Internship Title",
                    "Duration",
                ]
            },

            "SHORT_TERM": {

                "label":
                    "Short-Term Internship / "
                    "Industry Project",

                "points": 4,

                "requirements": [
                    "Organisation",
                    "Activity / Project",
                    "Duration",
                ]
            },

            "VISIT_INTERACTION": {

                "label":
                    "Industrial Visit / "
                    "Expert Interaction Only",

                "points": 2,

                "requirements": [
                    "Company / Expert Name",
                    "Programme / Visit",
                    "Date",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 6. RESEARCH, INNOVATION & IPR /10
    # =========================================================

    "RESEARCH": {

        "name":
            "Research, Innovation & IPR",

        "max_points": 10,

        "subtopics": {

            "GRANTED_PATENT": {

                "label":
                    "Granted Patent / "
                    "Major Research Achievement",

                "points": 10,

                "requirements": [
                    "Patent / Research Title",
                    "Patent Number / Reference",
                    "Achievement Details",
                ]
            },

            "PATENT_SCOPUS_WOS": {

                "label":
                    "Published Patent / "
                    "Scopus / WoS Quality Publication",

                "points": 9,

                "requirements": [
                    "Title",
                    "Journal / Patent Details",
                    "DOI / Patent Reference",
                ]
            },

            "PUBLICATION_PROJECT": {

                "label":
                    "Research Publication / "
                    "Significant Research Project",

                "points": 7,

                "requirements": [
                    "Research Title",
                    "Publication / Project Details",
                    "Reference",
                ]
            },

            "PAPER_IIC": {

                "label":
                    "Paper Presentation / "
                    "IIC Innovation Project",

                "points": 5,

                "requirements": [
                    "Title",
                    "Event / Institution",
                    "Presentation / Project Details",
                ]
            },

            "PROTOTYPE_IDEA": {

                "label":
                    "Research Participation / "
                    "Prototype / Idea Submission",

                "points": 3,

                "requirements": [
                    "Title",
                    "Description",
                ]
            },

            "AWARENESS": {

                "label":
                    "Research Awareness Programme",

                "points": 1,

                "requirements": [
                    "Programme Name",
                    "Organising Institution",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 7. PLACEMENT & CAREER READINESS /10
    # =========================================================

    "CAREER": {

        "name":
            "Placement & Career Readiness",

        "max_points": 10,

        "subtopics": {

            "PLACED_HIGHER_STUDIES": {

                "label":
                    "Placement / PPO / "
                    "Higher-Study Admission",

                "points": 10,

                "requirements": [
                    "Company / Institution",
                    "Offer / Admission Details",
                ]
            },

            "ADVANCED_READINESS": {

                "label":
                    "Advanced Placement Readiness",

                "points": 8,

                "requirements": [
                    "Programme / Assessment",
                    "Performance Details",
                ]
            },

            "STRONG_ASSESSMENT": {

                "label":
                    "Strong Performance in Aptitude / "
                    "Coding / Interview Assessment",

                "points": 6,

                "requirements": [
                    "Assessment Name",
                    "Score / Result",
                ]
            },

            "TRAINING_COMPLETED": {

                "label":
                    "Completed Placement Training",

                "points": 4,

                "requirements": [
                    "Training Name",
                    "Training Provider",
                    "Completion Details",
                ]
            },

            "CAREER_PROGRAMME": {

                "label":
                    "Participated in Career "
                    "Development Programme",

                "points": 2,

                "requirements": [
                    "Programme Name",
                    "Organising Institution",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 8. LEADERSHIP & STUDENT ENGAGEMENT /5
    # =========================================================

    "LEADERSHIP": {

        "name":
            "Leadership & Student Engagement",

        "max_points": 5,

        "subtopics": {

            "MAJOR_LEADER": {

                "label":
                    "Student Leader / Club Office Bearer / "
                    "Major Institutional Leadership",

                "points": 5,

                "requirements": [
                    "Role",
                    "Club / Organisation / Institution",
                    "Leadership Details",
                ]
            },

            "CLUB_LEADER": {

                "label":
                    "Active Domain Club / "
                    "Professional Society Leader",

                "points": 4,

                "requirements": [
                    "Role",
                    "Club / Professional Society",
                ]
            },

            "REGULAR_PARTICIPATION": {

                "label":
                    "Regular Club / Professional "
                    "Society Participation",

                "points": 3,

                "requirements": [
                    "Club / Professional Society",
                    "Activities",
                ]
            },

            "MENTOR_ACTIVITY": {

                "label":
                    "Peer Teaching / Mentoring / "
                    "Activity Participation",

                "points": 2,

                "requirements": [
                    "Activity",
                    "Role / Contribution",
                ]
            },

            "MEMBERSHIP": {

                "label":
                    "Membership Only",

                "points": 1,

                "requirements": [
                    "Club / Society / Body",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 9. SOCIAL RESPONSIBILITY /5
    # =========================================================

    "SOCIAL": {

        "name":
            "Social Responsibility & Institutional Contribution",

        "max_points": 5,

        "subtopics": {

            "LED_MAJOR": {

                "label":
                    "Led Major NSS / UBA / SDG / "
                    "IQAC / Institutional Initiative",

                "points": 5,

                "requirements": [
                    "Initiative / Programme",
                    "Role",
                    "Contribution",
                ]
            },

            "THREE_PLUS": {

                "label":
                    "Active Participation in "
                    "3 or More Activities",

                "points": 4,

                "requirements": [
                    "Activity Details",
                    "Number of Activities",
                ]
            },

            "TWO_ACTIVITIES": {

                "label":
                    "Participation in 2 Activities",

                "points": 3,

                "requirements": [
                    "Activity Details",
                ]
            },

            "ONE_ACTIVITY": {

                "label":
                    "Participation in 1 Activity",

                "points": 2,

                "requirements": [
                    "Activity Name",
                    "Participation Details",
                ]
            },

            "AWARENESS": {

                "label":
                    "Awareness Programme",

                "points": 1,

                "requirements": [
                    "Programme Name",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },


    # =========================================================
    # 10. SPORTS / CULTURAL / ACHIEVEMENTS /5
    # =========================================================

    "SPORTS": {

        "name":
            "Sports, Cultural & Achievements",

        "max_points": 5,

        "subtopics": {

            "NATIONAL_INTL": {

                "label":
                    "National / International Achievement",

                "points": 5,

                "requirements": [
                    "Event / Competition",
                    "Achievement",
                    "Level",
                ]
            },

            "STATE_UNIVERSITY": {

                "label":
                    "State / University / "
                    "Inter-Zone Achievement",

                "points": 4,

                "requirements": [
                    "Event / Competition",
                    "Achievement",
                ]
            },

            "DISTRICT_REGIONAL": {

                "label":
                    "District / Regional Achievement",

                "points": 3,

                "requirements": [
                    "Event / Competition",
                    "Achievement",
                ]
            },

            "INSTITUTIONAL": {

                "label":
                    "Institutional-Level Achievement",

                "points": 2,

                "requirements": [
                    "Event / Competition",
                    "Achievement",
                ]
            },

            "PARTICIPATION": {

                "label":
                    "Participation",

                "points": 1,

                "requirements": [
                    "Event / Competition",
                ]
            },

            "NONE": {

                "label": "None",
                "points": 0,
                "requirements": []
            },
        }
    },
}