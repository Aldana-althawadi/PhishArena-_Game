CASES = {

    "alice@emailme.com": {
        "name": "Alice Johnson",
        "role": "Junior Staff Member",
        "department": "Student Affairs",
        "level": "Junior",
        "bio": "Alice Johnson is a junior staff member in Student Affairs.",
        "image": "images/profiles/alice.png",
        "cases": [
            {
                "case_id": "J1",
                "order_in_level": 1,
                "level": "Junior",
                "title": "School ID Verification",
                "flag": "FLAG-1234",

                "mission_brief": "A hint image contains exposed school-related information connected to Alice. Use the available details to write a believable verification email.",
                "expected_from_player": "Write a realistic and convincing email using the exposed details from the hint.",

                "required_info": ["12345", "school"],

                "owner_name": "Alice Johnson",
                "owner_role": "Junior Staff Member",
                "owner_department": "Student Affairs",

                "image": "images/cases/j1_alice.png",

                "failure_msg": "Your request does not include enough clear and believable information. Please improve your message."
            }
        ]
    },

    "bob@emailme.com": {
        "name": "Bob Smith",
        "role": "Administrative Officer",
        "department": "Student Services",
        "level": "Junior",
        "bio": "Bob Smith works in Student Services.",
        "image": "images/profiles/bob.png",
        "cases": [
            {
                "case_id": "J2",
                "order_in_level": 2,
                "level": "Junior",
                "title": "Emergency Hospital Verification",
                "flag": "FLAG-3421",

                "mission_brief": "A hint image contains information related to a student emergency connected to Bob. Use the visible details to create a believable urgent request.",
                "expected_from_player": "Write a convincing email that reflects urgency and uses the available information correctly.",

                "required_info": ["school", "hospital", "student id"],

                "owner_name": "Bob Smith",
                "owner_role": "Administrative Officer",
                "owner_department": "Student Services",

                "image": "images/cases/j2_bob.png",

                "failure_msg": "Your message is not convincing enough. Please provide stronger context and details."
            }
        ]
    },

    "charlie@emailme.com": {
        "name": "Charlie Brown",
        "role": "Attendance Coordinator",
        "department": "Attendance Office",
        "level": "Junior",
        "bio": "Charlie manages attendance records.",
        "image": "images/profiles/charlie.png",
        "cases": [
            {
                "case_id": "J3",
                "order_in_level": 3,
                "level": "Junior",
                "title": "Absence Documentation Request",
                "flag": "FLAG-6543",

                "mission_brief": "A hint image contains attendance-related information connected to Charlie. Use the available details to support an absence-related request.",
                "expected_from_player": "Write a clear and believable email using the exposed information from the hint.",

                "required_info": ["absence", "student", "documentation"],

                "owner_name": "Charlie Brown",
                "owner_role": "Attendance Coordinator",
                "owner_department": "Attendance Office",

                "image": "images/cases/j3_charlie.png",

                "failure_msg": "Your explanation is not clear enough. Add more relevant details."
            }
        ]
    },

    "steven@emailme.com": {
        "name": "Steven Clark",
        "role": "Senior Records Officer",
        "department": "Attendance and Records",
        "level": "Senior",
        "bio": "Steven handles sensitive records.",
        "image": "images/profiles/steven.png",
        "cases": [
            {
                "case_id": "S1",
                "order_in_level": 1,
                "level": "Senior",
                "title": "Parent Attendance Inquiry",
                "flag": "FLAG-5678",

                "mission_brief": "A hint image contains information related to a student attendance matter. Use the available details to write a believable request.",
                "expected_from_player": "Write a realistic and structured email that sounds credible and appropriate.",

                "required_info": ["parent", "attendance", "student"],

                "owner_name": "Steven Clark",
                "owner_role": "Senior Records Officer",
                "owner_department": "Attendance and Records",

                "image": "images/cases/s1_steven.png",

                "failure_msg": "Your request lacks credibility. Provide stronger supporting details."
            }
        ]
    },

    "eve@emailme.com": {
        "name": "Eve Adams",
        "role": "Emergency Contact Specialist",
        "department": "Student Support",
        "level": "Senior",
        "bio": "Eve manages emergency contacts.",
        "image": "images/profiles/eve.png",
        "cases": [
            {
                "case_id": "S2",
                "order_in_level": 2,
                "level": "Senior",
                "title": "Emergency Contact Update",
                "flag": "FLAG-8765",

                "mission_brief": "A hint image contains emergency contact information related to a student. Use the available details to prepare a convincing update request.",
                "expected_from_player": "Write a believable email that uses the exposed details correctly and sounds realistic.",

                "required_info": ["parent", "emergency contact", "student", "update"],

                "owner_name": "Eve Adams",
                "owner_role": "Emergency Contact Specialist",
                "owner_department": "Student Support",

                "image": "images/cases/s2_eve.png",

                "failure_msg": "Your message is incomplete. Provide clearer context."
            }
        ]
    },

    "david@emailme.com": {
        "name": "David Miller",
        "role": "Medical Leave Officer",
        "department": "Medical Services",
        "level": "Senior",
        "bio": "David handles medical leave.",
        "image": "images/profiles/david.png",
        "cases": [
            {
                "case_id": "S3",
                "order_in_level": 3,
                "level": "Senior",
                "title": "Medical Leave Verification",
                "flag": "FLAG-2109",

                "mission_brief": "A hint image contains medical-related information connected to a student. Use the available details to write a convincing request.",
                "expected_from_player": "Write a realistic email that includes the necessary details and matches the situation.",

                "required_info": ["medical", "leave", "student id", "student"],

                "owner_name": "David Miller",
                "owner_role": "Medical Leave Officer",
                "owner_department": "Medical Services",

                "image": "images/cases/s3_david.png",

                "failure_msg": "Your request is not detailed enough. Improve clarity."
            }
        ]
    },

    "sophia@emailme.com": {
        "name": "Sophia Turner",
        "role": "Head of Enrollment",
        "department": "Enrollment Office",
        "level": "Head",
        "bio": "Sophia oversees enrollment.",
        "image": "images/profiles/sophia.png",
        "cases": [
            {
                "case_id": "H1",
                "order_in_level": 1,
                "level": "Head",
                "title": "Enrollment Confirmation",
                "flag": "FLAG-9012",

                "mission_brief": "A hint image contains enrollment-related information. Use the available details to build a believable confirmation request.",
                "expected_from_player": "Write a professional email that is formal, clear, and supported by the visible details.",

                "required_info": ["enrollment", "school", "student", "confirmation"],

                "owner_name": "Sophia Turner",
                "owner_role": "Head of Enrollment",
                "owner_department": "Enrollment Office",

                "image": "images/cases/h1_sophia.png",

                "failure_msg": "Your message is not formal enough. Improve structure."
            }
        ]
    },

    "michael@emailme.com": {
        "name": "Michael Harris",
        "role": "Operations Head",
        "department": "Transport",
        "level": "Head",
        "bio": "Michael handles operations.",
        "image": "images/profiles/michael.png",
        "cases": [
            {
                "case_id": "H2",
                "order_in_level": 2,
                "level": "Head",
                "title": "Transport Emergency",
                "flag": "FLAG-4321",

                "mission_brief": "A hint image contains transportation-related details connected to an urgent situation. Use the available information to write a convincing message.",
                "expected_from_player": "Write a realistic and structured email that reflects urgency.",

                "required_info": ["student", "transportation", "urgent", "school"],

                "owner_name": "Michael Harris",
                "owner_role": "Operations Head",
                "owner_department": "Transport",

                "image": "images/cases/h2_michael.png",

                "failure_msg": "Your message lacks urgency and detail."
            }
        ]
    },

    "olivia@emailme.com": {
        "name": "Olivia Bennett",
        "role": "Chief Officer",
        "department": "Access Control",
        "level": "Chief",
        "bio": "Olivia handles access control.",
        "image": "images/profiles/olivia.png",
        "cases": [
            {
                "case_id": "C1",
                "order_in_level": 1,
                "level": "Chief",
                "title": "Access Authorization",
                "flag": "FLAG-3456",

                "mission_brief": "A hint image contains access-related information. Use the visible details to prepare a believable request.",
                "expected_from_player": "Write a professional and credible email that justifies the request clearly.",

                "required_info": ["student", "authorization", "access", "request"],

                "owner_name": "Olivia Bennett",
                "owner_role": "Chief Officer",
                "owner_department": "Access Control",

                "image": "images/cases/c1_olivia.png",

                "failure_msg": "Your request is not justified enough."
            }
        ]
    },

    "daniel@emailme.com": {
        "name": "Daniel Walker",
        "role": "Executive Director",
        "department": "Institutional Affairs",
        "level": "CEO",
        "bio": "Daniel is the executive director.",
        "image": "images/profiles/daniel.png",
        "cases": [
            {
                "case_id": "CEO1",
                "order_in_level": 1,
                "level": "CEO",
                "title": "Executive Escalation",
                "flag": "FLAG-7890",

                "mission_brief": "A hint image contains high-level institutional details connected to Daniel. Use the available information to construct a convincing escalation request.",
                "expected_from_player": "Write a highly professional email that matches the seriousness of the situation.",

                "required_info": ["student", "verification", "institution", "escalation", "request"],

                "owner_name": "Daniel Walker",
                "owner_role": "Executive Director",
                "owner_department": "Institutional Affairs",

                "image": "images/cases/ceo1_daniel.png",

                "failure_msg": "Your request is not formal or strong enough."
            }
        ]
    }
}

ACTIVE_CASE = {
    email: 0 for email in CASES
}